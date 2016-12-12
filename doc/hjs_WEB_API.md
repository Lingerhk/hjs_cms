### hjs系统WEB接口设计文档

[TOC]



#### 通用说明

1. 接口响应均采用json格式，GET以URL带请求参数，POST 请求 BODY里带json格式的请求参数

2. 协议编码采用utf-8格式

3. 响应数据格式:

   ```json
   # 正常响应
   {
     "message": "SUCCESS",
     "code": 201,
     "result": 
   }

   # 出错响应
   {
     "message": "error_msg",
     "code": 101
   }
   ```


#### 接口说明

以下描述接口详细内容。

##### 用户管理

* 用户列表-页面
  - `GET /user_list.html`

  * 请求参数： 无
    
  * 响应结果(html)： user_list.html



* 添加用户-页面
  - `GET /user_add.html`

  * 请求参数： 无
    
  * 响应结果(html)： user_add.html



* 获取用户列表

  - `GET /api/user/list`

  * 请求参数：
    ```json
    # 类型  |  默认值 		| 是否必填
    # str  | None(没有默认值填None)  | yes
    {
      "page":1, # int | 1  | no
      "length": 20, # int | 20 | no
      "status": "normal", # str | None | no 
      "search":"123" # str | None | no
    }
    ```

  * 响应结果：
    ```json
    {
      "result": [{
    	        "uid": 103,
                "username": "zhang123",
    	        "nickname": "zhangxiaoci",
                "password": "123@qwe",
                "phone": "188292726354", 
                "email": "qwe@qw.com",
                "privilege": 2, # 1=>guest, 2=>user, 3=>admin
                "lastlogin": "2015-21-23 12:23:21"
    	        },
                ....
          ]
    }
    ```


* 添加用户信息

  - `POST /api/user/add`

  * 请求参数：
    ```json
    # 类型  |  默认值 		 | 是否必填
    # str  | None(没有默认值填None)  | yes

    {
      "nickname": "wange", # str | None | yes
      "username": "wange3", # str | None | yes 
      "password": "wg@345", # str | None | yes
      "phone": "12322120088", # str | None | yes
      "email": "wange@sina.com", # str | None | yes
      "priv": 2 # int | None | yes (# 1=>guest, 2=>user, 3=>admin)
    }
    ```

  * 响应结果： 
    ```json
    {
      "result": {
        "nickname": "wanger",
        "username": "wang",
        "password": "wang@123",
        "phone": "12300006666",
        "email": "wang@sina.com",
        "privilege": 2,
        "lastlogin": "2015-12-23 23:21:12"
    	}
    }
    ```


* 修改用户信息

  * `POST /api/user/update`

  * 请求参数：
    ```json
    # 类型  |  默认值 		 | 是否必填
    # str  | None(没有默认值填None)  | yes

    {
      "uid": 102, # int | None  | yes
      "nickname": "wange", # str | None | yes
      "username": "wange3", # str | None | yes 
      "password": "wg@345", # str | None | yes
      "phone": "12322120088", # str | None | yes
      "email": "wange@sina.com", # str | None | yes
      "priv": 2 # int | None | yes (# 1=>guest, 2=>user, 3=>admin)
    }
    ```

  * 响应结果：
    ```json
    # 仅列出result项。
    {
      "result": "Success"
    }
    ```


* 删除用户信息

  * `POST /api/user/del`

  * 请求参数：

    ```json
    {
      "uid": 5 # int | None | yes
    }
    ```

  * 响应结果：

    ```json
    {
      "result": "Success"
    }
    ```


##### 客户管理

* 客户列表-页面
  - `GET /custom_list.html`

  * 请求参数： 无
    
  * 响应结果(html)： custom_list.html



* 客户信息查询-页面
  - `GET /custom_search.html`

  * 请求参数： 无
    
  * 响应结果(html)： custom_search.html



* 添加客户-页面
  - `GET /custom_add.html`

  * 请求参数： 无
    
  * 响应结果(html)： custom_add.html



* 获取客户列表

  - `GET /api/custom/list`

  * 请求参数：
    ```json
    # 类型  |  默认值  |  是否必填
    # str  | None(没有默认值填None)  | yes
    {
      "page": 1, # int | 1  | no
      "length": 20, # int | 20 | no
      "status": "normal", # str | None | no 
      "search": "123" # str | None | no
    }
    ```
    
  * 响应结果：
    ```json
    {
        "result": [{
            "cid": 1004,
            "name": "zhang123",
            "address": "city_a xxx",
            "phone": "13288885555",
            "ctype": "A", 
            "class_priv": "O",
            "status": "normal",
            "remark": "xxxxxxx",
            "insert_tm": "2015-21-23 12:23:21"
            },
            ....
        ]
    }
    ```


* 添加客户

  - `POST /api/custom/add`

  * 请求参数：
    ```json
    # 类型  |  默认值  |  是否必填
    # str  | None(没有默认值填None)  | yes
    {
      "nickname": "wang",
      "address": "xxxxx",
      "phone": "1234566423232",
      "ctype": "N",
      "class": "A",
      "remark":"xxxxx"
    }
    ```
    
  * 响应结果：

    ```json
    {
      "result": "Success"
    }
    ```


* 修改客户

  - `POST /api/custom/update`

  * 请求参数：
    ```json
    # 类型  |  默认值  |  是否必填
    # str  | None(没有默认值填None)  | yes
    {
      "cid": 1002,
      "nickname": "wang2",
      "address": "xxxxyyyyzzzz",
      "phone": "12345678888",
      "ctype": "N",
      "class": "A",
      "status": "cancel",
      "remark":"xxxxx"
    }
    ```
    
  * 响应结果：

    ```json
    {
      "result": "Success"
    }
    ```


* 删除客户

  - `POST /api/custom/del`

  * 请求参数：
    ```json
    # 类型  |  默认值  |  是否必填
    # str  | None(没有默认值填None)  | yes
    {
      "cid": 1002
    }
    ```
    
  * 响应结果：

    ```json
    {
      "result": "Success"
    }
    ```


##### 订单管理

* 订单列表-页面
  - `GET /order_all.html`

  * 请求参数： 无
    
  * 响应结果(html)： order_all.html


* 添加订单-页面
  - `GET /order_add.html`

  * 请求参数： 无
    
  * 响应结果(html)： order_add.html


* 今日订单列表-页面
  - `GET /order_today.html`

  * 请求参数： 无
    
  * 响应结果(html)： order_today.html


* 查找订单-页面
  - `GET /order_search.html`

  * 请求参数： 无
    
  * 响应结果(html)： order_search.html


* 暂取消订单列表-页面
  - `GET /order_pause.html`

  * 请求参数： 无
    
  * 响应结果(html)： order_pause.html


* 添加暂取消订单-页面
  - `GET /order_pause_add.html`

  * 请求参数： 无
    
  * 响应结果(html)： order_pause_add.html


* 获取订单列表

  - `GET /api/order/list`

  * 请求参数：
    ```json
    # 类型  |  默认值  |  是否必填
    # str  | None(没有默认值填None)  | yes
    {
      "page": 1, # int | 1  | no
      "length": 20, # int | 20 | no
      "status": "normal", # str | None | no 
      "search": "123" # str | None | no
    }
    ```
    
  * 响应结果：
    ```json
    {
        "result": [{
            "oid": 2001,
            "cid": 1004,
            "name": "zhang123",
            "order_tm": "2015-12-21 23:12:11",
            "start_tm": "2016-02-12",
            "end_tm": "2016-04-12", 
            "amount": 600,
            "cash": 550,
            "remark": "xxxxxxx",
            "insert_tm": "2015-21-23 12:23:21"
            },
            ....
        ]
    }
    ```


* 获取当日订单列表

  - `GET /api/order/today`

  * 请求参数： 无
    
  * 响应结果：
    ```json
    {
        "result": [{
            "oid": 2001,
            "cid": 1004,
            "name": "zhang123",
            "address": "zzzzzxxxx",
            "phone": "13255559999",
            "remark": "xxxxxxx"
            },
            ....
        ]
    }
    ```


* 添加订单

  - `POST /api/order/add`

  * 请求参数：
    ```json
    # 类型  |  默认值  |  是否必填
    # str  | None(没有默认值填None)  | yes
    {
      "cid": 1002,
      "otype": "A", 
      "order_tm": "2016-03-12 12:23:11", # 非必须
      "start_tm": "2016-04-23",
      "end_tm": "2016-05-23",
      "amount": 300,
      "cash": 280,
      "remark":"need 20"
    }
    ```
    
  * 响应结果：

    ```json
    {
      "result": "Success"
    }
    ```


* 删除订单

  - `POST /api/order/del`

  * 请求参数：
    ```json	
    # 类型  |  默认值  |  是否必填
    # str  | None(没有默认值填None)  | yes
    {
      "oid": 2001
    }
    ```
    
  * 响应结果：

    ```json
    {
      "result": "Success"
    }
    ```


* 获取暂取消订单列表

  - `GET /api/order/pause_list`

  * 请求参数： 无
    
  * 响应结果：
    ```json
    {
        "result": [{
            "pid": 2001,
            "oid": 1003,
            "cid": 1004,
            "name": "zhang123",
            "pause_tm": "zzzzzxxxx",
            "remark": "13255559999"
            },
            ....
        ]
    }
    ```



* 添加暂取消订单

  - `GET /api/order/pause_add`

  * 请求参数：
    ```json	
    # 类型  |  默认值  |  是否必填
    # str  | None(没有默认值填None)  | yes
    {
      "oid": 2001,
      "pause_tm": "2016-03-23",
      "remark": "cxxxsssssss"
    }
    ```
    
  * 响应结果：

    ```json
    {
      "result": "Success"
    }
    ```


* 删除暂取消订单

  - `GET /api/order/pause_del`

  * 请求参数：
    ```json	
    # 类型  |  默认值  |  是否必填
    # str  | None(没有默认值填None)  | yes
    {
      "pid": 2001
    }
    ```
    
  * 响应结果：

    ```json
    {
      "result": "Success"
    }
    ```



























  ​
