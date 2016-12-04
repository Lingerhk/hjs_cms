# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: login view


from view_base import *
from hjs_user_dao import *
import web

class ViewLogin(ViewBase):
    def __init__(self):
        self._rDict = {
            "username": {'n': 'userName', 't': str, 'v': None},
            "password": {'n': 'passWord', 't': str, 'v': None}
        }

    def _check_param(self):

        if not self.userName: return False, "param(username) is None!"
        if not self.passWord: return False, "param(password) is NOne!"

        return True, None

    def GET(self):
        return render.login()

    def _deal_login(self):

        bRet, sRet = HjsUserDao.query_node_by_username(self.userName)
        if not bRet:  return False, "username does not exist!"
        
        if sRet['password'] != self.passWord:
        #if record['passwd'] != comput_md5_text(salt + self.passWord):
            return False, u"用户名或密码错误"

        Session.set_val("username", self.userName)
        web.setcookie("username", self.userName)
        return True, None

    def POST(self):

        bRet, sRet = self.process(self._deal_login)
        if not bRet:
            Log.err("deal_login: %s" % (str(sRet)))
            return self.make_error(sRet)
        
        return render.index()


class ViewLogout(ViewBase):
    def GET(self):
        Session.set_val("username", None)
        web.setcookie("username", None)
        return web.seeother("/login")

    def POST(self):
        return self.GET()


if __name__ == "__main__":

    def test_login():
        Session.session = {}
        viewLogin = ViewLogin()
        viewLogin.userName = 'moresec'
        viewLogin.password = 'test'
        bRet, sRet = viewLogin._deal_login()
        if not bRet:
            Log.err("test_case ERR! %s" % (str(sRet)))
        else:
            Log.info("test_case SUCCESS!")

    test_login()
