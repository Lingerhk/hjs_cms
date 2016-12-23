# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: custom处理逻辑 

if __name__ == "__main__":
    import sys
    import os
    
    sys.path.append("..")
    sys.path.append("../base")
    sys.path.append("../dao")

from web.utils import *
from hjs_cfg import *
from bs_util import *
from hjs_custom_dao import *


class CustomStatus:
    NORMAL = 'normal'
    CANCEL = 'cancel'
    DELETE = 'delete'
    ALL    = 'all'


class HjsCustom:


    @staticmethod
    def _page_data(data_list, status, search, page):
        if not isinstance(page, Page):
            return data_list
        return {
            "page_count": page.page_count,
            "current": page.page_index,
            "custom_list": data_list,
            "custom_query": {"status": status, "search": search}
        }
    

    @staticmethod
    def custom_list(page, length, status=None, search=None):
        allow_status = [CustomStatus.ALL, CustomStatus.NORMAL, CustomStatus.CANCEL, CustomStatus.DELETE]
        if status and (status not in allow_status):
            return False, 'param(status) not define'

        bRet, count = HjsCustomDao.query_node_count(status, search)
        if not bRet:
            return False, count

        pg = Page(count, page, length)
        bRet, sRet = HjsCustomDao.query_node_list(pg.offset, pg.limit, status, search)
        if not bRet:
            Log.err('list custom fail: %s' % str(sRet))
            return False, sRet
        if len(sRet) == 0:
            return True, None
        
        customList = list()
        for item in sRet:
            custom_info = storage()
            custom_info.cid = int(item['cid'])
            custom_info.name = item['name']
            custom_info.address = item['address']
            custom_info.phone = item['phone']
            custom_info.ctype = item['ctype']
            custom_info.class_priv = item['class']
            custom_info.status = item['status']
            custom_info.remark = item['remark']
            custom_info.insert_tm = str(item['insert_tm'])
            customList.append(custom_info)

        return True, HjsCustom._page_data(customList, status, search, pg)


    @staticmethod
    def custom_add(nickName, Address, Phone, Ctype, Class, Remark):
        bRet, sRet = HjsCustomDao.insert_node(nickName, Address, Phone, Ctype, Class, Remark)
        if not bRet:
            return False, sRet
        return True, sRet

        
    @staticmethod
    def custom_info(cId):
        bRet, cInfo = HjsCustomDao.query_node_by_cid(cId)
        if not bRet:
            return False, cInfo
        custom_info = storage()
        custom_info.cid = int(cInfo['cid'])
        custom_info.name = cInfo['name']
        custom_info.address = cInfo['address']
        custom_info.phone = cInfo['phone']
        custom_info.ctype = cInfo['ctype']
        custom_info.class_priv = cInfo['class']
        custom_info.status = cInfo['status']
        custom_info.remark = cInfo['remark']

        return True, custom_info


    @staticmethod
    def custom_update(cId, nickName, Address, Phone, Ctype, Class, Status, Remark):
        bRet, sRet = HjsCustomDao.update_node(cId, nickName, Address, Phone, Ctype, Class, Status, Remark)
        if not bRet:
            return False, sRet
        return True, sRet


    @staticmethod
    def custom_del(cId):
        bRet, sRet = HjsCustomDao.delete_node_by_cid(cId)
        if not bRet:
            return False, sRet
        return True, sRet


if __name__=="__main__":

    def test_custom_list():
        print HjsCustom.custom_list(1, 20, 'normal', '')

    def test_custom_add():
        nickName = "zhangxicheng"
        Address = "city_12_a"
        Phone = "18829252920"
        Ctype = "N"
        Class = "A"
        Status = "normal"
        Remark = "xxxx"
        print HjsCustom.custom_add(nickName, Address, Phone, Ctype, Class, Status, Remark)

    def test_custom_info():
        print HjsCustom.custom_info(1002)

    def test_custom_update():
        cId = 1002
        nickName = "zhangxicheng"
        Address = "city_12_a"
        Phone = "18829252920"
        Ctype = "N"
        Class = "A"
        Status = "normal"
        Remark = "xxxx"
        print HjsCustom.custom_add(nickName, Address, Phone, Ctype, Class, Status, Remark)

    def test_custom_del():
        print HjsCustom.custom_del(1003)

    # test ing ...

    test_custom_info()

