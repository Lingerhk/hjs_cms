# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: 简易订单系统


from bs_base_cfg import *

class EnvEnum:
    T_DEV       =   "dev"
    T_ONLINE    =   "online"
    
CUR_ENV         =   EnvEnum.T_DEV

if CUR_ENV ==  EnvEnum.T_DEV:
    
    BaseConf.IS_CTR_LOG     =   True
    BaseConf.LOG_LEVEL      =   1
    BaseConf.SQL_HOST       =   "222.24.62.48"
    BaseConf.SQL_PORT       =   3306
    BaseConf.SQL_USER       =   "hjs_user"
    BaseConf.SQL_PASSWD     =   "hjs@cms"
    BaseConf.SQL_DB         =   "hjs_cms_db"
    

else:
    BaseConf.IS_CTR_LOG     =   False
    BaseConf.LOG_LEVEL      =   2
    BaseConf.SQL_HOST       =   "127.0.0.1"
    BaseConf.SQL_PORT       =   3306
    BaseConf.SQL_USER       =   "root"
    BaseConf.SQL_PASSWD     =   "123456"
    BaseConf.SQL_DB         =   "hjs_cms_db"

