/**
 * Created by hang on 16-12-18.
 */
$(document).ready(function () {
    var custom_type;
    $("tr:contains(客户类型) li:eq(0)").click(function () {
        custom_type = "N";
        return custom_type;
    });
    $("tr:contains(客户类型) li:eq(1)").click(function () {
        custom_type = "O";
        return custom_type;
    });

    var custom_class;
    $("dl:contains(A) li:eq(0)").click(function () {
        custom_class = "A";
        return custom_class;
    });
    $("dl:contains(A) li:eq(1)").click(function () {
        custom_class = "B";
        return custom_class;
    });
    $("dl:contains(A) li:eq(2)").click(function () {
        custom_class = "C";
        return custom_class;
    });
    $(":button:eq(1)").click(function () {
        $.post("/api/custom/add",
            {
                nickname: $(":text:eq(0)").val(),
                name: $(":text:eq(1)").val(),
                phone: $(":text:eq(2)").val(),
                ctype: custom_type,
                class: custom_class,
                remark: $(":text:eq(3)").val()
            },
            function (data, status) {
                alert("提交情况：" + status +"\n"+ "数据结果："+ data);
            });
    })
});