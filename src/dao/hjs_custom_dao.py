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
    def insert_node(user_id, comp_id, task_name, task_type, task_pri_level, task_cycle, task_data, task_start_tm):

        dataBase = DataBase()
        sql = "insert into tb_task(user_id, comp_id, task_name, task_type, task_pri_level, task_cycle, " \
              "task_data, task_start_tm, insert_tm) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)" 
        param = (user_id, comp_id, task_name, task_type, task_pri_level, task_cycle, task_data, task_start_tm, get_cur_time())

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
