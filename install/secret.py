# -*- coding: utf-8 -*- 

# author: s0nnet
# time: 2015-12-21
# desc: web server conf ssh.
#

import sys

srvSecretConfMap = {
    'online' : {
        'user' : 's0nnet',
        'passwd' : 'you_ssh_srv_passwd'
    }
}


def get_srv_conf(env, sip):

    if srvSecretConfMap.has_key(sip):
        return srvSecretConfMap[sip]

    if srvSecretConfMap.has_key(env):
        return srvSecretConfMap[env]

    return None

