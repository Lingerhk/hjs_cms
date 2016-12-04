# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: user view


from view_base import *
from hjs_user import *
from hjs_user_dao import *
from hjs_order_dao import *
from hjs_custom_dao import *


class ViewUserList(ViewBase):
    def GET(self):
        if not self.check_login():
            Log.err("user not login")
            return web.seeother("/login")
        return render.user_list()

class ViewUserAdd(ViewBase):
    def GET(self):
        if not self.check_login():
            Log.err("user not login")
            return web.seeother("/login")
        return render.user_add()

class ViewApiUserList(ViewBase):
    def _deal_user_list(self):
        return HjsUser.user_list(self.get_user_name())

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")

        bRet, sRet = self.process(self._deal_user_list)
        if not bRet:
            Log.err("deal_user_del: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)


class ViewApiUserAdd(ViewBase):
    def __init__(self):
        self._rDict = {
            "user_name": {'n': 'userName', 't': str, 'v': None}
        }

    def _check_param(self):
        return True, ''

    def _get_user_info(self):
        if not self.userName:
            return MssBuUser.get_user_info(self.get_user_name())
        bRet, is_admin = MssBuUser.is_admin(self.get_user_name())
        if not bRet:
            return False, bRet
        if is_admin:
            return MssBuUser.get_user_info(self.userName)
        return False, "No permission get other info"

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")

        bRet, sRet = self.process(self._get_user_info)
        if not bRet:
            Log.err("[GetUserInfo]: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)
