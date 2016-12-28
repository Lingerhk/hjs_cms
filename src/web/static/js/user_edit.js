/**
 * Created by hang on 16-12-20.
 */
/**
 * Created by hang on 16-12-20.
 */


$(document).ready(function () {
        var uid = get_request_args("uid");
        $.get("/api/user/info",
            {
                uid: uid//发送当前用户的id
            },
            function (data) {
                $(":text:eq(1)").val(data.result.nickname);
                $(":text:eq(2)").val(data.result.username);
                $(":text:eq(3)").val(data.result.password);
                $(":text:eq(4)").val(data.result.phone);
                $("dt:contains('选择')").text(data.result.priv);//用户等级
                $("tr:contains(用户等级) dt:eq(0)").html($("tr:contains(用户等级) dt:eq(0)").html().replace(/3/g,"管理者"));
                $("tr:contains(用户等级) dt:eq(0)").html($("tr:contains(用户等级) dt:eq(0)").html().replace(/2/g,"运营者"));
                $("tr:contains(用户等级) dt:eq(0)").html($("tr:contains(用户等级) dt:eq(0)").html().replace(/1/g,"访客者"));
        });

    //用户等级换值模块
    var user_class;
    $("tr:contains(用户等级) li:eq(0)").click(function () {
        custom_class = 3;
        return user_class;
    });
    $("tr:contains(用户等级) li:eq(1)").click(function () {
        custom_class = 2;
        return user_class;
    });
    $("tr:contains(用户等级) li:eq(2)").click(function () {
        custom_class = 1;
        return user_class;
    });


    $(":button:eq(1)").click(function () {
        $.post("/api/user/update",
            {
                uid:uid,
                name: $(":text:eq(1)").val(),
                nickname: $(":text:eq(2)").val(),
                password: $(":text:eq(3)").val(),
                phone: $(":text:eq(4)").val(),
                priv:user_class//用户等级
            },
            function (data, status) {
                alert("提交情况：" + status +"\n"+ "数据结果："+ data);
            });
    })
});


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
