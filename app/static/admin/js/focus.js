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
        , {
            field: 'title', title: '焦点图名称', width: 240, edit: 'text', templet: function (d) {
                return '<span   style="color: green;">' + d.title + '</span>';
            }
        },
        {
            field: 'thumb_image',
            align: "center",
            title: '缩略图',
            width: 200,
            unresize: true,
            edit: 'images',
            templet: function (d) {
                if (d.thumb_image) {
                    return '<img src="' + d.thumb_image + '" lay-tips="单击查看图片" >';
                } else {
                    return '';
                }
            }
        }
        , {field: 'label', title: '焦点图简介',  edit: 'textarea',}
         , {field: 'level',width: 80,align:'center', title: '排序', edit: 'number',}
        , {
            field: 'target',
            title: '新窗口',
            width: 110,
            align: 'center',
            templet: '#switchTpl',
            fixed: 'right',
             sort: true,
            unresize: true
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
        thumb_image: function (value, item) {
            if (value.length <= 0) {
                return '请上传缩略图';
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


    common.lay_upload('#upload-thumb', false, function (res, index, item) {
        var container = item.siblings('.layui-upload-list');
        if (res.code === 0 && res.error_code === 0) {
            item.parents('.layui-form-item').find('input.input-upload').val(res.data.url);
            container.html('<div class="upload-thumb-img"><img src="' + res.data.url + '" lay-tips="单击删除"></div>')
        } else {
            container.find('#lay-' + index).find('span').remove();
            container.find('#lay-' + index).append('<span><i class="layui-icon layui-icon-close-fill" style="font-size: 30px; color: #FF5722;"></i>  </span>');
            return layer.msg(res.msg, {icon: 2, time: 1000});
        }

    });
        //删除上传的单图
    $(".layui-form").on('click', '.upload-thumb-img>img', function () {
        common.active['re_upload_img'].call(this)
    });

});