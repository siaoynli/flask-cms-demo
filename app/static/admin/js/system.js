layui.config({
    base: '/static/admin/src/',
}).use(['index', 'form', 'element', 'common'], function () {
    var $ = layui.$,
        form = layui.form,
        element = layui.element,
        common = layui.common;

    form.verify({
        site_name: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'basic');
                return '请输入网站名称';
            }
            if (value.length > 100) {
                element.tabChange('system-tab', 'basic');
                return '网站名称长度不能大于100位字符';
            }

        },
        title: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'basic');
                return '请输入网站标题';
            }
            if (value.length > 100) {
                element.tabChange('system-tab', 'basic');
                return '网站标题长度不能大于100位字符';
            }

        },
        keyword: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'basic');
                return '请输入META关键词';
            }
            if (value.length < 6 || value.length > 255) {
                element.tabChange('system-tab', 'basic');
                return 'META关键词长度6-255位字符';
            }

        },

        description: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'basic');
                return '请输入META描述';
            }
            if (value.length < 6 || value.length > 255) {
                element.tabChange('system-tab', 'basic');
                return 'META描述长度6-255位字符';
            }

        },
        upload_path: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'upload');
                return '请输入上传路径';
            }

        },
        txt_water: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'upload');
                return '请输入水印文字';
            }
            if (value.length > 100) {
                element.tabChange('system-tab', 'upload');
                return '水印文字最大长度100位';
            }

        },
        txt_water_size: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'upload');
                return '请输入水印文字大小';
            }
            if (!/^\d+$/.test(value)) {
                return '水印文字为数字';
            }

        },
        txt_water_font: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'upload');
                return '请输入水印字体路径';
            }


        },
        txt_water_color: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'upload');
                return '请输入水印文字颜色';
            }

        },
        images_size: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'upload');
                return '请输入图片大小';
            }
            if (!/^\d+$/.test(value)) {
                return '图片大小为数字';
            }

        },
        images_extensions: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'upload');
                return '请输入图片类型';
            }
            if (value.length > 100) {
                element.tabChange('system-tab', 'upload');
                return '图片类型长度不能大于100位字符';
            }

        },
        images_max_width: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'upload');
                return '请输入图片最大宽度';
            }
            if (!/^\d+$/.test(value)) {
                return '图片最大宽度为数字';
            }

        },
        images_max_height: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'upload');
                return '请输入图片最大高度';
            }
            if (!/^\d+$/.test(value)) {
                return '图片最大高度为数字';
            }

        },
        media_size: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'upload');
                return '请输入媒体大小';
            }
            if (!/^\d+$/.test(value)) {
                return '媒体大小为数字';
            }

        },
        media_extensions: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'upload');
                return '请输入媒体类型';
            }
            if (value.length > 100) {
                element.tabChange('system-tab', 'upload');
                return '媒体类型长度不能大于100位字符';
            }

        },
        attach_size: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'upload');
                return '请输入附件大小';
            }
            if (!/^\d+$/.test(value)) {
                return '附件大小为数字';
            }

        },
        attach_extensions: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'upload');
                return '请输入附件类型';
            }
            if (value.length > 100) {
                element.tabChange('system-tab', 'upload');
                return '附件类型长度不能大于100位字符';
            }

        },
        comment_time_interval: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'comment');
                return '请输入评论时间间隔';
            }
            if (!/^\d+$/.test(value)) {
                return '评论时间间隔为数字';
            }

        }, admin_prefix: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'other');
                return '请输入后台管理地址';
            }
            if (value.length > 100) {
                element.tabChange('system-tab', 'other');
                return '后台管理地址长度不能大于100位字符';
            }

        }, cache_time: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'other');
                return '请输入缓存时间';
            }
            if (!/^\d+$/.test(value)) {
                return '缓存时间为数字';
            }

        }, pagination_number: function (value) {
            if (value.length <= 0) {
                element.tabChange('system-tab', 'other');
                return '请输入内容分页大小';
            }
            if (!/^\d+$/.test(value)) {
                return '内容分页大小为数字';
            }

        }
    });
    common.formEvent('setSystem');
});