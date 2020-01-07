layui.config({
    base: '/static/admin/src/',
}).use(['index', 'datagrid', 'form','iconPicker'], function () {

    var $ = layui.$,
        datagrid = layui.datagrid,
        active = datagrid.active,
        iconPicker = layui.iconPicker,
        form = layui.form;

    var grid_id_filter = "LAY-app-content-list";


    var config = [
        {checkbox: true, fixed: true}
        , {field: 'id', title: 'ID', width: 40, fixed: true, unresize: true,}
        , {
            field: 'name', title: '导航名称', width: 240, edit: 'text', templet: function (d) {
                return  d.html+'<span style="color: green;">' + d.name + '</span>';
            }
        }
        , {field: 'label', title: '导航简介', event: 'txt_label'}
        , {
            field: 'icon',
            align: "center",
            title: '图标',
            width: 120,
            unresize: true,
            edit: 'text',
            templet: function (d) {
                return '<i class="layui-icon ' + d.icon + '"></i>  ';
            }
        }
        , {field: 'level', align: "center", title: '排序', width: 60, unresize: true, edit: 'number'}
        , {field: 'endpoint_name', title: 'endpoint名称', width: 200, unresize: true, edit: 'text'}
        , {
            field: 'target',
            title: '新窗口',
            width: 110,
            align: 'center',
            templet: '#switchTpl',
            fixed: 'right',
            unresize: true
        }
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

    iconPicker.render({
                elem: '#iconPicker',
                type: 'fontClass',
                search: true,
    });

     //选中图标
    iconPicker.checkIcon('iconPicker', $('#iconPicker').val());


});