# -*- coding: utf-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: tb_custom_dao


'''
# 客户表
CREATE TABLE `tb_custom` (
`cid` int(10) NOT NULL AUTO_INCREMENT,
`name` varchar(50) NOT NULL,
`address` varchar(100) NOT NULL,
`phone` varchar(50) DEFAULT NULL,
`ctype` varchar(10) DEFAULT NULL,
`class` varchar(10) DEFAULT 'A',
`status` enum('normal','cancel') NOT NULL DEFAULT 'normal',
`remark` text,
`insert_tm` datetime DEFAULT NULL,
PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    sys.path.append("../base")

from hjs_cfg import *
from bs_util import *
from bs_database_pid import *


class HjsCustomDao:

    @staticmethod
    def query_node_list(offset, limit, search):
        dataBase = DataBase()
        sql = "select * from (select * from tb_custom"


    @staticmethod
    def insert_node_custom(nickName, Address, Phone, Ctype, Class, Status, Remark):

        dataBase = DataBase()
        sql = "insert into tb_custom(name, address, phone, ctype, status, class, remark, insert_tm) " \
              "values(%s, %s, %s, %s, %s, %s, %s, %s)"
        param = (nickName, Address, Phone, Ctype, Class, Status, Remark, get_cur_time())

        bRet, sRet = dataBase.insert_data(sql, param)
        return bRet, sRet

    @staticmethod
    def query_node_by_id(user_id, task_id):
        
        dataBase = DataBase()
        sql = "select * from tb_task where user_id = %s and task_id = %s"
        param = (user_id, task_id)
        
        bRet, sRet = dataBase.query_data(sql, param)
        if not bRet: return False, sRet
        return True, sRet

    @staticmethod
    def query_node_add()


