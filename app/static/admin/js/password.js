layui.config({
    base: '/static/admin/src/',
}).use(['index', 'form', 'common'], function () {
    var $ = layui.$,
        common = layui.common,
        form = layui.form;
    form.verify({
        pass: [/^[\S]{6,20}$/, "密码必须6到20位，且不能出现空格"],
        repass: function (t) {
            if (t !== $("#LAY_password").val()) return "两次密码输入不一致"
        }
    });

    common.formEvent('setmypass');
});