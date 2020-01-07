layui.config({
    base: '/static/admin/src/',
}).use(['index', 'form', 'common'], function () {
    var $ = layui.$,
        form = layui.form,
        common = layui.common;

    form.verify({
        nickname: function (value, item) {
            if (value.length < 3 || value.length > 20) {
                return '昵称长度3-20位';
            }
            if (!new RegExp("^[a-zA-Z0-9_\u4e00-\u9fa5\\s·]+$").test(value)) {
                return '昵称不能有特殊字符';
            }
            if (/(^\_)|(\__)|(\_+$)/.test(value)) {
                return '昵称首尾不能出现下划线\'_\'';
            }
            if (/^\d+\d+\d$/.test(value)) {
                return '昵称不能全为数字';
            }
        },
        chinese_name: function (value, item) {
            if (!/^[\u4e00-\u9fa5]{2,10}$/.test(value) && value.length > 0) {
                return '真实姓名2-10个汉字';
            }
        },
        myphone: function (value, item) {
            if (!/^[1][3,4,5,7,8][0-9]{9}$/.test(value) && value.length > 0) {
                return '手机号码格式不正确';
            }
        },
        qq: function (value, item) {
            if (!/^\d{5,12}$/.test(value) && value.length > 0) {
                return 'qq号码为5位以上数字';
            }
        }
    });
    common.formEvent('setProfile');


});