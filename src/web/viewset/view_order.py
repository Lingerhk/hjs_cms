# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: order view


from view_base import *
from hjs_user import *
from hjs_user_dao import *
from hjs_order import *
from hjs_order_dao import *


class ViewOrderAll(ViewBase):
    def GET(self):
        if not self.check_login():
            Log.err("user not login")
            return web.seeother("/login")
        return render.order_all()

class ViewOrderToday(ViewBase):
    def GET(self):
        if not self.check_login():
            Log.err("user not login")
            return web.seeother("/login")
        return render.order_today()

class ViewOrderCancel(ViewBase):
    def GET(self):
        if not self.check_login():
            Log.err("user not login")
            return web.seeother("/login")
        return render.order_cancel()

class ViewApiOrderAll(ViewBase):
    def GET(self):
        pass


class ViewApiOrderToday(ViewBase):
    def GET(self):
        pass


class ViewApiOrderCancel(ViewBase):
    def GET(self):
        pass

