# coding:utf-8

# author: s0nnet
# time: 2016-11-28
# desc: urls

from viewset.view_login import *
from viewset.view_index import *
from viewset.view_custom import *
from viewset.view_order import *
from viewset.view_user import *

urls = (
    "/", ViewIndex,
    "/index", ViewIndex,
    "/index.html", ViewIndex,
    "/custom_list.html", ViewCustomList,
    "/custom_search.html", ViewCustomSearch,
    "/custom_add.html", ViewCustomAdd,
    "/order_all.html", ViewOrderAll,
    "/order_today.html", ViewOrderToday,
    "/order_cancel.html", ViewOrderCancel,
    "/user_list.html", ViewUserList,
    "/user_add.html", ViewUserAdd,
    "/login", ViewLogin,
    "/logout", ViewLogout,
    "/api/data/count", ViewApiDataCount,
    "/api/custom/list", ViewApiCustomList,
    "/api/custom/add", ViewApiCustomAdd,
    "/api/custom/update", ViewApiCustomUpdate,
    "/api/custom/del", ViewApiCustomDel,
    "/api/order/list", ViewApiOrderList,
    "/api/order/today", ViewApiOrderToday,
    "/api/order/add", ViewApiOrderAdd,
    "/api/order/del", ViewApiOrderDel,
    "/api/user/list", ViewApiUserList,
    "/api/user/add", ViewApiUserAdd,
    "/api/user/update", ViewApiUserUpdate,
    "/api/user/del", ViewApiUserDel,
)
