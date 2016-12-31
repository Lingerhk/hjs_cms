/**
 * project: hjs_cms
 * author: s0nnet
 */



/*订单列表-展示*/
function get_order_list(){
    var req_type = "GET";
    var req_url = "/api/order/list";
    var req_data = {"page": 1, "length":1000};
    ajax_request(req_type, req_url, req_data);
}

/*订单列表-查找*/
function search_order_list(){
    var search = $("#search_data").val();
    var status = $(".select").children(".search_status").html();
    if(status =="正常"){
        status = "normal";
    }else if(status == "已取消"){
        status = "stop";
    }else{
        status = "all";
    }

    var req_type = "POST";
    var req_url = "/api/order/list";
    var req_data = {"page":1, "length":1000, "status":status, "search": search};
    ajax_request(req_type, req_url, req_data);
}


/* ajax 请求客户列表数据*/
function ajax_request(req_type, req_url, req_data){


    $.ajax({
        type: req_type,
        async: true,
        dataType: "json",
        url: req_url,
        data: req_data,
        error: function(){
            console.log("/api/order/list/error");
        },
        success: function(data){
            if(data.code == 101){
                alert(data.message);
            }
            if(data.code == 201){
                $("table tr:not(:first)").remove();
                if(!data.result){
                    $("#data_count").html("0");
                    return;
                }
                var dataLen = data.result.order_list.length;
                for(var i = 0; i < dataLen; i++){
                    var order_info = data.result.order_list[i];
                    var oid = order_info["oid"];
                    var cid = order_info["cid"];
                    var name = order_info["name"];
                    var otype= order_info["otype"];
                    var order_tm = order_info["order_tm"];
                    var start_tm = order_info["start_tm"];
                    var end_tm = order_info["end_tm"];
                    var amount= order_info["amount"];
                    var cash = order_info["cash"];
                    var status = order_info["status"];
                    var remark = order_info["remark"];
                    var insert_tm = order_info["insert_tm"];

                    if(status=="normal"){
                        status = "正常";
                    }else if(status == "stop"){
                        status = "已取消";
                    }else{
                        status = status;
                    }

                    $("table").append(
                        "<tr><td>"+ oid +"</td>"+
                        "<td>"+ cid +"</td>"+
                        "<td>"+ name +"</td>"+
                        "<td>"+ otype +"</td>"+
                        "<td>"+ order_tm +"</td>"+
                        "<td>"+ start_tm +"</td>"+
                        "<td>"+ end_tm +"</td>"+
                        "<td>"+ amount +"</td>"+
                        "<td>"+ cash +"</td>"+
                        "<td>"+ status +"</td>"+
                        "<td>"+ remark +"</td>"+
                        "<td>"+ insert_tm +"</td>"+
                        "<td><div class='popup01'><a href='#' onclick=edit_order('"+oid+"')>编辑</a></div> | <a href='#' onclick=del_order('"+ oid +"')>删除</a></td></tr>"
                    );
                    $("#data_count").html(dataLen);
                }
            }
        }
    });
}

/*订单删除*/
function del_order(oid){
    if(!confirm("确认删除该用户？")){
        return;
    }
    $.ajax({
        type: "POST",
        async: true,
        dataType: "json",
        url: "/api/order/del",
        data: {"oid": oid},
        error: function() {
            console.log("/api/order/del/error");
        },
        success: function(data){
            if(data.code == 201){
                get_order_list();
            }else{
                alert("删除订单失败[Error:" + data.message + "]");
            }
        }
    });
}


/*添加用户*/
function add_order(cid){
    var params = "cid=" + cid;
    popWin.showWin("500","560","添加订单","order_add.html", params);

}


/*添加订单-获取客户信息*/
function get_custom_info(){
    var cid = get_request_args("cid");

    $.ajax({
        type: "GET",
        async: true,
        dataType: "json",
        url: "/api/custom/info",
        data: {"cid":cid},
        error: function(){
            console.log("/api/custom/info/error");
        },
        success: function(data){
            if(data.code == 201){
                if(!data.result){
                    return;
                }
                result = data.result;
                $("#form_cid").val(cid);
                $("#form_name").val(result.name);
            }
        } 
    });
}


/*提交添加订单的数据*/
function add_order_info(){
    var cid = $("#form_cid").val();
    var otype = $("#form_otype").val();
    var order_tm = $("#form_order_tm").val();
    var start_tm = $("#form_start_tm").val();
    var end_tm = $("#form_end_tm").val();
    var amount = $("#form_amount").val();
    var cash = $("#form_cash").val();
    var remark = $("#form_remark").val();


    $.ajax({
        type: "POST",
        async: true,
        dataType: "json",
        url: "/api/order/add",
        data: {
            "cid":cid,
            "otype": otype,
            "order_tm": order_tm,
            "start_tm": start_tm,
            "end_tm": end_tm,
            "amount": amount,
            "cash": cash,
            "remark": remark
        },
        error: function(){
            console.log("/api/order/add/error");
        },
        success: function(data){
            if(data.code == 101){
                alert(data.message);
            }
            if(data.code == 201){
                alert("添加订单成功,请关闭窗口并刷新！");
            }
        }
    });
}


/*编辑订单*/
function edit_order(oid){
    var params = "oid=" + oid;
    popWin.showWin("500","550","编辑订单","order_edit.html", params);
}


/*编辑订-获取订单信息*/
function get_order_info(){
    var oid = get_request_args("oid");

    $.ajax({
        type: "GET" ,
        async: true,
        dataType: "json",
        url: "/api/order/info",
        data:{"oid": oid},
        error: function(){
            console.log("/api/order/info/error");
        },
        success: function(data){
            if(data.code == 201){
                if(!data.result){
                    return;
                }
                result = data.result;
                $("#form_oid").val(result.oid);
                $("#form_name").val(result.name);
                $("#form_otype").val(result.otype);
                $("#form_order_tm").val(result.order_tm);
                $("#form_start_tm").val(result.start_tm);
                $("#form_end_tm").val(result.end_tm);
                $("#form_amount").val(result.amount);
                $("#form_cash").val(result.cash);
                $("#form_remark").val(result.remark);

                var status = result.status;
                if(status=="normal"){
                    status = "正常";
                }else if(status == "stop"){
                    status = "已取消";
                }else{
                    status = status;
                }
                $(".select").children(".status").html(status);
            }
        }
    });

}


/*提交修改好的订单数据*/
function update_order_info(){
    var oid = $("#form_oid").val();
    var otype = $("#form_otype").val();
    var order_tm = $("#form_order_tm").val();
    var start_tm = $("#form_start_tm").val();
    var end_tm = $("#form_end_tm").val();
    var amount = $("#form_amount").val();
    var cash = $("#form_cash").val();
    var remark = $("#form_remark").val();
    
    var status = $(".select").children(".status").html();
    if(status == "正常"){
        status = "normal";
    }else if(status == "已取消"){
        status = "stop";
    }else{
        status = status;
    }

    $.ajax({
        type: "POST",
        async: true,
        dataType: "json",
        url: "/api/order/update",
        data: {
            "oid":oid,
            "otype": otype,
            "order_tm": order_tm,
            "start_tm": start_tm,
            "end_tm": end_tm,
            "amount": amount,
            "cash": cash,
            "status": status,
            "remark": remark
        },
        error: function(){
            console.log("/api/order/update/error");
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


/*表单下拉框*/
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


