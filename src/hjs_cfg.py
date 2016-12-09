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
    BaseConf.SQL_HOST       =   "222.xx.xx.xx"
    BaseConf.SQL_PORT       =   3306
    BaseConf.SQL_USER       =   "db_user"
    BaseConf.SQL_PASSWD     =   "db_passwd"
    BaseConf.SQL_DB         =   "hjs_cms_db"
    

else:
    BaseConf.IS_CTR_LOG     =   False
    BaseConf.LOG_LEVEL      =   2
    BaseConf.SQL_HOST       =   "127.0.0.1"
    BaseConf.SQL_PORT       =   3306
    BaseConf.SQL_USER       =   "db_user"
    BaseConf.SQL_PASSWD     =   "db_passwd"
    BaseConf.SQL_DB         =   "hjs_cms_db"



# with local cfg, so do not modify the file when test in the local env.
if os.path.exists(os.path.join(os.path.dirname(__file__), 'hjs_local_cfg.py')):
    from hjs_local_cfg import *



