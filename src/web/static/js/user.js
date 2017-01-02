/**
 * project: hjs_cms
 * author: s0nnet
 *
 */


/*用户列表*/
function get_user_list(){
    $.ajax({
        type: "GET",
        async: true,
        dataType: "json",
        url: "/api/user/list",
        error: function(){
            console.log("/api/user/list/error");
        },
        success: function(data){
            if(data.code == 101){
                alert(data.message);
            }
            if(data.code == 201){
                if(!data.result){
                    $("table tr").append("<p>当前用户列表为空，请先添加用户！</p>");
                    return;
                }
                $("table tr:not(:first)").empty();
                var dataLen = data.result.length;
                for(var i = 0; i < dataLen; i++){
                    var user_info = data.result[i];
                    var uid = user_info["uid"];
                    var nickname = user_info["nickname"];
                    var username = user_info["username"];
                    var password = user_info["password"];
                    var phone = user_info["phone"];
                    var email = user_info["email"];
                    var priv = user_info["priv"];
                    var lastlogin = user_info["lastlogin"];


                    if(priv == 3){
                        priv = "管理";
                    }else if(priv == 2){
                        priv = "运营";
                    }else if(priv == 1){
                        priv = "访客";
                    }else{
                        priv = "--";
                    }

                    $("table").append(
                        "<tr><td>"+ uid +"</td>"+
                        "<td>"+ nickname +"</td>"+
                        "<td>"+ username +"</td>"+
                        "<td>"+ password +"</td>"+
                        "<td>"+ phone +"</td>"+
                        "<td>"+ email +"</td>"+
                        "<td>"+ priv +"</td>"+
                        "<td>"+ lastlogin +"</td>"+
                        "<td><div class='popup01'><a href='#' onclick=edit_user('"+uid+"')>编辑</a></div> | <a href='#' onclick=del_user('"+ uid +"')>删除</a></td></tr>"
                    );
                }
            }
        }
    });
}

/*用户删除*/
function del_user(uid){
    if(!confirm("确认删除该用户？")){
        return;
    }
    $.ajax({
        type: "POST",
        async: true,
        dataType: "json",
        url: "/api/user/del",
        data: {"uid": uid},
        error: function() {
            console.log("/api/user/del/error");
        },
        success: function(data){
            if(data.code == 101){
                alert(data.message);
            }
            if(data.code == 201){
                get_user_list();
            }else{
                alert("删除用户失败[Error:" + data.message + "]");
            }
        }
    });
}

/*编辑用户*/
function edit_user(uid){
    var params = "uid=" + uid;
    popWin.showWin("500","430","用户编辑","user_edit.html", params);
}

/*编辑页面-获取用户信息*/
function get_user_info(){
    var uid = get_request_args("uid");

    $.ajax({
        type: "GET",
        async: true,
        dataType: "json",
        url: "/api/user/info",
        data: {"uid":uid},
        error: function(){
            console.log("/api/user/info/error");
        },
        success: function(data){
            if(data.code == 101){
                alert(data.message);
            }
            if(data.code == 201){
                if(!data.result){
                    return;
                }
                result = data.result;
                $("#form_uid").val(uid);
                $("#form_nickname").val(result.nickname);
                $("#form_username").val(result.username);
                $("#form_password").val(result.password);
                $("#form_phone").val(result.phone);
                $("#form_email").val(result.email);

                var priv = result.priv;
                if(priv == 3){
                    priv = "管理";
                }else if(priv == 2){
                    priv = "运营";
                }else if(priv == 1){
                    priv = "访客";
                }else{
                    priv = "??";
                }

                $(".select").children("dt").html(priv);
            }
        }
    });
}

/*提交修改后的数据*/
function update_user_info(){
    var uid = $("#form_uid").val();
    var nickname = $("#form_nickname").val();
    var username = $("#form_username").val();
    var password = $("#form_password").val();
    var phone = $("#form_phone").val();
    var email = $("#form_email").val();
    var priv = $(".select").children("dt").html();

    if(priv == "管理"){
        priv = 3;         
    }else if(priv == "运营"){
        priv = 2;
    }else if(priv == "访客"){
        priv = 1;
    }else{
        alert("用户等级输入错误!");
        return;
    }

    $.ajax({
        type: "POST",
        async: true,
        dataType: "json",
        url: "/api/user/update",
        data: {
            "uid":uid,
            "nickname": nickname,
            "username": username,
            "password": password,
            "phone": phone,
            "email": email,
            "priv": priv
        },
        error: function(){
            console.log("/api/user/update/error");
        },
        success: function(data){
            if(data.code == 101){
                alert(data.message);
            }
            if(data.code == 201){
                alert("更新成功,请关闭窗口并刷新！");
            }
        }
    });
}

/*添加用户*/
function add_user(){
    var nickname = $("#form_nickname").val();
    var username = $("#form_username").val();
    var password = $("#form_password").val();
    var phone = $("#form_phone").val();
    var email = $("#form_email").val();
    var priv = $(".select").children("dt").html();

    if(priv == "管理"){
        priv = 3;
    }else if(priv == "运营"){
        priv = 2;
    }else if(priv == "访客"){
        priv = 1;
    }else{
        alert("用户等级输入错误!");
        return;
    }
    $.ajax({
        type: "POST",
        async: true,
        dataType: "json",
        url: "/api/user/add",
        data: {
            "nickname": nickname,
            "username": username,
            "password": password,
            "phone": phone,
            "email": email,
            "priv": priv
        },
        error: function(){
            console.log("/api/user/add/error");
        },
        success: function(data){
            if(data.code == 101){
                alert(data.message);
            }
            if(data.code == 201){
                alert("添加成功,请关闭窗口！");
            }
        }
    });
}


/*获取URL传过来的参数*/
function get_request_args(argname){  
    var url = document.location.href;
    var arrStr = url.substring(url.indexOf("?")+1).split("&");

    for(var i = 0; i < arrStr.length; i++) {
        var loc = arrStr[i].indexOf(argname+"=");  
        if(loc != -1){
            return arrStr[i].replace(argname+"=","").replace("?","");
            break;
        }
    }
    return "";
}



