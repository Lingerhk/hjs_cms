/**
 * project: hjs_cms
 * author: s0nnet
 */


/*选择下拉框*/
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
            _hide();
        });

        $("body").click(function(i){
            !$(i.target).parents(".select").first().is(s) ? _hide():"";
        });
    });
});



