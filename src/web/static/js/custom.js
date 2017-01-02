/**
 * project: hjs_cms
 * author: s0nnet
 */


/*客户列表-展示*/
function get_custom_list(){
    var req_type = "GET";
    var req_url = "/api/custom/list";
    var req_data = {"page": 1, "length":1000};
    ajax_request_custom(req_type, req_url, req_data);
}

/*客户列表-查找*/
function search_custom_list(){
    var search = $("#search_data").val();
    var status = $(".select").children(".search_status").html();
    if(status =="正常"){
        status = "normal";
    }else if(status == "已删除"){
        status = "delete";
    }else{
        status = "all";
    }

    var req_type = "POST";
    var req_url = "/api/custom/list";
    var req_data = {"page":1, "length":1000, "status":status, "search": search};
    ajax_request_custom(req_type, req_url, req_data);
}


/* ajax 请求客户列表数据*/
function ajax_request_custom(req_type, req_url, req_data){

    $.ajax({
        type: req_type,
        async: true,
        dataType: "json",
        url: req_url,
        data: req_data,
        error: function(){
            console.log("/api/custom/list/error");
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
                var dataLen = data.result.custom_list.length;
                for(var i = 0; i < dataLen; i++){
                    var custom_info = data.result.custom_list[i];
                    var cid = custom_info["cid"];
                    var name = custom_info["name"];
                    var address = custom_info["address"];
                    var phone = custom_info["phone"];
                    var ctype = custom_info["ctype"];
                    var class_priv = custom_info["class_priv"];
                    var status = custom_info["status"];
                    var remark = custom_info["remark"];
                    var insert_tm = custom_info["insert_tm"];


                    if(ctype == "O"){
                        ctype = "老";
                    }else if(ctype == "N"){
                        ctype = "新";
                    }else{
                        ctype = ctype;
                    }

                    if(status == "normal"){
                        status = "正常";
                    }else if(status=="delete"){
                        status = "已删除";
                    }else{
                        status = status;
                    }


                    $("table").append(
                        "<tr><td>"+ cid +"</td>"+
                        "<td>"+ name +"</td>"+
                        "<td>"+ address +"</td>"+
                        "<td>"+ phone +"</td>"+
                        "<td>"+ ctype +"</td>"+
                        "<td>"+ class_priv +"</td>"+
                        "<td>"+ status +"</td>"+
                        "<td>"+ remark +"</td>"+
                        "<td>"+ insert_tm +"</td>"+
                        "<td><div class='popup01'><a href='#' onclick=add_order('"+cid+"')>订单</a> | <a href='#' onclick=edit_custom('"+cid+"')>编辑</a></div> | <a href='#' onclick=del_custom('"+ cid +"')>删除</a></td></tr>"
                    );
                    $("#data_count").html(dataLen);
                }
            }
        }
    });
}

/*客户删除*/
function del_custom(cid){
    if(!confirm("确认删除该用户？")){
        return;
    }
    $.ajax({
        type: "POST",
        async: true,
        dataType: "json",
        url: "/api/custom/del",
        data: {"cid": cid},
        error: function() {
            console.log("/api/custom/del/error");
        },
        success: function(data){
            if(data.code == 201){
                get_custom_list();
            }else{
                alert("删除用户失败[Error:" + data.message + "]");
            }
        }
    });
}


/*编辑用户*/
function edit_custom(cid){
    var params = "cid=" + cid;
    popWin.showWin("500","470","用户编辑","custom_edit.html", params);

}


/*编辑页面-获取客户信息*/
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
                $("#form_address").val(result.address);
                $("#form_phone").val(result.phone);
                $("#form_remark").val(result.remark);

                var ctype = result.ctype;
                if(ctype == "O"){
                    ctype = "老";
                }else if(ctype == "N"){
                    ctype = "新";
                }else{
                    ctype= ctype;
                } 
                $(".select").children(".ctype").html(ctype);
                
                $(".select").children(".class_priv").html(result.class_priv);

                var status = result.status;
                if(status == "normal"){
                    status = "正常";
                }else if(status == "delete"){
                    status = "已取消";
                }else{
                    status = status;
                }
                $(".select").children(".status").html(status);
            }
        } 
    });
}


/*提交修改后的数据*/
function update_custom_info(){
    var cid = $("#form_cid").val();
    var name = $("#form_name").val();
    var address = $("#form_address").val();
    var phone = $("#form_phone").val();
    var remark = $("#form_remark").val();

    var ctype = $(".select").children(".ctype").html();
    if(ctype == "老"){
        ctype = "O";
    }else if(ctype == "新"){
        ctype = "N";
    }else{
        ctype = ctype;
    }

    var class_priv = $(".select").children(".class_priv").html();

    var status = $(".select").children(".status").html();
    if(status == "正常"){
        status = "normal";
    }else if(status == "已取消"){
        status = "delete";
    }else{
        status = status;
    }

    $.ajax({
        type: "POST",
        async: true,
        dataType: "json",
        url: "/api/custom/update",
        data: {
            "cid":cid,
            "nickname": name,
            "address": address,
            "phone": phone,
            "ctype": ctype,
            "class_priv": class_priv,
            "status": status,
            "remark": remark
        },
        error: function(){
            console.log("/api/custom/update/error");
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


/*添加客户*/
function add_custom(){
    var name = $("#form_name").val();
    var address = $("#form_address").val();
    var phone = $("#form_phone").val();
    var ctype = $(".select").children(".ctype").html();
    var class_priv = $(".select").children(".class_priv").html();
    var status = $(".select").children(".status").html();
    var remark = $("#form_remark").val();

    if(ctype == "新"){
        ctype = "N";
    }else{
        ctype = "O";
    }

    if(status=="正常"){
        status = "normal";
    }else{
        status = "delete";
    }

    $.ajax({
        type: "POST",
        async: true,
        dataType: "json",
        url: "/api/custom/add",
        data: {
            "nickname": name,
            "address": address,
            "phone": phone,
            "ctype": ctype,
            "class_priv": class_priv,
            "status": status,
            "remark": remark
        },
        error: function(){
            console.log("/api/custom/add/error");
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


