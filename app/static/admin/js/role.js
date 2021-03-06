layui.config({
    base: '/static/admin/src/',
}).use(['index', 'datagrid', 'form'], function () {

    var $ = layui.$,
        datagrid = layui.datagrid,
        active = datagrid.active,
        form = layui.form;


    var  grid_id_filter = "LAY-app-content-list";


    var config = [
        {checkbox: true, fixed: true}
        // , {field: 'id', title: 'ID', width: 80, fixed: true, unresize: true,}
        , {
            field: 'name', title: '角色名称', width: 240, edit: 'text', templet: function (d) {
                return '<span style="color: green;">' + d.name + '</span>';
            }
        }
        , {field: 'label', title: '角色简介', edit: 'text'}
        , {
            field: 'active',
            title: '状态',
             width: 110,
            align: 'center',
            templet: '#checkboxTpl',
            fixed: 'right',
            unresize: true
        }
        , {title: '操作', width: 140, align: 'center', toolbar: '#action_menu', fixed: 'right', unresize: true,}
    ];


    datagrid.renderNoPage(grid_id_filter, config);

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


    form.on('checkbox(ckeckmenu)', function (data) {
        if (data.elem.checked === true) {
            $(data.elem).parents('td').siblings('td').find('input').prop('checked', true);
        } else {
            $(data.elem).parents('td').siblings('td').find('input').prop('checked', false);
        }
        form.render('checkbox');
    });


});