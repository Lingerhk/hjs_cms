#!/bin/bash



#global value
CUR_VERSION="1.0"
LOG_FILE=deploy_hjs_cms.log
NGINXi_PATH=/usr/local/nginx/sbin/nginx
MYSQL_PATH=/usr/local/mysq



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
    
    log_to_file "[*] "

}



deploy_hjs_cms()
{
    install_basic_suite
    setup_iptables
    add_user
    install_web_suite
    install_nginx
    install_mysql
    install_python_venv
    config_web_suite
    install_service
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
