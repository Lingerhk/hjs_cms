# -*- coding: utf-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: tb_order_dao


'''
# 订单表
CREATE TABLE `tb_order` (
`oid` int(10) NOT NULL AUTO_INCREMENT,
`cid` int(10) NOT NULL,
`name` varchar(50) NOT NULL,
`otype` varchar(10) NOT NULL DEFAULT 'A',
`order_tm` datetime NOT NULL,
`start_tm` date NOT NULL,
`end_tm` date NOT NULL,
`amount` float NOT NULL,
`cash` float NOT NULL,
`status` enum('normal','stop') DEFAULT 'normal',
`remark` text NOT NULL,
`insert_tm` datetime NOT NULL,
PRIMARY KEY (`oid`),
KEY `cid` (`cid`),
CONSTRAINT `tb_order_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `tb_custom` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''



if __name__ == "__main__":
    import sys
    sys.path.append("..")
    sys.path.append("../base")

from hjs_cfg import *
from bs_util import *
from bs_database_pid import *


class HjsOrderDao:

    @staticmethod
    def insert_node():

        dataBase = DataBase()
        sql = ""
        param = ()

        bRet, sRet = dataBase.insert_data(sql, param)
        return bRet, sRet

    @staticmethod
    def query_node():
        dataBase = DataBase()
        sql = ""
        param = ()

        bRet, sRet = dataBase.query_data(sql, param)
        if not bRet:
            return False, sRet

        return True, sRet


    @staticmethod
    def query_node_list(offset, limit, status, search):
        dataBase = DataBase()
        sql = "select * from tb_order where 1=1 "
        param = []
        if status and status != 'all':
            sql += "and status = %s "
            param.append(status)
        if search:
            search = "%%%s%%" % (search)
            sql += "and (cid like %s or name like %s)"
            param.append(search)
            param.append(search)

        sql += "order by oid desc limit %s, %s"
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
        sql = "select count(*) as cnt from tb_order where 1=1 "
        param = []

        if status and status != 'all':
            sql += "and status = %s"
            param.append(status)
        if search:
            search = "%%%s%%" % (search)
            sql += "and (cid like %s or name like %s)"
            param.append(search)
            param.append(search)

        param = tuple(param)
        bRet, sRet = dataBase.query_data(sql, param)
        if not bRet:
            return False, sRet
        if len(sRet) !=1:
            return True, 0

        return True, sRet[0]['cnt']









