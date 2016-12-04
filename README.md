##基于python开发的简易订单系统


这是受朋友之托帮忙开发的一个简易的订单系统。基本也没什么有创新可谈的，主要是它基于Python开发的高效特色框架。得益于实习期间跟随师父学了不要东西，该框架也是从他那学来的，在此十分感谢，算是领我这个菜鸟上道了^_^！整个开发差不多花了一周时间，从数据库，后台到前端，算是坑了一把，不过毕竟还是要经历才有收获。

### 1. 框架简述

该系统前端采用了RestAPI的设计，使用jQuery异步调取后端WEB接口的形式获取json的数据并渲染展示。
后端框架采用了base（基础类库层）、bean（后台逻辑层）、dao（数据持久层）、web（view展示层）的四层结构，代码结构清晰，高度模块化设计，使得开发起来高效、实用、可靠，并且便于扩展和维护。


下面是该系统的源码结构：
```
hjs_cms
├── bin/
├── conf/
├── src
│   ├── base/
│   ├── bean/
│   ├── dao/
│   ├── hjs_cfg.py
│   └── web
│       ├── sessions/
│       ├── static
│       │   ├── css/
│       │   ├── images/
│       │   └── js/
│       ├── templates/
│       ├── url.py
│       ├── viewset/
│       └── web_main.py
└── test/
```

### 2. 框架亮点

* 高度模块化、结构化设计
* 双返回值设计结构确保安全、可靠
* 采用fabric自动化部署
* 采用nose单元测试框架
* 实现了标准规范的log模块
* web.py 设计RestAPI
* 采用JQuery 调用WEB API渲染展示
* 采用nginx + gunicorn + web.py + supervisor 部署运行

### 3. 安装部署

xxxxxxxxxxxxx

