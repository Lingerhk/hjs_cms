##基于python开发的简易订单系统

### 这是受朋友之托帮忙开发的一个简易的订单系统。基本也没什么有创新可谈的，主要在基于Python开发的架构。得益于实习期间学了不要东西，所以就花了一周时间开发了这么个简单的系统。

### 架构简述

下面是该系统的源码结构：
```
hjs_cms
├── bin/
├── conf/
├── src
│   ├── base 
│   │   ├── bs_base_cfg.py
│   │   ├── bs_database_pid.py
│   │   ├── bs_email.py
│   │   ├── bs_log.py
│   │   ├── bs_process.py
│   │   ├── bs_syshead.py
│   │   ├── bs_time.py
│   │   └── bs_util.py
│   ├── bean
│   │   ├── hjs_custom.py
│   │   ├── hjs_order.py
│   │   └── hjs_user.py
│   ├── dao
│   │   ├── hjs_custom_dao.py
│   │   ├── hjs_order_dao.py
│   │   └── hjs_user_dao.py
│   ├── hjs_cfg.py
│   └── web
│       ├── sessions/
│       ├── static
│       │   ├── css/
│       │   ├── images/
│       │   └── js/
│       ├── templates/
│       ├── url.py
│       ├── viewset
│       │   ├── __init__.py
│       │   ├── view_base.py
│       │   ├── view_custom.py
│       │   ├── view_index.py
│       │   ├── view_login.py
│       │   ├── view_order.py
│       │   ├── view_user.py
│       │   └── web_util.py
│       └── web_main.py
└── test/
```
