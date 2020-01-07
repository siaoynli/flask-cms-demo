layui.config({
    base: '/static/admin/src/',
}).use(['index', 'datagrid', 'form', 'common'], function () {

    var $ = layui.$,
        datagrid = layui.datagrid,
        active = datagrid.active,
        form = layui.form;


    var grid_id_filter = "LAY-app-content-list";


    var config = [
        {checkbox: true, fixed: true}
        , {field: 'id', title: 'ID', width: 80, sort: true, fixed: true, unresize: true,}
        , {
            field: 'content', title: '留言内容', edit: 'textarea', templet: function (d) {
                if (d.html === undefined) {
                    d.html = "";
                }
                return  d.html + d.content;
            }
        }
        , {
            field: 'username', width: 120, align: 'center', title: '发布者'
        }
        , {
            field: 'user_type', width: 100, align: 'center', title: '用户类型', templet: function (d) {
                if (d.user_type === 'user') {
                    return '<i class="layui-icon layui-icon-user" title="前台用户"></i>';
                } else {
                    return '<i class="layui-icon layui-icon-group" title="管理员"></i>';
                }
            }
        }
        , {
            field: 'good', width: 80, align: 'center', sort: true, edit: 'number', title: '点赞数'
        }
        , {
            field: 'published_at', width: 200, align: 'center', sort: true, title: '发布时间'
        }
        , {
            field: 'ip', width: 120, align: 'center', title: 'IP地址'
        }

        , {
            field: 'active',
            title: '状态',
            width: 110,
            align: 'center',
            templet: '#checkboxTpl',
            fixed: 'right',
            sort: true,
            unresize: true
        }
        , {title: '操作', width: 140, align: 'center', toolbar: '#action_menu', fixed: 'right', unresize: true,}
    ];


    datagrid.render(grid_id_filter, config);


    //弹窗添加修改
    form.on("submit(app-form-submit)", function (data) {
        var type = $(this).data('type');
        active[type] ? active[type].call(this, data, grid_id_filter) : '';
        return false;
    });

    //table内表单事件
    form.on('checkbox(lock)', function (obj) {
        var type = $(this).data('type');
        active[type] ? active[type].call(this, obj, grid_id_filter) : '';

    });

    datagrid.tableEvent(grid_id_filter);


});