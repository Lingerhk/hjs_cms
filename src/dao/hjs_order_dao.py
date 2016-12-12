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
    def insert_node(cId, name, otype, order_tm, start_tm, end_tm, amount, cash, remark):

        dataBase = DataBase()
        sql = "insert into tb_order(cid, name, otype, order_tm, start_tm, end_tm, amount, cash, remark, insert_tm) " \
              "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        param = (cId, name, otype, order_tm, start_tm, end_tm, amount, cash, remark, get_cur_time())

        bRet, sRet = dataBase.insert_data(sql, param)
        return bRet, sRet


    @staticmethod
    def update_node_status(oId, status):
        dataBase = DataBase()
        sql = "update tb_order set status = %s where oid = %s"
        param = (status, oId)

        bRet, sRet = dataBase.update_data(sql, param)
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

    @staticmethod
    def query_node_by_oid(oId):
        dataBase = DataBase()
        sql = "select * from tb_order where oid = %s"
        param = (oId, )

        bRet, sRet = dataBase.query_data(sql, param)
        if (not bRet) or (len(sRet) != 1):
            return False, sRet
        
        return True, sRet[0]


    @staticmethod
    def query_node_by_status(status):
        dataBase = DataBase()
        sql = "select count(*) as cnt from tb_order where 1=1 "
        param = []

        if status == 'all':
            pass
        else:
            sql += 'and status = %s'
            param.append(status)
        
        param = tuple(param)
        bRet, sRet = dataBase.query_data(sql, param)
        if not bRet:
            return False, sRet
        if len(sRet) != 1:
            return True, 0
        
        return True, sRet[0]['cnt']

        
    @staticmethod
    def query_node_by_days(days):
        dataBase = DataBase()
        sql = "select oid, cid, name, date_format(end_tm, '%%Y-%%m-%%d') as end_time from tb_order " \
              "where end_tm >= curdate() and end_tm < curdate() + %s"
        param = (days, )

        bRet, sRet = dataBase.query_data(sql, param)
        if not bRet:
            return False, sRet
        
        return True, sRet

    
    @staticmethod
    def query_node_by_date(status, tg_date):
        dataBase = DataBase()
        sql = "select * from tb_order where status = %s and start_tm <= %s and %s <= end_tm"
        param = (status, tg_date, tg_date)

        bRet, sRet = dataBase.query_data(sql, param)
        if not bRet:
            return False, sRet

        return True, sRet


if __name__ == "__main__":
    #print HjsOrderDao.query_node_by_status('stop')

    print HjsOrderDao.query_node_by_date('normal', '2016-12-11')





