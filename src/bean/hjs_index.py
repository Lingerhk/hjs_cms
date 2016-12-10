# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: index data展示

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
from hjs_custom_dao import *


class HjsIndex:

    @staticmethod
    def _get_custom_data():
        bRet, custom_cnt = HjsCustomDao.query_node_by_status('all')
        if not bRet: custom_cnt = 0

        bRet, custom_nor = HjsCustomDao.query_node_by_status('normal')
        if not bRet: custom_nor = 0

        bRet, custom_can = HjsCustomDao.query_node_by_status('cancel')
        if not bRet: custom_can = 0

        return  {
            "custom_cnt": custom_cnt,
            "custom_nor": custom_nor,
            "custom_can": custom_can
        }


    @staticmethod
    def _get_order_data():
        bRet, order_cnt = HjsOrderDao.query_node_by_status('all')
        if not bRet: order_cnt = 0

        bRet, order_nor = HjsOrderDao.query_node_by_status('normal')
        if not bRet: order_nor = 0

        bRet, order_stop = HjsOrderDao.query_node_by_status('stop')
        if not bRet: order_stop = 0

        return {
            "order_cnt": order_cnt, 
            "order_nor": order_nor,
            "order_stop": order_stop
        }


    @staticmethod
    def _get_expire_order():
        bRet, daysList_3 = HjsOrderDao.query_node_by_days(3)
        if not bRet: daysList_3 = ''
        
        bRet, daysList_7 = HjsOrderDao.query_node_by_days(7)
        if not bRet: daysList_7 = ''

        return {
            "days_3": {"count": len(daysList_3), "list": daysList_3},
            "days_7": {"count": len(daysList_7), "list": daysList_7}
        }


    @staticmethod
    def data_show(userName):
        datas = {
            "dt_custom": HjsIndex._get_custom_data(),
            "dt_order": HjsIndex._get_order_data(),
            "dt_days": HjsIndex._get_expire_order()
        }
        
        return True, datas




if __name__ == "__main__":

    bRet, sRet = HjsIndex.data_show('admin')

    print '>>>> ', sRet

    #print HjsIndex._get_expire_order()


