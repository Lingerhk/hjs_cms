#### 自动化部署脚本


##### 脚本说明：

* nginx/ nginx配置
* supervisor/ supervisor配置
* tools/ ssh.exp执ssh的脚本
* persion.conf 远程服务器的业务配置环境
* publish_hjs_cms.py 自动化部署脚本主执行脚本
* secret.py 远程服务器的ssh配置信息
* template_deal.py 对配置(persion.conf)的解析



##### 自动化部署
```
python publish_hjs_cms.py deploy $srv_ip
```

注意：
1. 在publish_hjs_cms.py脚本最后有重启supervisor的命令，这需要root权限才可以重启！
2. 日志目录配置在根目录下logs下，重新部署后可能需要创建此目录

