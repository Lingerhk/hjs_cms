/**
 * project: hjs_cms
 * author: s0nnet
 *
 */


$(document).ready(function() {
    list_user();
});



/*用户列表*/
function list_user(){
    $.ajax({
        type: "GET",
        async: true,
        dataType: "json",
        url: "/api/user/list",
        error: function(){
            console.log("/api/user/list/error");
        },
        success: function(data){
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
                    var priv = user_info["priv"];
                    var lastlogin = user_info["lastlogin"];


                    if(priv == 3){
                        priv = "管理员";
                    }else if(priv == 2){
                        priv = "运营者";
                    }else if(priv == 1){
                        priv = "访客者";
                    }else{
                        priv = "--";
                    }

                    $("table").append(
                        "<tr><td>"+ uid +"</td>"+
                        "<td>"+ username +"</td>"+
                        "<td>"+ nickname +"</td>"+
                        "<td>"+ password +"</td>"+
                        "<td>"+ phone +"</td>"+
                        "<td>"+ priv +"</td>"+
                        "<td>"+ lastlogin +"</td>"+
                        "<td><div class='popup01'><a href='#' onclick=edit_user('"+uid+"')>编辑</a></div> | <a href='#' onclick=del_user('"+ uid +"')>删除</a></td></tr>"
                    );
                }
            }
        }
    });
}


/*编辑用户*/
function edit_user(uid){
    var params = "uid=" + uid;
    popWin.showWin("500","430","用户编辑","user_edit.html", params);
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
            if(data.code == 201){
                list_user();
                $("")

            }else{
                alert("删除用户失败[Error:" + data.message + "]");
            }
        }
    });
}
