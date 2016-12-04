# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: index view

from view_base import *
from hjs_user_dao import *
from hjs_order_dao import *
from hjs_custom_dao import *


class ViewIndex(ViewBase):
    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("user not login!")
            return web.seeother("/login")
        
        return render.index()

    def POST(self):
        return self.GET()


class ViewApiDataCount(ViewBase):

    def GET(self):
        pass
