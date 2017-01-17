#!/bin/bash



#global value
CUR_VERSION="1.0"
LOG_FILE=deploy_hjs_cms.log
NGINXi_PATH=/usr/local/nginx/sbin/nginx
MYSQL_PATH=/usr/local/mysql



# 运行状态日志
log_to_file()
{
    echo "$1"
    echo "$1" >> ${LOG_FILE}
}

# 运行状态结果日志
log_result()
{
    if [ $2 -ne 0 ];then
        log_to_file "[-] $1 faild!"
    else
        log_to_file "[+] $1 successed!"
    fi
}

# 文件备份
backup_file()
{
    cp -f $1 $1.bak
}


# 安装系统基本依赖库
install_basic_suite()
{
    cur_module="install_basic_suite"
    log_to_file "[*] ${cur_module}"
    suite=(
        "gcc --version"
        "g++ --version"
        "pip --veriosn"
        "virtualenv --version"
        "wget --version"
    )
    length=${#suite[@]}

    yum install -y gcc gcc-c++
    yum install -y pip
    yum install -y mysql-devel
    yum install -y pyhton-pip
    yum install -y python-virtualenv
    yum install -y wget

    for((i=0; i<$length; i++))
    do
        ${suite[$i]} > /dev/null
        check_result ${cur_module} \
            "[-] install failed: ${suite[$i]}" \
            "[+] installed: ${suite[$i]}"
    done

    log_result ${cur_module} 0
}

# 安装Nginx
install_nginx()
{
    cur_module="install nginx"
    log_to_file "[*] ${cur_module}"

    ${NGINX_PATH} -v > /dev/null
    if [ $? -ne 0 ];then
        log_to_file "[!] no nginx installed! installing ..."
        yum install -y nginx
    else
        log_to_file "[!] nginx has realdy installed!"
    fi

    ${NGINX_PATH} > /dev/null
    if [ $? -ne 0];then
        nginx
    fi
    
    log_result ${cur_module} 0
}

# 安装MySQL
install_mysql()
{
    cur_module="install mysql"
    log_to_file "[*] ${cur_module}"
    
    mysql --version > /dev/null
    if [ $? -ne 0 ];then
        log_to_file "[!] no mysql intsalled! installing ..."
        yum install -y mysql-server mysql mysql-devel
    fi

    systemctl enable mysqld
    systemctl start mysqld.service
    if [ $? -ne 0 ];then
        log_to_file "[!] start mysqld service failed!"
    fi

    log_result ${cur_module} 0
}

# 安装python_web环境
install_web_suite()
{
    cur_module="install_web_suite"
    log_to_file "[*] ${cur_module}"

    suite=(
        "supervisord -v"
    )
    length=${#suite[@]}
    yum install -y supervisor
    pip install web.py

    for((i=0; i<$length; i++))
    do
        ${suite[$i]} > /dev/null
        check_result ${cur_module} \
            "[-] install faild: ${suite[$i]}" \
            "[+] installed: ${suite[$i]}"
    done

    log_result ${cur_module} 0
}

# 配置iptables
setup_iptables()
{
    cur_module="setup_iptables"
    log_to_file "[*] ${cur_module}"
    
    #install iptables
    yum install iptables-services
    check_result ${cur_module} \
        "[-] install iptabes failed" \
        "[+] installed iptables!"
    
    log_to_file "[*] start iptables"
    systemctl enable iptables;
    systemctl enable ip6tables;
    systemctl start iptables;
    systemctl start ip6tables;
    iptables -L
    iptables -F
    iptables -X

    log_to_file "[*] backup /etc/sysctl.conf"
    backup_file /etc/sysctl.conf
}

# 添加系统账户
add_web_user()
{
    cur_module="add_user"
    log_to_file "[*] ${cur_module}"

    # add mysql user
    userdel mysql
    groupadd mysql
    useradd -r -g mysql mysql
    check_result ${cur_module} \
        "[-] useradd mysql failed" \
        "[+] useradd mysql successed"

    #add web user
    userdel hjs_cms
    groupadd hjs_cms
    useradd -g hjs_cms hjs_cms -p hjs@!cms
    check_result ${cur_module} \
        "[-] useradd hjs_cms failed" \
        "[+] useradd hjs_cms successed"

    log_result ${cur_module} 0
}

# 配置web环境
config_web_suite()
{
    cur_module="config_web_suite"
    log_to_file "[*] ${cur_module}"
    
    #deploy source code
    thisPath=`pwd`
    backup_file /home/project/hjs_cms/src
    cp $thisPath/../src /home/project/hjs_cms -R

    chown -R s0nnet:s0nnet /home/project/hjs_cms

    log_result ${cur_module} 0
}

# 启动web服务
start_services()
{
    cur_module="start_services"
    log_to_file "[*] ${cur_module}"

    service_list=(
        "mysql"
        "nginx"
        "supervisor"
    )
    length=${#service_list[@]}

    for ((i=0; i<$length; i++))
    do
        service=$(service_list[$i])
        service $service start
    done

    log_result ${cur_module} 0
}

# 重启web服务
restart_services()
{
    cur_module="restart_services"
    log_to_file "[*] ${cur_module}"

    service_list=(
        "mysql"
        "nginx"
        "supervisor"
    )
    length=${#service_list[@]}

    for ((i=0; i<$length; i++))
    do
        service=${service_list[$i]}
        service $service stop
        service $service start
    done

    log_result ${cur_module} 0
}

install_hjs_cms()
{
    install_basic_suite
    install_nginx
    install_mysql
    install_web_suite
    setup_iptables
    add_web_user
    config_web_suite
    start_services
}

case "$1" in
    deploy)
        deploy_hjs_cms
    ;;
    install)
        install_hjs_cms
    ;;
    service)
        restart_service
    ;;
    *)
        echo "args error: $1"
        exit -1
    ;;
esac
