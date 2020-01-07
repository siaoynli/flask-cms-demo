layui.config({
    base: '/static/admin/src/'
}).extend({
    login: 'modules/login'
}).use('login', function () {
    var $ = layui.jquery;
    var obj = $("form");
    var submit = obj.find('button.submit');
    var name = obj.find('input[name=name]');
    var avatar = obj.find('.ui-avatar');
    login = layui.login;

    submit.click(function () {
        login.loginClick();
    });

    name.blur(function () {
        login.blur();
    });

    avatar.click(function () {
        login.avatarClick();
    });

});