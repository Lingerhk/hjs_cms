# -*- coding: utf-8 -*- 

# author: s0nnet
# time: 2015-12-21
# desc: publish main


import sys
import os
import datetime
from template_deal import *
from secret import *


class PublishHjsCmsWeb:

    def __init__(self):
        self.app_name = "hjs_cms"
        self.conf_file = "hjs_cfg.py"
        self.localPath = "/tmp/publish_dir"
        
        self.code_rep = "git clone git@github.com:Lingerhk/hjs_cms.git"
        self.code_update = "git pull origin master"

        self.remote_path = "/home/project"
        self.remote_owner = "s0nnet"
        self.remote_enum = "online"


    def _cmd_exec(self, cmd):
        iRet = os.system(cmd)
        print cmd
        if iRet < 0: 
            os.write(sys.stderr.fileno(), "cmd: %s ERR\n" %(cmd))
            return False, "cmd: %s ERR\n" %(cmd)
        return True, ""

    def _ssh_cp(self, ip, fpath, dstpath):
        cmd = "ssh.exp %s scp %s %s@%s:%s" %(self.passwd, fpath, self.user, ip, dstpath)
        return self._cmd_exec(cmd)

    def _ssh_cmd(self, ip, cmd):
        cmd = "ssh.exp %s ssh %s@%s \"%s\"" %(self.passwd, self.user, ip, cmd)
        return self._cmd_exec(cmd)

    def _up_source(self):
        appPath = "%s_source/%s" %(self.localPath, self.app_name)
        if not os.path.exists(appPath):
            bRet,sRet = self._cmd_exec("%s %s" %(self.code_rep, appPath))
            if not bRet: return bRet, sRet
        else:
            bRet,sRet = self._cmd_exec("cd %s; %s; cd -" %(appPath, self.code_update))
            if not bRet: return bRet, sRet

        return True, ""


    def _get_source_code(self):
        bRet, sRet = self._up_source()
        if not bRet: return bRet, sRet

        appPath = "%s_source/%s" %(self.localPath, self.app_name)
        dstPath = "%s/%s" %(self.localPath, self.app_name)
        if os.path.exists(dstPath): os.system("rm -rf %s" %(dstPath))
        cmd = "cp %s %s -r" %(appPath, dstPath)
        os.system(cmd)

        cmd = "find %s -name .svn | xargs rm -rf" %(dstPath)
        os.system(cmd)
        cmd = "find %s -name .git | xargs rm -rf" %(dstPath)
        os.system(cmd)
        cmd = "find %s -name .idea | xargs rm -rf" %(dstPath)
        os.system(cmd)

        return True, ""


    def _build_dst(self):
        dstPath = "%s/%s" %(self.localPath, self.app_name)
        tarCmd = "cd %s;tar -zcvf %s.tar.gz %s" %(self.localPath, dstPath, self.app_name)
        os.system(tarCmd)
        return True, None


    def _replace_conf(self, ip):
        persionConf = "persion.conf"
        dstConfPath = "%s/%s/src/%s" %(self.localPath, self.app_name, self.conf_file)
        confTemplate = "%s/%s/src/%s.template" %(self.localPath, self.app_name, self.conf_file)
        os.rename(dstConfPath, confTemplate)
        bRet = conf_produce(persionConf, confTemplate, dstConfPath, ip)
        os.unlink(confTemplate)
        if not bRet: return False, "ERR"
        return True, ""


    def _package(self, ip):
        if not os.path.exists(self.localPath):
            bRet, sRet = self._cmd_exec("mkdir -p %s" %(self.localPath))
            if not bRet: return bRet, sRet
            if not os.path.exists(self.localPath):
                return False, "ERR"

        #get source
        bRet, sRet = self._get_source_code()
        if not bRet: return bRet, sRet

        # replace conf
        bRet, sRet = self._replace_conf(ip)
        if not bRet: return bRet, sRet

        # build dst
        bRet, sRet = self._build_dst()
        if not bRet: return bRet, sRet

        return True, ""


    def _load_conf(self, ip):
        confJson = get_srv_conf(self.remote_enum, ip)
        if not confJson:
            os.write(sys.stderr.fileno(), "ip: %s not conf\n" %(ip))
            return False, "ERR"

        if not confJson.has_key("user"):
            os.write(sys.stderr.fileno(), "confJson: %s not user\n" %(str(confJson)))
            return False, "ERR"
        self.user = confJson["user"]

        if not confJson.has_key("passwd"):
            os.write(sys.stderr.fileno(), "confJson: %s not passwd\n" %(str(confJson)))
            return False, "ERR"
        self.passwd = confJson["passwd"]

        return True, ""


    def _unzip_package(self, ip, version):
        # backup old code
        cmd = "cd %s; mv %s %s_%s" %(self.remote_path, self.app_name, self.app_name, version)
        bRet, sRet = self._ssh_cmd(ip, cmd)
        if not bRet: return False, sRet

        # unzip
        cmd = 'cd %s; tar -xvf %s_%s.tar.gz; chown %s.%s %s -R' %(self.remote_path, self.app_name, version, self.remote_owner, self.remote_owner, self.app_name)
        bRet, sRet = self._ssh_cmd(ip, cmd)
        if not bRet: return False, sRet

        return True, "" 

    def _send_package(self, ip):
        # send
        version = (datetime.datetime.now() - datetime.timedelta(0)).strftime("%Y%m%d")
        sourcePath = "%s/%s.tar.gz" %(self.localPath, self.app_name)
        dstPath = "%s/%s_%s.tar.gz" %(self.remote_path, self.app_name, version)
        bRet, sRet = self._ssh_cp(ip, sourcePath, dstPath)
        if not bRet: return bRet, sRet

        # prep srv env
        bRet, sRet = self._unzip_package(ip, version)
        if not bRet: return bRet, sRet

        return True, ""


    def _start_srv(self, ip):
        cmd = "supervisorctl restart %s" % (self.app_name)
        bRet, sRet = self._ssh_cmd(ip, cmd)
        if not bRet: return False, sRet
        return True, "" 


    def deploy(self, ip):
        # get srv conf
        bRet, sRet = self._load_conf(ip)
        if not bRet: return bRet, sRet

        # package
        bRet, sRet = self._package(ip)
        if not bRet: return bRet, sRet

        # send package
        bRet, sRet = self._send_package(ip)
        if not bRet: return bRet, sRet

        # start 
        bRet, sRet = self._start_srv(ip)
        if not bRet: return bRet, sRet

        return True, ""


    def _install_conf(self, ip):
        return True, ""


    def install(self, ip):
        # get srv conf
        bRet, sRet = self._load_conf(ip)
        if not bRet: return bRet, sRet

        # install conf
        bRet, sRet = self._install_conf(ip)
        if not bRet: return bRet, sRet

        bRet, sRet = self.deploy(ip)
        if not bRet: return bRet, sRet

        return True, ""


if __name__ == "__main__": 

    if len(sys.argv) < 3:
        os.write(sys.stderr.fileno(), "Useage: \n %s deploy $ip\n\n" %(sys.argv[0]))
        sys.exit()

    cmd = sys.argv[1]
    ip = sys.argv[2]

    hjsWeb = PublishHjsCmsWeb()
    if cmd == "deploy":
        print hjsWeb.deploy(ip)

    elif cmd == "install":
        print hjsWeb.install(ip)

    else:
        print "cmd:%s error!" %(cmd)
        sys.exit()


