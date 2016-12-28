/**
 * Created by hang on 16-12-13.
 */
/*用户列表*/

/*
$(document).ready(function (){
    $.get("/api/user/list", function(data) {
        $("table tr:last").html("");
        $.each(data.result, function(i, item) {
            $("table").append(
                "<tr><td>"+ item.uid +"</td>"+
                "<td>"+ item.username +"</td>"+
                "<td>"+ item.nickname +"</td>"+
                "<td>"+ item.password +"</td>"+
                "<td>"+ item.email +"</td>"+
                "<td>"+ item.privilege +"</td>"+
                "<td>"+ item.lastlogin +"</td>"+
                "<td><div class='popup01'><a href='javascript:'>编辑</a></div> | <a href='#'>删除</a></td></tr>"
            );
            });
        $(".popup01 a").click(function () {
                popWin.showWin("500","430","用户编辑","user_edit.html");
        });
    });
});

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
                    var email = user_info["email"];
                    var privilege = user_info["privilege"];
                    var lastlogin = user_info["lastlogin"];


                    $("table").append(
                        "<tr><td>"+ uid +"</td>"+
                        "<td>"+ username +"</td>"+
                        "<td>"+ nickname +"</td>"+
                        "<td>"+ password +"</td>"+
                        "<td>"+ email +"</td>"+
                        "<td>"+ privilege +"</td>"+
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
