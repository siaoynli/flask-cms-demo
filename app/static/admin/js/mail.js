layui.config({
    base: '/static/admin/src/',
}).use(['index', 'form', 'common'], function () {
    var $ = layui.$,
        form = layui.form,
        common = layui.common;
    common.formEvent('setMail');
});