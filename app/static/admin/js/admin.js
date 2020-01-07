layui.config({
    base: '/static/admin/src/',
}).use(['index', 'datagrid', 'form', 'common'], function () {

    var $ = layui.$,
        datagrid = layui.datagrid,
        active = datagrid.active,
        common = layui.common,
        form = layui.form;

    var grid_id_filter = "LAY-app-content-list";


    var config = [
        {checkbox: true, fixed: true}
        // , {field: 'id', title: 'ID', width: 40, fixed: true, unresize: true,}
        , {
            field: 'name', align: "center", title: '用户名', width: 120, templet: function (d) {
                return '<span style="color: green;">' + d.name + '</span>';
            }
        }
        , {
            field: 'avatar',
            align: "center",
            title: '头像',
            width: 80,
            unresize: true,
            edit: 'images',
            templet: function (d) {
                if (d.avatar) {
                    return '<img src="' + d.avatar + '" class="avatar" lay-tips="单击查看头像">';
                } else {
                    return '<img src="/static/admin/images/guest.png" class="avatar" >';
                }
            }
        }, {
            field: 'role_name',
            align: "center",
            title: '角色',
            width: 120,
            unresize: true,
            templet: function (d) {
                if (d.role) {
                    var role = JSON.parse(d.role);
                    return role.name
                } else {
                    return '-'
                }
            }
        }
        , {field: 'nick_name', align: "center", title: '昵称', width: 100, edit: 'text'}
        , {
            field: 'sex',
            title: '性别',
            width: 80,
            align: 'center',
            unresize: true,
            templet: function (d) {
                if (d.sex == 1) {
                    return '<i class="layui-icon layui-icon-male male-color" title="男" ></i>';
                } else if (d.sex == 2) {
                    return '<i class="layui-icon layui-icon-female female-color" title="女" ></i>';
                } else {
                    return '保密';
                }
            }
        }
        , {field: 'chinese_name', align: "center", title: '中文姓名', width: 100, edit: 'text'}
        , {field: 'email', align: "center", title: '邮箱', width: 200, edit: 'text'}
        , {field: 'phone', align: "center", title: '手机号码', width: 150, edit: 'text'}
        , {field: 'qq', align: "center", title: 'QQ', width: 120, edit: 'text'}
        , {field: 'login_ip', align: "center", title: '登录IP', width: 120}
        , {field: 'login_time', align: "center", title: '登录时间', sort: true, width: 200}
        , {field: 'login_count', align: "center", title: '登录次数', sort: true, width: 150}
        , {
            field: 'active',
            title: '状态',
             width: 110,
            align: 'center',
            templet: '#checkboxTpl',
            sort: true,
            fixed: 'right',
            sort: true,
            unresize: true
        }
        , {title: '操作', width: 140, align: 'center', toolbar: '#action_menu', fixed: 'right', unresize: true,}
    ];

    form.verify({
        name: function (value, item) {
            if (value.length < 3 || value.length > 20) {
                return '用户名长度3-20位';
            }
            if (!new RegExp("^[a-zA-Z0-9_\u4e00-\u9fa5\\s·]+$").test(value)) {
                return '用户名不能有特殊字符';
            }
            if (/(^\_)|(\__)|(\_+$)/.test(value)) {
                return '用户名首尾不能出现下划线\'_\'';
            }
            if (/^\d+\d+\d$/.test(value)) {
                return '用户名不能全为数字';
            }
        },
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
            if (!/^\d{5,20}$/.test(value) && value.length > 0) {
                return 'qq号码为5位以上数字';
            }
        },
        avatar: function (value, item) {
            if (value.length <= 0) {
                return '请上传头像';
            }
        },
    });

    common.lay_upload('#upload-avatar', false, function (res, index, item) {
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
        common.active['re_upload_img'].call(this, true)
    });

    //以下为公共部分


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

    datagrid.renderNoPage(grid_id_filter, config);
    datagrid.tableEvent(grid_id_filter);


});