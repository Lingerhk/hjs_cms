# -*- coding: UTF-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: custom view


from view_base import *
from hjs_user import *
from hjs_custom import *


class ViewCustomList(ViewBase):

    def GET(self):
        if not self.check_login():
            Log.err("user not login")
            return web.seeother("/login")
        return render.custom_list()


class ViewCustomSearch(ViewBase):
    def GET(self):
        if not self.check_login():
            Log.err("user not login")
            return web.seeother("/login")
        return render.custom_search()


class ViewCustomAdd(ViewBase):
    def GET(self):
        if not self.check_login():
            Log.err("user not login")
            return web.seeother("/login")
        return render.custom_add()


class ViewCustomEdit(ViewBase):
    def GET(self):
        if not self.check_login():
            Log.err("user not login!")
            return web.seeother("/login")
        return render.custom_edit()


class ViewApiCustomList(ViewBase):
    def __init__(self):
        self._rDict = {
            "page": {'n': "page", 't': int, 'v': 1},
            "length": {'n': "length", 't': int, 'v': 20},
            "status": {'n': "status", 't': str, 'v': ''},
            "search": {'n': "search", 't': str, 'v': ''}
        }
        
    def _check_param(self):
        bRet, sRet = super(ViewApiCustomList, self)._check_param()
        if not bRet:
            return bRet, sRet
        return True, None

    def _deal_custom_list(self):
        return HjsCustom.custom_list(self.page, self.length, self.status, self.search)

    # get custom list
    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            return web.seeother("/login")
        
        bRet, customList = self.process(self._deal_custom_list)
        if not bRet:
            Log.err("deal_custom_list: %s" % (str(customList)))
            return self.make_error(customList)

        return self.make_response(customList)

    # get custom list by search
    def POST(self):
        bRet, sRet = self.check_login()
        if not bRet:
            return web.seeother("/login")
        bRet, customList = self.process(self._deal_custom_list)
        if not bRet:
            Log.err("deal_custom_list: %s" % (str(customList)))
            return self.make_error(customList)

        return self.make_response(customList)


class ViewApiCustomAdd(ViewBase):
    def __init__(self):
        self._rDict = {
            "nickname": {'n': 'nickName', 't': str, 'v': None},
            "address": {'n': 'Address', 't': str, 'v': None},
            "phone": {'n': 'Phone', 't': str, 'v': None},
            "ctype": {'n': 'Ctype', 't': str, 'v': None},
            "class": {'n': 'Class', 't': str, 'v': None},
            "remark": {'n': 'Remark', 't': str, 'v': None}
        }

    def _check_param(self):
        bRet, sRet = super(ViewApiCustomAdd, self)._check_param()
        if not bRet:
            return bRet, sRet
        
        return True, None

    def _deal_custom_add(self):
        bRet, is_admin = HjsUser.is_admin(self.get_user_name())
        if not bRet:
            return False, sRet
        if not is_admin:
            return False, 'No permission do custom add'
        
        return HjsCustom.custom_add(self.nickName, self.Address, self.Phone, self.Ctype, self.Class, self.Remark)

    def POST(self):
        if not self.check_login():
            return self.make_error("user not login")
        
        bRet, sRet = self.process(self._deal_custom_add)
        if not bRet:
            Log.err("add custom error: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(ViewBase.RetMsg.MSG_SUCCESS)


class ViewApiCustomInfo(ViewBase):
    def __init__(self):
        self._rDict = {
            "cid": {'n': 'cId', 't': int, 'v': None}
        }
                
    def _check_param(self):
        bRet, sRet = super(ViewApiCustomInfo, self)._check_param()
        if not bRet:
            return bRet, sRet
        
        return True, None

    def _deal_custom_info(self):
        bRet, is_admin = HjsUser.is_admin(self.get_user_name())
        if not bRet:
            return False, sRet
        if not is_admin:
            return False, 'No permission do custom info'
                                                                                                                        
        return HjsCustom.custom_info(self.cId)

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")
        
        bRet, sRet = self.process(self._deal_custom_info)
        if not bRet:
            Log.err("deal_custom_info: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)


class ViewApiCustomUpdate(ViewBase):
    def __init__(self):
        self._rDict = {
            "cid": {'n': 'cId', 't': int, 'v': None},
            "nickname": {'n': 'nickName', 't': str, 'v': None},
            "address": {'n': 'Address', 't': str, 'v': None},
            "phone": {'n': 'Phone', 't': str, 'v': None},
            "ctype": {'n': 'Ctype', 't': str, 'v': None},
            "class": {'n': 'Class', 't': str, 'v': None},
            "status": {'n': 'Status', 't': str, 'v': None},
            "remark": {'n': 'Remark', 't': str, 'v': None}
        }

    def _check_param(self):
        bRet, sRet = super(ViewApiCustomUpdate, self)._check_param()
        if not bRet:
            return bRet, sRet
        
        return True, None

    def _deal_custom_update(self):
        bRet, is_admin = HjsUser.is_admin(self.get_user_name())
        if not bRet:
            return False, sRet
        if not is_admin:
            return False, 'No permission do user update'
        
        return HjsCustom.custom_update(self.cId, self.nickName, self.Address, self.Phone, self.Ctype, self.Class, self.Status, self.Remark)        

    def POST(self):
        if not self.check_login():
            return self.make_error("user not login")

        bRet, sRet = self.process(self._deal_custom_update)
        if not bRet:
            Log.err("update custom error: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(ViewBase.RetMsg.MSG_SUCCESS)


class ViewApiCustomDel(ViewBase):
    def __init__(self):
        self._rDict = {
            "cid": {'n': 'cId', 't': int, 'v': None}
        }
    
    def _check_param(self):
        bRet, sRet = super(ViewApiCustomDel, self)._check_param()
        if not bRet:
            return bRet, sRet
        return True, None

    def _deal_custom_del(self):
        bRet, is_admin = HjsUser.is_admin(self.get_user_name())
        if not bRet:
            return False, sRet
        if not is_admin:
            return False, 'No permission do custom del'
        
        return HjsCustom.custom_del(self.cId)

    def POST(self):
        if not self.check_login():
            return self.make_error("user not login")
        
        bRet, sRet = self.process(self._deal_custom_del)
        if not bRet:
            Log.err("deal_custom_del: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(ViewBase.RetMsg.MSG_SUCCESS)





