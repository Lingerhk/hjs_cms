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

* 获取用户列表

  - `GET /api/user/list`

  - 请求参数：
    ```json
    # 类型  |  默认值 		| 是否必填
    # str  | None(没有默认值填None)  | yes
    {
      "page":1, # int | 1  | no
      "length": 20, # int | 20 | no
      "status": "normal", # str | None | no 
      "search":"123", # str | None | no
    }
    ```

  - 响应结果：
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

  - 响应结果： 
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

  ​
