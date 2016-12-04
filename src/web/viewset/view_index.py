# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: index view

from view_base import *
from hjs_user import *
from hjs_index import *


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
    def _deal_data_show(self):
        return HjsIndex.data_show(self.get_user_name())


    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")

        bRet, sRet = self.process(self._deal_data_show)
        if not bRet:
            Log.err("deal_user_list: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)



