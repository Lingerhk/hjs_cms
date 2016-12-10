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

class ViewApiOrderList(ViewBase):
    def __init__(self):
        self._rDict = {
            "page": {'n': "page", 't': int, 'v': 1},
            "length": {'n': "length", 't': int, 'v': 20},
            "status": {'n': "status", 't': str, 'v': 'normal'},
            "search": {'n': "search", 't': str, 'v': ''}
        }
    
    def _check_param(self):
        bRet, sRet = super(ViewApiOrderList, self)._check_param()
        if not bRet:
            return bRet, sRet
        return True, None

    def _deal_order_list(self):
        return HjsOrder.order_list(self.page, self.length, self.status, self.search)

    # get all order list
    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            return web.seeother("/login")
        bRet, orderList = self.process(self._deal_order_list)
        if not bRet:
            Log.err("deal_order_list: %s" % (str(orderList)))
            return self.make_error(orderList)

        return self.make_response(orderList)

    # do search the order list
    def POST(self):
        bRet, sRet = self.check_login()
        if not bRet:
            return web.seeother("/login")
        bRet, orderList = self.process(self._deal_order_list)
        if not bRet:
            Log.err("deal_search_order_list: %s" % (str(orderList)))
            return self.make_error(orderList)

        return self.make_response(orderList)


class ViewApiOrderToday(ViewBase):
    def GET(self):
        pass


class ViewApiOrderCancel(ViewBase):
    def GET(self):
        pass



class ViewApiOrderAdd(ViewBase):
    def GET(self):
        pass


class ViewApiOrderDel(ViewBase):
    def GET(self):
        pass








