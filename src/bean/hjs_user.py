# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: user处理逻辑

if __name__ == "__main__":
    import sys
    import os

    sys.path.append("../base")
    sys.path.append("..")
    sys.path.append("../dao")

from web.utils import *
from bs_util import *
from hjs_user_dao import *
from hjs_order_dao import *
from hjs_custom_dao import *


class HjsUser:
    
    @staticmethod
    def user_list(userName):
        bRet, sRet = HjsUserDao.query_node_user_list()
        if not bRet:
            return False, sRet
        userList = list()
        for item in sRet:
            user_info = storage()
            user_info.uid = int(item['uid'])
            user_info.username = item['username']
            user_info.nickname = item['nickname']
            user_info.password = item['password']
            user_info.phone = item['phone']
            user_info.email = item['email']
            user_info.priv = item['privilege']
            user_info.lastlogin = str(item['lastlogin'])
            userList.append(user_info)

        return True, userList




if __name__ == "__main__":
    print HjsUser.user_list('admin')


