/**
 * project: hjs_cms
 * author: s0nnet
 *
 */


/*用户列表*/
function get_data_count(){
    $.ajax({
        type: "GET",
        async: true,
        dataType: "json",
        url: "/api/data/count",
        error: function(){
            console.log("/api/data/count/error");
        },
        success: function(data){
            if(data.code == 101){
                alert(data.message);
            }
            if(data.code == 201){
                if(!data.result){
                    return;
                }
                
                var dt_custom = data.result.dt_custom;
                $("#custom_cnt").html(dt_custom.custom_cnt);
                $("#custom_nor").html(dt_custom.custom_nor);
                $("#custom_can").html(dt_custom.custom_can);

                var dt_order = data.result.dt_order;
                $("#order_cnt").html(dt_order.order_cnt);
                $("#order_nor").html(dt_order.order_nor);
                $("#order_stop").html(dt_order.order_stop);
                $("#order_today").html(dt_order.order_today);
                $("#order_today_stop").html(dt_order.order_today_stop);

                var dt_days = data.result.dt_days;

                var days_3_count = dt_days.days_3.count;
                var days_3_list = dt_days.days_3.list;
                var lists = '人 -> ';
                for(var i=0; i < days_3_list.length; i++){
                    res = days_3_list[i];
                    oid = res['oid'];
                    name = res['name'];
                    end_tm = res['end_tm'];
                    lists += '['+oid+' '+name+' '+end_tm+'],';
                }
                var days3 = days_3_count + lists;
                $("#days_3").html(days3);

                var days_7_count = dt_days.days_7.count;
                var days_7_list = dt_days.days_7.list;
                var lists = '人 -> ';
                for(var i=0; i < days_7_list.length; i++){
                    res = days_3_list[i];
                    oid = res['oid'];
                    name = res['name'];
                    end_tm = res['end_tm'];
                    lists += '['+oid+' '+name+' '+end_tm+'],';
                }
                var days7 = days_7_count + lists;
                $("#days_7").html(days7);

                $("#update_date").html(data.result.update_date);
            }
        }
    });
}
