layui.config({
    base: '/static/admin/src/',
}).use(['index', 'datagrid', 'form', 'element', 'common'], function () {

    var $ = layui.$,
        datagrid = layui.datagrid,
        active = datagrid.active,
        element = layui.element,
        common = layui.common,
        form = layui.form;


    var grid_id_filter = "LAY-app-content-list";


    var config = [
        {checkbox: true, fixed: true}
        , {field: 'id', title: 'ID', width: 80, sort: true, fixed: true, unresize: true,}
        , {
            field: 'title', title: '文档标题', width: 240, edit: 'text', templet: function (d) {
                if (d.external_link) {
                    return '<span title="' + d.title + '">' + d.title + '</span>'
                } else {
                    return d.title;
                }
            }
        }
        , {
            field: 'column_title', align: "center", title: '所属栏目', width: 140, templet: function (d) {
                if (d.column) {
                    var column = JSON.parse(d.column);
                    return '<b>'+column.title+'</b>'
                } else {
                    return '-'
                }
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
        , {
            field: 'attribute',  width: 150, title: '属性', templet: function (d) {
                if (d.attribute) {
                    var tmp = d.attribute.split(',');
                    var html = '';
                    if (tmp.indexOf('R') != -1) {
                        html += '<span class="layui-badge layui-bg-orange">推荐</span>&nbsp;';
                    }
                    if (tmp.indexOf('T') != -1) {
                        html += '<span class="layui-badge  layui-bg-green">置顶</span>&nbsp;';
                    }
                    if (tmp.indexOf('H') != -1) {
                        html += '<span class="layui-badge layui-bg-blu">头条</span>&nbsp;';
                    }
                    return html;
                } else {
                    return '';
                }
            }
        }, {field: 'keyword', width: 300, title: 'META关键字', edit: 'text',}
        , {field: 'description', width: 300, title: 'META描述', edit: 'textarea',}
        , {field: 'label', width: 300, title: '摘要', edit: 'textarea',}

        , {
            field: 'attach_file', width: 100, align: 'center', title: '附件', templet: function (d) {
                if (d.attach_file) {
                    return '<i class="layui-icon layui-icon-link" title="' + d.attach_name + '"></i>';
                } else {
                    return '';
                }
            }
        }


        , {field: 'author', align: 'center', width: 160, title: '作者', edit: 'text',}
        , {field: 'source', align: 'center', width: 160, title: '来源', edit: 'text',}
        , {field: 'click', align: 'center', width: 100, title: '阅读数', edit: 'number'}
        , {field: 'editor', align: 'center', width: 160, title: '编辑', edit: 'text',}
        , {field: 'password_txt', align: 'center', width: 160, title: '密码', edit: 'text',}
        , {field: 'published_at', align: 'center', width: 200, title: '发布时间', edit: 'datetime', sort: true,}
        ,{
            field: 'link', width: 100, align: 'center', title: '访问', templet: function (d) {
                if (d.external_link) {
                    return '<a href="' + d.external_link + '" target="_blank" title="' + d.title + '"><i class="layui-icon layui-icon-website"></i></a>';
                } else {
                    return '';
                }
            }
        }


        , {
            field: 'is_original',
            title: '原创',
            width: 110,
            align: 'center',
            templet: '#originalTpl',
            sort: true,
            unresize: true
        }
        , {
            field: 'open_comment',
            title: '允许评论',
            width: 110,
            align: 'center',
            templet: '#commentTpl',
            sort: true,
            unresize: true
        }
        , {
            field: 'target',
            title: '新窗口',
            width: 110,
            align: 'center',
            templet: '#switchTpl',
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
        title: function (value, item) {
            if (value.length < 3 || value.length > 100) {
                return '标题长度3-100位';
            }
        },
        keyword: function (value) {
            if (value.length <= 0) {
                element.tabChange('document-tab', 'document');
                return '请输入META关键词';
            }
            if (value.length < 6 || value.length > 255) {
                element.tabChange('document-tab', 'document');
                return 'META关键词长度6-255位字符';
            }

        },

        description: function (value) {
            if (value.length <= 0) {
                element.tabChange('document-tab', 'document');
                return '请输入META描述';
            }
            if (value.length < 6 || value.length > 255) {
                element.tabChange('document-tab', 'document');
                return 'META描述长度6-255位字符';
            }

        },
        author: function (value) {
            if (value.length <= 0) {
                element.tabChange('document-tab', 'editor');
                return '请输入作者';
            }
        },
        published_at: function (value) {
            if (value.length <= 0) {
                element.tabChange('document-tab', 'editor');
                return '请选择发布时间';
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


    common.lay_upload('#upload-attach', false, function (res, index, item) {
        var container = item.siblings('.layui-upload-list');
        if (res.code === 0 && res.error_code === 0) {
            item.parents('.layui-form-item').find('input[name=attach_file]').val(res.data.url);
             item.parents('.layui-form-item').find('input[name=attach_name]').val(res.data.original_name);
            container.html('<div class="upload-thumb-img">附件:<a href="javascript:;" lay-tips="单击删除">' + res.data.original_name + '</a></div>')
        } else {
            container.find('#lay-' + index).find('span').remove();
            container.find('#lay-' + index).append('<span><i class="layui-icon layui-icon-close-fill" style="font-size: 30px; color: #FF5722;"></i>  </span>');
            return layer.msg(res.msg, {icon: 2, time: 1000});
        }
    });
     //删除附件
     $(".layui-form").on('click', '.upload-thumb-img>a', function () {
        common.active['re_upload_attach'].call(this)
    });

    datagrid.lay_datetime('.lay_datetime');
    //修复form的高度
    $("form.ui-form").css('height',$(document).height()+'px');

    $("textarea.ui-textarea").keyup(function(){
		var curLength=$(this).val().length;
		if(200-curLength>=0) {
		    $(this).parents('.layui-form-item').find('span').text(200-$(this).val().length);
        }else{
		    var num=$(this).val().substr(0,200);
			$(this).val(num);
			layer.msg("超过字数限制，多出的字将被截断！" );
        }
	})

});