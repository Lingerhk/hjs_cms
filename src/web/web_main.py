# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: web.py 入口主函数


import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

import sys
sys.path.append("../base")
sys.path.append("../dao")
sys.path.append("../bean")
sys.path.append("..")
sys.path.append(".")

reload(sys)
sys.setdefaultencoding("utf-8")

os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'

import web
from viewset.view_base import *
from url import urls


# 权限校验
def user_check(handler):
    return handler()


# 启动
app = web.application(urls, globals())
app.add_processor(user_check)
Session.init(app)

if __name__ == "__main__":
    try:
        Log.info("ms_web work start!")
        app.run()
        Log.info("ms_web work end!")

    except Exception, e:
        Log.err("ms_web work err(%s)" % (str(e)))

else:
    application = app.wsgifunc()
