/**
 * project: hjs_cms
 * author: s0nnet
 */



/*订单列表-展示*/
function get_order_today(){
    var req_type = "GET";
    var req_url = "/api/order/today";
    var req_data = {"page": 1, "length":1000};
    ajax_request_order(req_type, req_url, req_data);
}

/*订单列表-查找*/
function search_order_today(){
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
    var req_url = "/api/order/today";
    var req_data = {"page":1, "length":1000, "status":status, "search": search};
    ajax_request_order(req_type, req_url, req_data);
}


/* ajax 请求客户列表数据*/
function ajax_request_order(req_type, req_url, req_data){


    $.ajax({
        type: req_type,
        async: true,
        dataType: "json",
        url: req_url,
        data: req_data,
        error: function(){
            console.log("/api/order/today/error");
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
                var dataLen = data.result.length;
                for(var i = 0; i < dataLen; i++){
                    var order_info = data.result[i];
                    var oid = order_info["oid"];
                    var cid = order_info["cid"];
                    var name = order_info["name"];
                    var address= order_info["address"];
                    var phone = order_info["phone"];
                    var otype = order_info["otype"];
                    var ctype = order_info["ctype"];
                    var status = order_info["status"];
                    var remark = order_info["remark"];

                    if(status=="normal"){
                        status = "正常";
                    }else if(status == "stop"){
                        status = "暂取消";
                    }else{
                        status = status;
                    }

                    if(ctype == "O"){
                        ctype = "老";
                    }else if(ctype == "N"){
                        ctype = "新";
                    }else{
                        ctype = ctype;
                    }

                    $("table").append(
                        "<tr><td>"+ oid +"</td>"+
                        "<td>"+ cid +"</td>"+
                        "<td>"+ name +"</td>"+
                        "<td>"+ address +"</td>"+
                        "<td>"+ phone +"</td>"+
                        "<td>"+ otype +"</td>"+
                        "<td>"+ ctype +"</td>"+
                        "<td>"+ status +"</td>"+
                        "<td>"+ remark +"</td>"+
                        "<td><div class='popup01'><a href='#' onclick=stop_order('"+oid+"')>今日取消</a></div></td></tr>"
                    );
                    $("#data_count").html(dataLen);
                }
            }
        }
    });
}

/*订单数据CSV文件导出*/
function export_order_today(){

    $.ajax({
        type: "GET",
        async: true,
        dataType: "json",
        url: "/api/order/today",
        data: {"page": 1, "length":10000},
        error: function(){
            console.log("/api/order/today/error");
        },
        success: function(data){
            if(data.code == 101){
                alert("export fail: "+data.message);
            }
            if(data.code == 201){
                if(!data.result){
                    return;
                }
                jsonData = data.result;
                order_jsonTocsv(jsonData, true);
            }
        }  
    });
}

/*order: jsonTocsv*/
function order_jsonTocsv(JSONData, ShowLabel) {
    var arrData = typeof JSONData != 'object' ? JSON.parse(JSONData) : JSONData;
    var CSV = '';

    if (ShowLabel) {
　　　　//add column index
        var row = "订单号,客户号,客户姓名,配送地址,联系电话,奶类,客户类型,订单状态,备注,说明1,说明2";
        CSV += row + '\r\n';
    }
    
    //loop each column
    for (var i = 0; i < arrData.length; i++) {
        var row = "";

        item = arrData[i];

        var status = item.status;
        if(status == "normal"){
            status = "正常";
        }else if(status == "stop"){
            status = "暂取消";
        }else{
            status = status;
        }

        var ctype = item.ctype;
        if(ctype == "O"){
            ctype = "老";
        }else if(ctype == "N"){
            ctype = "新";
        }else{
            ctype = ctype;
        }

        row += '"'+ item.oid +'",'+
               '"'+ item.cid +'",'+
               '"'+ item.name +'",'+
               '"'+ item.address +'",'+
               '"'+ item.phone +'",'+
               '"'+ item.otype +'",'+
               '"'+ ctype +'",'+
               '"'+ status +'",'+
               '"'+ item.remark +'",'+'" ",'+'" "';

        CSV += row + '\r\n';
    }

    if (CSV == '') {        
        alert("Invalid data");
        return;
    }   
    
    var d = new Date();
    var year = d.getFullYear();
    var month = d.getMonth()+1;
    var date = d.getDate();
    var hour = d.getHours();
    var minute = d.getMinutes();
    var timestr = year+"_"+month+"_"+date+"_"+hour+"_"+minute;

    var fileName = "今日订单列表_导出_"+timestr;
    var uri = 'data:text/csv;charset=utf-8,\uFEFF' + encodeURI(CSV);
    
    var link = document.createElement("a");    
    link.href = uri;
    
    link.style = "visibility:hidden";
    link.download = fileName + ".csv";
    
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
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


