#-*- coding=utf-8 -*-

# author: s0nnet
# time: 2015-12-21
# desc: 


import os
import sys
import traceback
from subprocess import *

def exec_cmd(cmd, bShell = True):
    content = ""
    try:
        p = Popen(cmd, bufsize = 4096, stdout = PIPE, shell = bShell)
                           
        while True:
            cont = p.stdout.read()
            if cont == "": break
            content += cont
            retState = p.wait()
                                                                       
        return retState, content
    except Exception, e:
        sys.stderr.write("(%s)" %(traceback.format_exc()))
        return 255, "cmd(%s) err: %s" %(str(cmd), str(e)) 

def _get_local_ip():
    cmd = "/sbin/ifconfig | grep 'inet addr:' | awk '{print $2}'"
    bRet, sRet = exec_cmd(cmd)
    if bRet != 0:  return None

    lineList = sRet.split("\n")
    for line in lineList:
        ip = line[5 : ]
        if ip.startswith("10.") or ip.startswith("172."): 
            return ip

    return None


def _split_line(line):
    tmpList = []
    strLen = len(line)
    s = 0
    while s < strLen:
        while s < strLen:
            if line[s] == '#':  return True, tmpList
            if line[s] != ' ' and line[s] != '\t': break
            s += 1
        if s == strLen:  return True, tmpList

        e = s + 1
        while e  < strLen:
            if line[e] == '#':
                tmpList.append(line[s : e])
                return True, tmpList
            if line[e] == ' ' or line[e] == '\t': break 
            e += 1

        tmpList.append(line[s : e])
        if e >= strLen: break 

        s = e + 1

    return True, tmpList


val_sep = "    "
def _load_person_conf(confPath, localIp):
    keyDict = {}
    try:
        lines = open(confPath, "r").readlines()
        for line in lines:
            if len(line) > 0 and line[len(line) - 1] == '\n':  line = line[0 : len(line) - 1]
            if len(line) > 0 and line[len(line) - 1] == '\r':  line = line[0 : len(line) - 1]
            bRet, tmpList = _split_line(line)
            if len(tmpList) < 3: continue
            ip = tmpList[0]
            key = tmpList[1]
            val = tmpList[2]
            i = 3
            while i < len(tmpList):
                val += val_sep + tmpList[i]
                i += 1

            if ip == localIp:
                keyDict[key] = val

        return True, keyDict
    except Exception, e:
        sys.stderr.write("_load_person_conf(%s) ERR(%s)\n" %(localIp, str(e)))
        return False, None


def _replace_conf(confTemple, conf, keyDict):
    try:
        
        lines = open(confTemple, "r").readlines()
        fp = open(conf, "w")

        for line in lines:
            if len(line) > 0 and line[len(line) - 1] == '\n':  line = line[0 : len(line) - 1]
            if len(line) > 0 and line[len(line) - 1] == '\r':  line = line[0 : len(line) - 1]
            bRet, tmpList = _split_line(line)

            if len(tmpList) > 1:
                key = tmpList[0]
                if keyDict.has_key(key):

                    sepIdx = line.find(key)
                    sepval = line[0 : sepIdx]
                    line = "%s%s%s%s" %(sepval, key, val_sep, keyDict[key])

            fp.write("%s\n" %(line))

        fp.close()
        return True

    except Exception, e:
        sys.stderr.write("_replace_conf(%s, %s) ERR(%s)\n" %(confTemple, conf, traceback.format_exc()))
        return False


def conf_produce(persionConf, confTemplate, dstConfPath, ip):

    bRet, keyDict = _load_person_conf(persionConf, ip)
    if not bRet: return bRet

    print keyDict

    return _replace_conf(confTemplate, dstConfPath, keyDict)

                


if __name__ == "__main__":

    def test_1():

        persionConf = "persion.conf"
        confTemplate = "/home/s0nnet/hjs_cms/src/hjs_cfg.py"
        dstConfPath = "hjs_cfg.py"
        ip = "222.24.xx.xx"

        print conf_produce(persionConf, confTemplate, dstConfPath, ip)

    test_1()

