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
from hjs_user_dao import *
from hjs_order_dao import *
from hjs_custom_dao import *


class HjsIndex:
    
    @staticmethod
    def data_show(userName):
        return True, sRet

if __name__ == "__main__":
    print HjsIndex.data_show('admin')


