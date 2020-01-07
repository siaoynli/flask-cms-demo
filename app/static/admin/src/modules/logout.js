layui.define(function(exports) {
    var i = (layui.$, layui.layer, layui.laytpl, layui.setter, layui.view, layui.admin);
    var $ = layui.$,
        layer = layui.layer,
        logout = $("#logout");
    var logout_url = logout.attr('data-logout-url');
    var login_url = logout.attr('data-login-url');
    i.events.logout = function() {
        layer.confirm('您确认要退出系统吗?', {
            btn: ['是', '否'],
            icon: 3,
            title: '提示'
        }, function() {
            layer.closeAll('dialog');
            i.req({
                url: logout_url,
                type: "get",
                data: {},
                done: function(e) {
                    i.exit(function() {
                        location.href = login_url
                    })
                }
            });
        });
    };
    exports('logout', {});
});