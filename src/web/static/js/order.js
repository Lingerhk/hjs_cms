/**
 * project: hjs_cms
 * author: s0nnet
 */


/*订单列表*/
function get_order_list(){
    var page = 1;
    var length = 20;

    $.ajax({
        type: "GET",
        async: true,
        dataType: "json",
        url: "/api/order/list",
        data: {"page": page, "length": length},
        error: function(){
            console.log("/api/order/list/error");
        },
        success: function(data){
            if(data.code == 101){
                alert(data.message);
            }
            if(data.code == 201){
                if(!data.result){
                    $("table tr").append("<p>当前订单列表为空，请先添加订单！</p>");
                    return;
                }
                $("table tr:not(:first)").empty();
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
                    var remark = order_info["remark"];
                    var insert_tm = order_info["insert_tm"];

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
                        "<td>"+ remark +"</td>"+
                        "<td>"+ insert_tm +"</td>"+
                        "<td><div class='popup01'><a href='#' onclick=edit_order('"+oid+"')>编辑</a></div> | <a href='#' onclick=del_order('"+ oid +"')>删除</a></td></tr>"
                    );
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
    popWin.showWin("500","465","编辑订单","order_edit.html", params);
}


/*编辑订-获取订单信息*/
function get_order_info(){
    var oid = get_request_args("oid");


}




/*提交修改好的订单数据*/
function update_order_info(){
    


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


