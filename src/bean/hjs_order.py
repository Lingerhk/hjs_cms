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
from hjs_user_dao import *
from hjs_order_dao import *


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
            order_info.order_tm = str(item['insert_tm'])
            order_info.start_tm = str(item['start_tm'])
            order_info.end_tm = str(item['end_tm'])
            order_info.amount = item['amount']
            order_info.cash = item['cash']
            order_info.remark = item['remark']
            order_info.insert_tm = str(item['insert_tm'])
            orderList.append(order_info)

        return True, HjsOrder._page_data(orderList, status, search, pg)













if __name__ == "__main__":
    pass


