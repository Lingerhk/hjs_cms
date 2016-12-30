# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: 时间处理类封装


from bs_log import *
import datetime
import time


def get_cur_dtime():
    return int(time.time())


def get_cur_time(tmFormat=None):
    if tmFormat == None: tmFormat = "%Y-%m-%d %H:%M:%S"
    return (datetime.datetime.now()).strftime(tmFormat)


def yg_tm_str_int(strTm, format="%Y-%m-%d %H:%M:%S"):
    if type(strTm) == datetime.datetime:
        strTm = strTm.strftime(format)
    tmTuple = time.strptime(strTm, format)
    return time.mktime(tmTuple)


def yg_tm_int_str(tm, format="%Y-%m-%d %H:%M:%S"):
    # tmObj = time.localtime(tm)
    tmObj = time.localtime(tm)
    return time.strftime(format, tmObj)


def get_cur_day(days=0, format="%Y%m%d"):
    return (datetime.datetime.now() - datetime.timedelta(days)).strftime(format)


def get_cur_time_2(days=0, format="%Y-%m-%d %H:%M:%S"):
    return (datetime.datetime.now() - datetime.timedelta(days)).strftime(format)




if __name__ == "__main__":
    def test1():
        print get_cur_time_2(1, "%Y-%m-%d 00:00:00")


    print get_cur_day(0,format="%Y-%m-%d")
