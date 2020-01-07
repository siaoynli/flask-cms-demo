layui.config({
    base: '/static/admin/src/',
}).extend({
    index: 'index',
}).use(['index', 'form', 'form', 'common'], function () {
    var $ = layui.$,
        layer = layui.layer,
        form = layui.form,
        common = layui.common;


    form.verify({
        avatar: function (value, item) {
            if (value.length <= 0) {
                return '请上传头像';
            }
        },

    });

    //删除上传的单图
    $(".layui-form").on('click', '.upload-thumb-img>img', function () {
        common.active['re_upload_img'].call(this, true)
    });


    common.image_croppers('#upload-avatar',250,250,1,function(res,item){
        var container = item.siblings('.layui-upload-list');
        if (res.code === 0 && res.error_code === 0) {
            item.parents('.layui-form-item').find('input.input-upload').val(res.data.url);
            container.html('<div class="upload-thumb-img"><img src="' + res.data.url + '" lay-tips="单击删除"></div>')
        } else {
            return layer.msg(res.msg, {icon: 2, time: 1000});
        }

    });

    common.formEvent('setavatar');

        // common.lay_upload('#upload-avatar', false, function (res, index, item) {
    //     var container = item.siblings('.layui-upload-list');
    //     if (res.code === 0 && res.error_code === 0) {
    //         item.parents('.layui-form-item').find('input.input-upload').val(res.data.url);
    //         container.html('<div class="upload-thumb-img"><img src="' + res.data.url + '" lay-tips="单击删除"></div>')
    //     } else {
    //         container.find('#lay-' + index).find('span').remove();
    //         container.find('#lay-' + index).append('<span><i class="layui-icon layui-icon-close-fill" style="font-size: 30px; color: #FF5722;"></i>  </span>');
    //         return layer.msg(res.msg, {icon: 2, time: 1000});
    //     }
    //
    // });

    //上传附件实例
    // common.lay_upload('#upload-attach', false, function (res, index, item) {
    //     var container = item.siblings('.layui-upload-list');
    //     if (res.code === 0 && res.error_code === 0) {
    //     } else {
    //         return layer.msg(res.msg, {icon: 2, time: 1000});
    //     }
    // });

    //上传视频实例
    // common.web_chunk_upload('#upload-video', false, function (file, res, item) {
    //     var container = item.siblings('.layui-upload-list');
    //     if (res.code === 0 && res.error_code === 0) {
    //         //container.find(' #' + file.id)
    //         item.parents('.layui-form-item').find('input.input-upload').val(res.data.url);
    //     } else {
    //         $('#' + file.id).find('p.state').removeClass('state').attr('title', '上传失败').html('<i class="layui-icon layui-icon-face-cry" style="font-size: 30px; color: #FF5722;"></i>');
    //         return layer.msg(res.msg, {icon: 2, time: 1000});
    //     }
    // });


});