# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: order view


from view_base import *
from hjs_user import *
from hjs_order import *
from hjs_ps_order import *

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
            return False, sRet
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
    def _deal_order_today(self):
        return HjsOrder.order_today()

    # order list today
    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            return web.seeother("/login")
        bRet, sRet = self.process(self._deal_order_today)
        if not bRet:
            Log.err("deal_order_today: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)


class ViewApiOrderAdd(ViewBase):
    def __init__(self):
        self._rDict = {
            "cid": {'n': "cId", 't': int, 'v': None},
            "otype": {'n': "otype", 't': str, 'v': None},
            "order_tm": {'n': "order_tm", 't': str, 'v': ''},
            "start_tm": {'n': "start_tm", 't': str, 'v': None},
            "end_tm": {'n': "end_tm", 't': str, 'v': None},
            "amount": {'n': "amount", 't': str, 'v': None},
            "cash": {'n': "cash", 't': str, 'v': None},
            "remark": {'n': "remark", 't': str, 'v': None}
        }

    def _check_param(self):
        bRet, sRet = super(ViewApiOrderAdd, self)._check_param()
        if not bRet:
            return False, sRet
        return True, None

    def _deal_order_add(self):
        bRet, is_admin = HjsUser.is_admin(self.get_user_name())
        if not bRet:
            return False, sRet
        if not is_admin:
            return False, 'No permission to do this'

        return HjsOrder.order_add(self.cId, self.otype, self.order_tm, self.start_tm, self.end_tm, self.amount, self.cash, self.remark)

    def POST(self):
        bRet, sRet = self.check_login()
        if not bRet:
            return web.seeother("/login")
        bRet, sRet = self.process(self._deal_order_add)
        if not bRet:
            Log.err("deal_order_add: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(ViewBase.RetMsg.MSG_SUCCESS)


class ViewApiOrderDel(ViewBase):
    def __init__(self):
        self._rDict = {
            "oid": {'n': "oId", 't': int, 'v': None},
        }

    def _check_param(self):
        bRet, sRet = super(ViewApiOrderDel, self)._check_param()
        if not bRet:
            return False, sRet
        return True, None

    def _deal_order_del(self):
        bRet, is_admin = HjsUser.is_admin(self.get_user_name())
        if not bRet:
            return False, sRet
        if not is_admin:
            return False, 'No permission to do this'

        return HjsOrder.order_del(self.oId)

    def POST(self):
        bRet, sRet = self.check_login()
        if not bRet:
            return web.seeother("/login")
        bRet, sRet = self.process(self._deal_order_del)
        if not bRet:
            Log.err("deal_order_del: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(ViewBase.RetMsg.MSG_SUCCESS)


class ViewApiOrderPauseList(ViewBase):
    def _deal_order_pause_list(self):
        return HjsOrderPause.order_list()

    # pause order list
    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            return web.seeother("/login")
        bRet, sRet = self.process(self._deal_order_pause_list)
        if not bRet:
            Log.err("deal_pause_order_list: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)


class ViewApiOrderPauseAdd(ViewBase):
    def __init__(self):
        self._rDict = { 
            "oid": {'n': "oId", 't': int, 'v': None},
            "pause_tm": {'n': "pause_tm", 't': str, 'v': None},
            "remark": {'n': "remark", 't': str, 'v': None}
        }
    
    def _check_param(self):
        bRet, sRet = super(ViewApiOrderPauseAdd, self)._check_param()
        if not bRet:
            return False, sRet
        return True, None

    def _deal_order_pause_add(self):
        bRet, is_admin = HjsUser.is_admin(self.get_user_name())
        if not bRet:
            return False, sRet
        if not is_admin:
            return False, 'No permission to do this'

        return HjsOrderPause.order_add(self.oId, self.pause_tm, self.remark)

    # pause order add
    def POST(self):
        bRet, sRet = self.check_login()
        if not bRet:
            return web.seeother("/login")
        bRet, sRet = self.process(self._deal_order_pause_add)
        if not bRet:
            Log.err("deal_pause_order_add: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(ViewBase.RetMsg.MSG_SUCCESS)


class ViewApiOrderPauseDel(ViewBase):
    def __init__(self):
        self._rDict = { 
            "pid": {'n': "pId", 't': int, 'v': None}
        }
    
    def _check_param(self):
        bRet, sRet = super(ViewApiOrderPauseDel, self)._check_param()
        if not bRet:
            return False, sRet
        
        return True, None

    def _deal_order_pause_del(self):
        bRet, is_admin = HjsUser.is_admin(self.get_user_name())
        if not bRet:
            return False, sRet
        if not is_admin:
            return False, 'No permission to do this'

        return HjsOrderPause.order_del(self.pId)

    # pause order del
    def POST(self):
        bRet, sRet = self.check_login()
        if not bRet:
            return web.seeother("/login")
        bRet, sRet = self.process(self._deal_order_pause_del)
        if not bRet:
            Log.err("deal_pause_order_del: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(ViewBase.RetMsg.MSG_SUCCESS)



