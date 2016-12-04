# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: 完成参数提取与校验


import web
from web_util import *
from bs_log import *
#from hjs_cfg import *
import os
import re

from xml.etree import ElementTree as ET

t_globals = dict(datestr=web.datestr, )
curPath = os.path.abspath(os.path.dirname(__file__))
render = web.template.render(curPath + '/../templates', globals=t_globals)
render._keywords['globals']['render'] = render


class Session:
    session = None

    @staticmethod
    def init(app):
        if Session.session == None:
            Session.session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={})

    @staticmethod
    def set_val(key, val):
        Session.session[key] = val

    @staticmethod
    def get_val(key):
        if Session.session is None: return None
        if Session.session.has_key(key) is False: return None
        return Session.session.get(key)


render._keywords['globals']['session'] = Session


# 请求基础类， 完成参数提取校验
class ViewBase(object):
    class RetCode:
        T_SUCCESS = 201
        T_ERROR = 101

    class RetMsg:
        MSG_SUCCESS = "Success"

    SEPCODE_RE = re.compile(r'.*[\"\']+')
    TEMPLATE = ""

    def __init__(self):
        self._rDict = {}
        self.param = {}

    # 参数校验
    def _check_param(self):
        for name in self._rDict.keys():
            keyName = self._rDict[name]['n'] if self._rDict[name].has_key('n') else name
            value = getattr(self, keyName, None)
            if value is None:
                return False, "param(%s) is None" % (str(keyName))
            if isinstance(value, str) and self.SEPCODE_RE.match(value) is not None:
                return False, u"不允许输入特殊字符"
        return True, None

    # 参数提取
    def _get_req_param(self):
        for name in self._rDict.keys():
            valueType = str
            if self._rDict[name].has_key('t'): valueType = self._rDict[name]['t']
            defaultVal = None
            if self._rDict[name].has_key('v'): defaultVal = self._rDict[name]['v']

            value = get_req_qstr(name, defaultVal, valueType)
            if self._rDict[name].has_key('n'):
                keyName = self._rDict[name]['n']
            else:
                keyName = name
            object.__setattr__(self, keyName, value)

        return self._check_param()

    def process(self, _process=None):
        try:
            bret, sret = self._get_req_param()
            Log.info("****REQ(%s?%s): %s" % (get_req_path_info(), get_req_all_param(), sret))
            if bret != True:
                return False, sret
            if _process is not None:
                bret, sret = _process()
                return bret, sret
            return bret, sret

        except Exception, e:
            Log.err("req(%s?%s): ERROR(%s)" % (get_req_path_info(), get_req_all_param(), traceback.format_exc()))
            return False, "req: %s ERROR(%s)" % (get_req_path_info(), str(e))

    def get_error_html(self, errInfo):
        htmlCnt = []
        htmlCnt.append("<html>")
        htmlCnt.append("<head>")
        htmlCnt.append("<title>  ERR req   </title>")
        htmlCnt.append("</head>")
        htmlCnt.append("<body>")
        htmlCnt.append("<center>")
        htmlCnt.append("</br></br></br>")
        htmlCnt.append("<h2> ERR req  </h2>")
        htmlCnt.append("</br>")
        htmlCnt.append("</br>")
        if errInfo == None: errInfo = "ERROR"
        htmlCnt.append("%s" % (str(errInfo)))
        htmlCnt.append("</center>")
        htmlCnt.append("</body>")
        htmlCnt.append("</html>")
        cnt = "".join(htmlCnt)
        return htmlCnt

    def get_json(self, retCode, retValue):
        try:
            # jaymiao 2015-11-13 for xss defense
            web.header('Content-Type', 'application/json')
            retJson = {"code": retCode, "result": retValue}
            return json.dumps(retJson, encoding='utf-8')
        except Exception, e:
            Log.err("%s" % (str(e)))
            retJson = {"code": retCode, "message": "please hi me!"}
            return json.dumps(retJson)

    def get_result(self, retType, retCode, retValue):
        if retType == "json":
            return self.get_json(retCode, retValue)
        else:
            return retValue

    def make_response(self, result):
        """ 构建response对象 """
        try:
            ret = {
                "message": "OK",
                "code": ViewBase.RetCode.T_SUCCESS,
                "result": self.html_encode_result(result)
            }
            web.header('Content-Type', 'application/json')
            Log.info("****RESP: %s" % ret)
            return json.dumps(ret, encoding='utf-8')
        except Exception, e:
            Log.err("%s" % (str(e)))
            retJson = {"code": ViewBase.RetCode.T_ERROR, "message": "please hi me!"}
            return json.dumps(retJson)

    def make_error(self, result):
        """构建error对象"""
        ret = {
            "message": result,
            "code": ViewBase.RetCode.T_ERROR,
        }
        Log.info("****RESP: %s" % ret)
        return json.dumps(ret)

    def make_csv_response(self, datas, csv_name='download'):
        def __encode_gbk(data):
            new_data = []
            for x in data:
                if isinstance(x, basestring):
                    x = x.encode("gbk", "ignore") if isinstance(x, unicode) else x
                new_data.append(x)
            return new_data

        web.header('Content-Type', 'text/csv;charset=utf-8')
        web.header('Content-Disposition', 'attachment; filename=%s.csv' % csv_name)

        writer = CSVWriter()
        for data in datas:
            data = __encode_gbk(data)
            yield writer.writerow(data)

    def html_encode(self, cnt):
        return web.websafe(cnt)

    def html_encode_result(self, result):
        if type(result) == str:
            return self.html_encode(result)

        if type(result) == list:
            for i in range(len(result)):
                result[i] = self.html_encode_result(result[i])
            return result

        if type(result) == dict:
            for key in result:
                result[key] = self.html_encode_result(result[key])

            return result

        return result

    # 校验权限
    def check_login(self):

        if Session.get_val("username") == None:
            return False, web.seeother("/login")

        return True, None

    def get_user_name(self):
        return Session.get_val("username")

    def GET(self):
        # 不能影响依赖方对数据的接收格式
        try:
            return self.process()
        except Exception, e:
            Log.err("%s" % (str(traceback.format_exc())))
            return self.get_json(ViewBase.RetCode.T_ERROR, "ERROR_ERROR")

    def POST(self):
        try:
            return self.process()
        except Exception, e:
            Log.err("%s" % (str(traceback.format_exc())))
            return self.get_json(ViewBase.RetCode.T_ERROR, "ERROR_ERROR")
