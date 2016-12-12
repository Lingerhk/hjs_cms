# -*- coding: utf-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: tb_order_dao


'''
# 暂取消订单表
CREATE TABLE `tb_ps_order` (
`pid` int(11) NOT NULL AUTO_INCREMENT,
`oid` int(10) NOT NULL,
`cid` int(10) NOT NULL,
`name` varchar(50) NOT NULL,
`pause_tm` date NOT NULL,
`remark` text NOT NULL,
`insert_tm` datetime NOT NULL,
PRIMARY KEY (`pid`),
KEY `oid` (`oid`),
KEY `cid` (`cid`),
CONSTRAINT `tb_ps_order_ibfk_1` FOREIGN KEY (`oid`) REFERENCES `tb_order` (`oid`),
CONSTRAINT `tb_ps_order_ibfk_2` FOREIGN KEY (`cid`) REFERENCES `tb_custom` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    sys.path.append("../base")

from hjs_cfg import *
from bs_util import *
from bs_database_pid import *


class HjsOrderPauseDao:

    @staticmethod
    def insert_node(oid, cid, name, pause_tm, remark):

        dataBase = DataBase()
        sql = "insert into tb_ps_order(oid, cid, name, pause_tm, remark, insert_tm) " \
              "values(%s, %s, %s, %s, %s, %s)"
        param = (oid, cid, name, pause_tm, remark, get_cur_time())

        bRet, sRet = dataBase.insert_data(sql, param)
        return bRet, sRet

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
    def delete_node_by_pid(pId):
        dataBase = DataBase()
        sql = "delete from tb_ps_order where pid = %s"
        param = (pId, )

        bRet, sRet = dataBase.delete_data(sql, param)
        if not bRet:
            return False, sRet
        
        return True, sRet


    @staticmethod
    def query_node_by_date(tg_date):
        dataBase = DataBase()
        sql = "select * from tb_ps_order where pause_tm = %s"
        param = (tg_date, )

        bRet, sRet = dataBase.query_data(sql, param)
        if not bRet:
            return False, sRet
    
        return True, sRet



if __name__ == "__main__":
    #print HjsOrderDao.query_node_by_status('stop')

    #print HjsOrderDao.query_node_by_date(3)
    print HjsOrderPauseDao.delete_node_by_pid(3)





