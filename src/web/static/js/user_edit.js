/**
 * Created by hang on 16-12-20.
 */

$(document).ready(function(){
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
            if(data.code == 201){
                if(!data.result){
                    return;
                }
                result = data.result;
                $("#form_nickname").val(result.nickname);
                $("#form_username").val(result.username);
                $("#form_password").val(result.password);
                $("#form_phone").val(result.phone);

                var priv = result.priv;
                if(priv == 3){
                    priv = "管理员";
                }else if(priv == 2){
                    priv = "运营者";
                }else if(priv == 1){
                    priv = "访客者";
                }else{
                    priv = "??";
                }
                
                $(".select").children("dt").html(priv);
            }
        }
    });
});


$(function(){
    $(".select").each(function(){
        var s = $(this);
        var z = parseInt(s.css("z-index"));
        var dt = $(this).children("dt");
        var dd = $(this).children("dd");
        var _show = function(){
            dd.slideDown(200);
            dt.addClass("cur");
            s.css("z-index",z+1);
        };
        var _hide = function(){
            dd.slideUp(200);
            dt.removeClass("cur");
            s.css("z-index",z);
        };
        
        dt.click(function(){
            dd.is(":hidden")?_show():_hide();
        });
        
        dd.find("a").click(function(){
            dt.html($(this).html());
            hide();
        });
        
        $("body").click(function(i){
            !$(i.target).parents(".select").first().is(s) ? _hide():"";
        });
    });
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
