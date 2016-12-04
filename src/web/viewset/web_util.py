 # -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: web.py 框架相关方法封装


if __name__ == "__main__":
    import sys
    sys.path.append("../base")

import web
from bs_log import *
from bs_util import *


# webpy 框架环境有关的方法
def get_req_all_param():
    params = web.input()

    retParams = {}
    for node in params.items():
        if type(node[1]) == unicode:
            retParams[node[0]] = node[1].encode('utf-8')
        else:
            retParams[node[0]] = node[1]

    return retParams


def get_req_path_info():
    return web.ctx.env['PATH_INFO']


def get_req_method():
    return web.ctx.env['REQUEST_METHOD']


def is_get_method():
    if get_req_method() == 'GET': return True
    return False


def get_client_ip():
    if web.ctx.env.has_key('HTTP_X_FORWARDED_FOR'):
        return web.ctx.env['HTTP_X_FORWARDED_FOR']
    else:
        return web.ctx.env['REMOTE_ADDR']


def set_cookie(key, value):
    web.setcookie(key, value, 3600 + 24 * 3600)


def get_cookie(key):
    try:
        cookies = web.cookies()
        return cookies.get(key)
    except:
        return None


def get_req_qstr(key, defaultVal=None, ttype=str):
    if is_get_method():
        val = web.input().get(key, defaultVal)
    else:
        val = getattr(web.input(), key, defaultVal)

    if type(val) == unicode:
        val = val.encode('utf-8')

    # Log.debug("key = %s, val = %s, default = %s, dtype = %s" % (key, val, defaultVal, ttype))

    if val == None or val == "":
        return defaultVal
    if ttype == int:
        return int(val)
    if ttype == str:
        return val

    return defaultVal


def get_result_json(bret, val):
    if val == None:
        if bret == True:
            val = "SUCCESS!"
        else:
            val = "ERROR!"

    retDict = {
        'return_code': int(bret),
        'return_str': str(val)
    }
    web.header('Content-Type', 'application/json')
    return json.dumps(retDict)


def decode_all(sMsg):
    def decode(source, encoding):
        try:
            return source.decode(encoding)
        except:
            return None

    dMsg = decode(sMsg, 'GB')
    if dMsg:  return dMsg

    dMsg = decode(sMsg, 'UTF8')
    if dMsg:  return dMsg

    return sMsg


def get_web_ip_port():
    cmd = "ps aux | grep python | grep ms_web_main.py | awk '{print $13}'"

    bRet, sRet = exec_cmd(cmd)
    if bRet == 0 and sRet != "":
        sRet = sRet.split("\n")[0]
        return True, sRet

    # ip = get_local_ip()
    # if ip != None:
    #     return True, ip

    return False, None


if __name__ == "__main__":
    print get_web_ip_port()
