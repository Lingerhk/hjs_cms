# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: order处理逻辑 


if __name__ == "__main__":
    import sys
    import os

    sys.path.append("..")
    sys.path.append("../base")
    sys.path.append("../dao")

from web.utils import *
from hjs_cfg import *
from bs_util import *
from bs_time import *
from hjs_user_dao import *
from hjs_order_dao import *
from hjs_ps_order_dao import *
from hjs_custom_dao import *


class OrderStatus:
    ALL    = 'all'
    STOP   = 'stop'
    NORMAL = 'normal'
    DELETE = 'delete'


class HjsOrder:

    @staticmethod
    def _page_data(data_list, status, search, page):
        if not isinstance(page, Page):
            return data_list
        return {
            "page_count": page.page_count,
            "current": page.page_index,
            "order_list": data_list,
            "order_query": {"status": status, "search": search}
        }


    @staticmethod
    def order_list(page, length, status=None, search=None):
        allow_status = [OrderStatus.ALL, OrderStatus.NORMAL, OrderStatus.STOP, OrderStatus.DELETE]
        if status and (status not in allow_status):
            return False, 'param(status) not define'

        bRet, count = HjsOrderDao.query_node_count(status, search)
        if not bRet:
            return False, count

        pg = Page(count, page, length)
        bRet, sRet = HjsOrderDao.query_node_list(pg.offset, pg.limit, status, search)
        if not bRet:
            Log.err('list order fail: %s' % str(sRet))
            return False, sRet
        if len(sRet) == 0:
            return True, None
        
        orderList = list()
        for item in sRet:
            order_info = storage()
            order_info.oid = int(item['oid'])
            order_info.cid = int(item['cid'])
            order_info.name = item['name']
            order_info.order_tm = str(item['order_tm'])
            order_info.start_tm = str(item['start_tm'])
            order_info.end_tm = str(item['end_tm'])
            order_info.amount = item['amount']
            order_info.cash = item['cash']
            order_info.remark = item['remark']
            order_info.insert_tm = str(item['insert_tm'])
            orderList.append(order_info)

        return True, HjsOrder._page_data(orderList, status, search, pg)


    @staticmethod
    def order_today(status='normal', days=0):
        tg_date = get_cur_day(days, format="%Y-%m-%d")
        bRet, orderList_tmp = HjsOrderDao.query_node_by_date(status, tg_date)
        if not bRet:
            return False, orderList
        
        bRet, sRet = HjsOrderPauseDao.query_node_by_date(tg_date)
        if not bRet:
            return False, sRet
        
        pauseList = list()
        for item in sRet:
            if item.has_key('oid'):
                pauseList.append(item['oid'])

        orderList = list()
        for item in orderList_tmp:
            if item['oid'] in pauseList: continue
            
            order_info = storage()
            order_info.oid = int(item['oid'])
            order_info.cid = int(item['cid'])
            order_info.name = item['name']
            order_info.remark = item['remark']
            
            bRet, custom_info = HjsCustomDao.query_node_by_cid(order_info.cid)
            order_info.address = custom_info['address'] if bRet else ''
            order_info.phone = custom_info['phone'] if bRet else ''

            orderList.append(order_info)

        return True, orderList


    @staticmethod
    def order_add(cId, otype, order_tm, start_tm, end_tm, amount, cash, remark):
        bRet, custom_info = HjsCustomDao.query_node_by_cid(cId)
        name = custom_info['name'] if bRet else ''

        return HjsOrderDao.insert_node(cId, name, otype, order_tm, start_tm, end_tm, amount, cash, remark)


    @staticmethod
    def order_del(oId):
        return HjsOrderDao.update_node_status(oId, 'stop')




if __name__ == "__main__":
    
    print HjsOrder.order_today() 


