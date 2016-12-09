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
`ctype` enum('N', 'O') NOT NULL DEFAULT 'N',
`class` varchar(10) DEFAULT 'A',
`status` enum('normal','cancel', 'delete') NOT NULL DEFAULT 'normal',
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
    def query_node_list(offset, limit, status, search):
        dataBase = DataBase()
        sql = "select * from tb_custom where 1=1 "
        param = []
        if status and status != 'all':
            sql += "and status = %s "
            param.append(status)
        if search:
            search = "%%%s%%" % (search)
            sql += "and (name like %s or address like %s or phone like %s)"
            param.append(search)
            param.append(search)
            param.append(search)

        sql += "order by cid desc limit %s, %s"
        param.append(offset)
        param.append(limit)

        param = tuple(param)
        bRet, sRet = dataBase.query_data(sql, param)
        if not bRet:
            return False, sRet

        return True, sRet


    @staticmethod
    def query_node_count(status=None, search=None):
        dataBase = DataBase()
        sql = "select count(*) as cnt from tb_custom where 1=1 "
        param = []

        if status and status != 'all':
            sql += "and status = %s"
            param.append(status)
        if search:
            search = "%%%s%%" % (search)
            sql += "and (name like %s or address like %s or phone like %s)"
            param.append(search)
            param.append(search)
            param.append(search)

        param = tuple(param)
        bRet, sRet = dataBase.query_data(sql, param)
        if not bRet:
            return False, sRet
        if len(sRet) !=1:
            return True, 0

        return True, sRet[0]['cnt']


    @staticmethod
    def insert_node(nickName, Address, Phone, Ctype, Class, Status, Remark):

        dataBase = DataBase()
        sql = "insert into tb_custom(name, address, phone, ctype, class, status, remark, insert_tm) " \
              "values(%s, %s, %s, %s, %s, %s, %s, %s)"
        param = (nickName, Address, Phone, Ctype, Class, Status, Remark, get_cur_time())

        bRet, sRet = dataBase.insert_data(sql, param)
        return bRet, sRet


    @staticmethod
    def update_node(cId, nickName, Address, Phone, Ctype, Class, Status, Remark):
        dataBase = DataBase()
        sql = "update tb_custom set name = %s, address = %s, phone = %s, ctype = %s, class = %s, " \
              "status = %s, remark = %s where cid = %s"
        param = (nickName, Address, Phone, Ctype, Class, Status, Remark, cId)
        bRet, sRet = dataBase.update_data(sql, param)
        if not bRet:
            return False, sRet
        
        return True, sRet


    # just update the status when delete custom_info.
    @staticmethod
    def delete_node_by_cid(cId):
        dataBase = DataBase()
        sql = "update tb_custom set status = %s where cid = %s"
        param = ('delete', cId)
        bRet, sRet = dataBase.update_data(sql, param)
        if not bRet:
            return False, sRet
        
        return True, sRet


