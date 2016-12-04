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
    def insert_node(user_id, comp_id, task_name, task_type, task_pri_level, task_cycle, task_data, task_start_tm):

        dataBase = DataBase()
        sql = "insert into tb_task(user_id, comp_id, task_name, task_type, task_pri_level, task_cycle, " \
              "task_data, task_start_tm, insert_tm) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)" 
        param = (user_id, comp_id, task_name, task_type, task_pri_level, task_cycle, task_data, task_start_tm, get_cur_time())

        bRet, sRet = dataBase.insert_data(sql, param)
        return bRet, sRet
