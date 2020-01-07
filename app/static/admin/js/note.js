layui.config({
    base: '/static/admin/src/',
}).use(['index', 'datagrid', 'form', 'common'], function () {

    var $ = layui.$,
        datagrid = layui.datagrid,
        active = datagrid.active,
        common = layui.common,
        form = layui.form;


    var  grid_id_filter = "LAY-app-content-list";


    var config = [
        {checkbox: true, fixed: true}
        , {field: 'id', title: 'ID', width: 80,sort: true, fixed: true, unresize: true,}
        , {field: 'content', title: '公告内容', edit: 'textarea'}
        , {field: 'start_date', width: 150, align: 'center', title: '起始时间',sort: true, edit: 'date',}
        , {field: 'end_date', width: 150, align: 'center', title: '结束时间',sort: true, edit: 'date',}
        , {field: 'level', width: 80, align: 'center', title: '排序',sort: true, edit: 'number',}
        , {
            field: 'admin_name', width: 120, align: 'center', title: '发布者', templet: function (d) {
                if (d.admin) {
                    var admin = JSON.parse(d.admin);
                    return admin.name
                } else {
                    return '-'
                }
            }
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


    form.verify({
        end_date: function (value, item) {
            if (value <= $("#start_date").val()) {
                return '结束时间必须大于起始时间';
            }

        }

    });


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

    form.on('switch(switch)', function (obj) {
        var type = $(this).data('type');
        active[type] ? active[type].call(this, obj, grid_id_filter) : '';
    });

    datagrid.tableEvent(grid_id_filter);

    datagrid.lay_date('.laydate');

    //表单下拉select事件
    form.on("select(app-form-select)", function () {
        active['chooseSelect'].call(this);
    });

    $(".layui-form").on('click', '.laydate', function () {
         active['dropSelect'].call(this);
    });

});