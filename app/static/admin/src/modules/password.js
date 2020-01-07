layui.define(["form", "toastr"], function (exports) {
    var $ = layui.$,
        layer = layui.layer,
        toastr = layui.toastr,
        i = (layui.laytpl, layui.setter, layui.view, layui.admin),
        form = layui.form;
    form.verify({
        pass: [/^[\S]{6,20}$/, "密码必须6到20位，且不能出现空格"],
        repass: function (t) {
            if (t !== $("#LAY_password").val()) return "两次密码输入不一致"
        }
    });
    form.on("submit(setmypass)", function (t) {
        var me = $(this);
        i.req({
            url: me.parents(".layui-form").attr('data-url'),
            type: "post",
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf-token]').attr('content'))
                }
                layer.load();
            },
            data: t.field,
            done: function (e) {
                layer.closeAll();
                if (e.error_code === 0) {
                    toastr.success(e.msg);
                    setTimeout(function () {
                        window.location.reload();
                    }, 1000);
                } else {
                    toastr.error(e.msg);
                }
            }
        });
    });
    exports("password", {})
});