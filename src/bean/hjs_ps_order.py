# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: order 暂取消处理逻辑 


if __name__ == "__main__":
    import sys
    import os

    sys.path.append("..")
    sys.path.append("../base")
    sys.path.append("../dao")

from web.utils import *
from hjs_cfg import *
from bs_util import *
from hjs_order_dao import *
from hjs_ps_order_dao import *

class HjsOrderPause:

    @staticmethod
    def order_list():
        bRet, sRet = HjsOrderPauseDao.query_node_list()
        if not bRet:
            Log.err('list pause order fail: %s' % str(sRet))
            return False, sRet
        if len(sRet) == 0:
            return True, None
        
        orderPsList = list()
        for item in sRet:
            pause_info = storage()
            pause_info.pid = int(item['pid'])
            pause_info.oid = int(item['oid'])
            pause_info.cid = int(item['cid'])
            pause_info.name = item['name']
            pause_info.pause_tm = str(item['pause_tm'])
            pause_info.remark = item['remark']
            pause_info.insert_tm = str(item['insert_tm'])
            orderPsList.append(pause_info)

        return True, orderPsList


    @staticmethod
    def order_add(oId, pause_tm, remark):
        bRet, order = HjsOrderDao.query_node_by_oid(oId)
        if not bRet:
            return False, order
        
        cid = order['cid'] if order.has_key('cid') else ''
        name = order['name'] if order.has_key('name') else ''
        
        return HjsOrderPauseDao.insert_node(oId, cid, name, pause_tm, remark)


    @staticmethod
    def order_del(pId):
        bRet, sRet = HjsOrderPauseDao.delete_node_by_pid(pId)
        if not bRet:
            return False, sRet
        
        return True, sRet


if __name__ == "__main__":
    pass


