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


class HjsCustom:
    
    @staticmethod
    def custom_list(uId, page, length, search):
        bRet, sRet = HjsCustomDao.query_node_list(uId, page, length, search)
        if not bRet:
            return False, sRet
        
        return True, sRet

    @staticmethod
    def custom_add(nickName, Address, Phone, Ctype, Class, Status, Remark):
        bRet, sRet = HjsCustomDao.insert_node(nickName, Address, Phone, Ctype, Class, Status, Remark)
        if not bRet:
            return False, sRet
        return True sRet

    @staticmethod
    def custom_update(cId, nickName, Address, Phone, Ctype, Class, Status, Remark):
        bRet, sRet = HjsCustomDao.update_node(uId, nickName, Address, Phone, Ctype, Class, Status, Remark)
        if not bRet:
            return False, sRet
        return True, sRet

    @staticmethod
    def custom_del(cId):
        bRet, sRet = HjsCustomDao.del_node_custom(cId)
        if not bRet:
            return False, sRet
        return True, sRet












if __name__ == "__main__":
    pass


