# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: custom view


from view_base import *
from hjs_user import *
from hjs_user_dao import *
from hjs_order_dao import *
from hjs_custom_dao import *


class ViewCustomList(ViewBase):

    def GET(self):
        if not self.check_login():
            Log.err("user not login")
            return web.seeother("/login")
        return render.custom_list()

class ViewCustomSearch(ViewBase):
    def GET(self):
        if not self.check_login():
            Log.err("user not login")
            return web.seeother("/login")
        return render.custom_search()

class ViewCustomAdd(ViewBase):
    def GET(self):
        if not self.check_login():
            Log.err("user not login")
            return web.seeother("/login")
        return render.custom_add()



class ViewApiCustomList(ViewBase):

    def GET(self):
        pass

class ViewApiCustomSearch(ViewBase):

    def POST(self):
        pass

class ViewApiCustomAdd(ViewBase):

    def POST(self):
        pass
