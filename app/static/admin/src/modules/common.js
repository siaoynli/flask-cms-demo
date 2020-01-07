layui.define(["form", 'upload', "toastr", "webuploader", 'croppers'], function (exports) {
    var $ = layui.$,
        toastr = layui.toastr,
        layer = layui.layer,
        object = (layui.laytpl, layui.setter, layui.view, layui.admin),
        form = layui.form,
        upload = layui.upload,
        croppers = layui.croppers,
        webuploader = layui.webuploader;

    var formEvent = function (filter_name) {
        form.on('submit(' + filter_name + ')', function (form) {
            var me = $(this);
            object.req({
                url: me.parents(".layui-form").attr('action'),
                type: "post",
                beforeSend: function (xhr, settings) {
                    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf-token]').attr('content'))
                    }
                    layer.load();
                },
                data: form.field,
                done: function (e) {
                    layer.closeAll('loading');
                    if (e.error_code === 0) {
                        toastr.success(e.msg);
                        setTimeout(function () {
                            window.location.reload();
                        }, 1000);
                    } else {
                        toastr.error(e.msg);
                    }
                }
            });
            return false;
        });
    };

    //普通上传
    var web_upload = function (btnId, is_multi, func) {
        var title, exts, mimeTypes;
        var id = btnId;
        var file_type = 'images';
        var btn = $(btnId);
        var container = btn.siblings('.layui-upload-list');
        var multiple = is_multi;
        var csrf_token = $('meta[name=csrf-token]').attr('content');

        if (typeof(btn.attr('upload-type')) !== "undefined") {
            file_type = btn.attr('upload-type');
        }

        //类型  image  avatar  media  attach
        if (file_type === 'media') {
            title = 'Videos';
            exts = 'mp4,mkv,flv,avi,vob,mov,mpg';
            mimeTypes = 'video/*'
        } else if (file_type === 'attach') {
            title = 'application';
            exts = 'pdf,doc,zip,rar,rtf,txt,docx';
            mimeTypes = 'application/msword,application/pdf,application/zip,application/csv'
        } else {
            title = 'Images';
            exts = 'gif,jpg,jpeg,bmp,png';
            mimeTypes = 'image/*'
        }

        var uploader = webuploader.create({
            // 选完文件后，是否自动上传。
            auto: true,
            // swf文件路径
            swf: '/static/js/webuploader/Uploader.swf',
            runtimeOrder: 'html5,flash',
            // 文件接收服务端。
            server: $(btn).attr('upload-url'),
            pick: {
                id: id,
                multiple: multiple,
            },
            threads: 1,
            prepareNextFile: true,
            resize: false,
            compress: false,
            duplicate: true,
            formData: {csrf_token: csrf_token, file_type: file_type},
            fileNumLimit: 10,
            accept: {
                title: title,
                extensions: exts,
                mimeTypes: mimeTypes
            }
        });

        uploader.on('beforeFileQueued', function (file) {
            if (multiple === false) {
                container.html('');
            }
        });

        uploader.on('fileQueued', function (file) {
            if (file_type === 'images') {
                var $li = $(
                    '<div id="' + file.id + '" class="item">' +
                    '<div class="pic-box"><img src=""></div>' +
                    '<p class="state" ><i class="fa fa-arrow-up"></i></p>' +
                    '</div>'
                ), $img = $li.find('img');
                uploader.makeThumb(file, function (error, src) {
                    if (error) {
                        $img.replaceWith('<span>不能预览</span>');
                        return;
                    }
                    $img.attr('src', src);
                }, 100, 100);
            } else {
                var $li = $(
                    '<div id="' + file.id + '" class="item">' +
                    '<div class="note">正在计算文件特征...</div>' +
                    '<div class="pic-box"><img src="/static/images/' + file_type + '.jpg"></div>' +
                    '<p class="state" ><i class="fa fa-arrow-up"></i></p>' +
                    '</div>'
                );
            }
            container.show().append($li);
        });

        uploader.on('uploadProgress', function (file, percentage) {

            var $li = container.find(file.id),
                $percent = $li.find('.progress .progress-bar');
            // 避免重复创建
            if (!$percent.length) {
                $percent = $('<div class="progress progress-striped active">' +
                    '<div class="progress-bar" role="progressbar" style="width: 0%">' +
                    '</div>' +
                    '</div>').appendTo($li).find('.progress-bar');
            }
            $li.find('p.state').attr('title', '正在上传').html(parseInt(percentage * 100) + '%');
            $percent.css('width', percentage * 100 + '%');
        });

        uploader.on('uploadSuccess', function (file, response) {
            func(file, response);
        });

        // 文件上传失败，显示上传出错。
        uploader.on('uploadError', function (file) {
            $('#' + file.id).find('p.state').removeClass('state').attr('title', '上传失败').html('<i class="layui-icon layui-icon-face-cry" style="font-size: 30px; color: #FF5722;"></i>');
            toastr.error('文件上传失败');
        });

        // 完成上传完了，成功或者失败，先删除进度条。
        uploader.on('uploadComplete', function (file) {
            $('#' + file.id).find('.progress').fadeOut();
            if (multiple) {
                $('#' + file.id).find('p.state').removeClass('state').attr('title', '上传成功').html('<i class="layui-icon layui-icon-ok-circle" style="font-size: 40px; color: #ffffff;"></i>');
            } else {
                $('#' + file.id).find('p.state').hide();
            }
            uploader.reset();
        });

        uploader.on("error", function (type, handler) {
            if (type === "Q_TYPE_DENIED") {
                toastr.error('上传文件格式不符合要求');
            } else if (type === "F_EXCEED_SIZE") {
                toastr.error('上传文件超过限制');
            }
        });


    };

    //分片上传,断点续传，秒传
    var web_chunk_upload = function (btnId, is_multi, func) {
        var title, exts, mimeTypes;
        var id = btnId;
        var file_type = 'images';
        var btn = $(btnId);
        var container = btn.siblings('.layui-upload-list');
        var chunk_size = 10 * 1024 * 1024;
        var multiple = is_multi;
        var csrf_token = $('meta[name=csrf-token]').attr('content');


        if (typeof(btn.attr('upload-type')) !== "undefined") {
            file_type = btn.attr('upload-type');
        }

        //类型  image  avatar  media  attach
        if (file_type === 'media') {
            title = 'Videos';
            exts = 'mp4,mkv,flv,avi,vob,mov,mpg';
            mimeTypes = 'video/*'
        } else if (file_type === 'attach') {
            title = 'application';
            exts = 'pdf,doc,zip,rar,rtf,txt,docx';
            mimeTypes = 'application/msword,application/pdf,application/zip,application/csv'
        } else {
            title = 'Images';
            exts = 'gif,jpg,jpeg,bmp,png';
            mimeTypes = 'image/*'
        }

        //注册功能一定要写在前头，否则不会生效
        webuploader.Uploader.register({
            'before-send-file': 'beforeSendFile'
            , "before-send": "beforeSend"
            , "after-send-file": "afterSendFile"
        }, {
            beforeSendFile: function (file) {
                var owner = this.owner,
                    server = this.options.server,
                    deferred = webuploader.Deferred(),
                    obj = container.find(' #' + file.id);
                owner.md5File(file.source).fail(function () {
                    deferred.reject();
                }).progress(function (percentage) {
                    obj.find('.note').text('读取文件进度' + parseInt(percentage * 100) + "%");
                }).then(function (md5Value) {
                    obj.find('.note').text('文件验证完毕...');
                    file.wholeMd5 = md5Value;
                    $.ajax(server, {
                        dataType: 'json',
                        type: 'post',
                        data: {
                            action: "md5check",
                            csrf_token: csrf_token,
                            unique: md5Value
                        },
                        cache: false,
                        timeout: 1000,//todo 超时的话，只能认为该文件不曾上传过
                    }).then(function (response, textStatus, jqXHR) {
                        if (response.code === 0) {
                            if (response.data.is_file_exist) {
                                deferred.reject();
                                owner.skipFile(file);
                                obj.find('.note').remove();
                                obj.find('p.state').attr('title', '正在上传').html('100%');
                                file.unique_file_name = md5Value;
                                func(file, response);
                            } else {
                                deferred.resolve();
                                file.unique_file_name = md5Value;
                            }
                        } else {
                            deferred.resolve();
                            file.unique_file_name = md5Value;
                        }

                    }, function (jqXHR, textStatus, errorThrown) {
                        //任何形式的验证失败，都触发重新上传
                        deferred.resolve();
                    });

                });

                return deferred.promise();
            }, beforeSend: function (block) {
                //分片验证是否已传过，用于断点续传
                var deferred = webuploader.Deferred();
                var server = this.options.server;
                $.ajax({
                    type: "POST"
                    , url: server
                    , data: {
                        action: "chunk"
                        , csrf_token: csrf_token
                        , unique_file_name: block.file.unique_file_name
                        , chunk_index: block.chunk
                        , ext: block.file.ext
                        , size: block.end - block.start
                    }
                    , cache: false
                    //todo 超时的话，只能认为该文件不曾上传过
                    , timeout: 1000
                    , dataType: "json"
                }).then(function (response, textStatus, jqXHR) {

                    if (response.code === 0) {
                        if (response.data.is_file_exist) {
                            deferred.reject();
                        } else {
                            deferred.resolve();
                        }
                    } else {
                        //重新上传
                        deferred.resolve();
                    }

                }, function () {
                    //任何形式的验证失败，都触发重新上传
                    deferred.resolve();
                });

                return deferred.promise();
            }, afterSendFile: function (file) {
                var chunks_total = 0;
                if ((chunks_total = Math.ceil(file.size / chunk_size)) >= 1) {
                    var deferred = webuploader.Deferred();
                    var server = this.options.server;
                    $.ajax({
                        type: "POST"
                        , url: server
                        , data: {
                            action: "merge"
                            , csrf_token: csrf_token
                            , unique_file_name: file.unique_file_name
                            , chunks: chunks_total
                            , original_name: file.source.name
                            , ext: file.ext
                            , size: file.size
                            , file_type: file_type
                        }
                        , cache: false
                        , dataType: "json"
                    }).then(function (response, textStatus, jqXHR) {
                        deferred.resolve();
                        func(file, response, btn);
                    }, function () {
                        deferred.reject();
                    });
                    return deferred.promise();
                } else {
                    toastr.error('文件有误，上传失败');
                }
            }
        });


        var uploader = webuploader.create({
            // 选完文件后，是否自动上传。
            auto: true,
            // swf文件路径
            swf: '/static/js/webuploader/Uploader.swf',
            runtimeOrder: 'html5,flash',
            // 文件接收服务端。
            server: $(btn).attr('upload-url'),
            pick: {
                id: id,
                multiple: multiple,
            },
            threads: 1,
            prepareNextFile: true,
            resize: false,
            compress: false,
            duplicate: true,
            chunked: true,
            chunkSize: chunk_size,
            // formData: {guid: GUID},
            fileNumLimit: 10,
            // fileSingleSizeLimit:2*1024*1024*1024,
            accept: {
                title: title,
                extensions: exts,
                mimeTypes: mimeTypes
            }
        });

        uploader.on('beforeFileQueued', function (file) {
            if (multiple === false) {
                container.html('');
            }
        });

        uploader.on('fileQueued', function (file) {

            if (file_type === 'images') {
                var $li = $(
                    '<div id="' + file.id + '" class="item">' +
                    '<div class="pic-box"><img src=""></div>' +
                    '<p class="state" ><i class="fa fa-arrow-up"></i></p>' +
                    '</div>'
                ), $img = $li.find('img');
                uploader.makeThumb(file, function (error, src) {
                    if (error) {
                        $img.replaceWith('<span>不能预览</span>');
                        return;
                    }
                    $img.attr('src', src);
                }, 100, 100);
            } else {
                var $li = $(
                    '<div id="' + file.id + '" class="item">' +
                    '<div class="note">正在计算文件特征...</div>' +
                    '<div class="pic-box"><img src="/static/images/' + file_type + '.jpg"></div>' +
                    '<p class="state" ><i class="fa fa-arrow-up"></i></p>' +
                    '</div>'
                );
            }

            container.show().append($li);

        });

        uploader.on('uploadBeforeSend', function (block, data) {
            // block为分块数据。
            // file为分块对应的file对象。
            // var file = block.file;
            // var fileMd5 = file.wholeMd5;
            // 修改data可以控制发送哪些携带数据。
            // console.info("fileName= " + file.name + " fileMd5= " + fileMd5 + " fileId= " + file.id);
            // 将存在file对象中的md5数据携带发送过去。
            data.md5value = block.file.wholeMd5;//md5
            //唯一标识符，用作断点续传
            data.unique_file_name = block.file.unique_file_name;
            data.csrf_token = csrf_token;
            data.file_type = file_type;

            if (block.chunks > 1) {
                data.is_chunked = true;
            } else {
                data.is_chunked = false;
            }

        });

        uploader.on('startUpload', function () {

        });

        uploader.on('uploadProgress', function (file, percentage) {

            var $li = container.find(' #' + file.id),
                $percent = $li.find('.progress .progress-bar');
            // 避免重复创建
            if (!$percent.length) {
                $percent = $('<div class="progress progress-striped active">' +
                    '<div class="progress-bar" role="progressbar" style="width: 0%">' +
                    '</div>' +
                    '</div>').appendTo($li).find('.progress-bar');
            }
            $li.find(".note").remove();
            $li.find('p.state').show().attr('title', '正在上传').html(parseInt(percentage * 100) + '%');
            $percent.css('width', percentage * 100 + '%');
        });

        uploader.on('uploadError', function (file) {
            $('#' + file.id).find('p.state').removeClass('state').attr('title', '上传失败').html('<i class="layui-icon layui-icon-face-cry" style="font-size: 30px; color: #FF5722;"></i>');
            toastr.error('文件上传失败');
        });


        uploader.on('uploadSuccess', function (file, response) {

        });


        uploader.on('uploadComplete', function (file) {
            $('#' + file.id).find('.progress').fadeOut();
            if (multiple) {
                $('#' + file.id).find('p.state').removeClass('state').attr('title', '上传成功').html('<i class="layui-icon layui-icon-ok-circle" style="font-size: 40px; color: #ffffff;"></i>');
            } else {
                $('#' + file.id).find('p.state').hide();
            }
            uploader.reset();
        });

        uploader.on("error", function (type, handler) {
            if (type === "Q_TYPE_DENIED") {
                toastr.error('上传文件格式不符合要求');
            } else if (type === "F_EXCEED_SIZE") {
                toastr.error('上传文件超过限制');
            }
        });


    };

    //layui 上传组件上传
    var lay_upload = function (btn, is_multi, func) {

        var container, url;
        var file_type = 'images';
        var accept = 'file';
        var exts = 'jpg|png|jpeg|gif';
        var size = 1024 * 100;
        var multiple = is_multi;
        var files;

        if (typeof($(btn).attr('upload-type')) !== "undefined") {
            file_type = $(btn).attr('upload-type');
        }

        if (file_type === 'images') {
            accept = 'file';
            exts = 'jpg|png|jpeg|gif';
            size = 1024 * 20;
        }


        if (file_type === 'attach') {
            accept = 'file';
            exts = 'zip|rar|pdf|doc';
            size = 1024 * 1024 * 10;
        }


        if (file_type === 'media') {
            accept = 'video';
            exts = 'mp4|mkv|avi|flv';
            size = 1024 * 1024 * 200;
        }

        var uploader = upload.render({
            elem: btn
            , url: url
            , accept: accept
            , exts: exts
            , size: size
            , multiple: multiple
            , data: {'csrf_token': $('meta[name=csrf-token]').attr('content'), 'file_type': file_type}
            , choose: function (obj) {
                this.url = this.item.attr('upload-url');
                container = this.item.siblings('.layui-upload-list');
                files = obj.pushFile();
                container.html('').show();
                obj.preview(function (index, file, result) {
                    if (file_type === 'images') {
                        result = result
                    } else {
                        result = '/static/images/' + file_type + '.jpg';
                    }
                    container.append('<div class="upload-thumb-list" id="lay-' + index + '"><span><i class="layui-icon layui-icon-loading layui-icon layui-anim layui-anim-rotate layui-anim-loop"></i></span><img src="' + result + '" alt="' + file.name + '" class="layui-upload-images"></div>')
                });

            }
            , before: function (obj) {

            }
            , done: function (res, index, upload) {
                if (multiple) {
                    container.find('#lay-' + index).remove();
                }
                func(res, index, this.item);
                //删除已经上传的图片对象
                delete files[index];
            }
            , allDone: function (obj) {

            }
            , error: function (index, upload) {
                container.find('#lay-' + index).find('span').remove();
                container.find('#lay-' + index).append('<span><i class="layui-icon layui-icon-close-fill" style="font-size: 30px; color: #FF5722;"></i>  </span>');
            }
        });


    };


    var image_croppers = function (btn, width, height,ratio, func) {
        croppers.render({
            elem: btn
            , saveW: width     //保存宽度
            , saveH: height
            , aspectRatio: ratio   //选取比例
            , area: '900px'  //弹窗宽度
            , url: $(btn).attr('upload-url')  //图片上传接口返回和（layui 的upload 模块）返回的JOSN一样
            , done: function (result,item) { //上传完毕回调
                func(result,item);
            }
        });
    };

    var active = {
        re_upload_img: function (is_avatar) {
            is_avatar = is_avatar || false;
            var me = $(this);
            if (me.attr('src') === "/static/admin/images/guest.png") return;

            layer.confirm('删除这张图片么？', {
                btn: ['是', '否'],
                icon: 3,
                title: '提示'
            }, function (index) {
                layer.close(index);
                if (is_avatar === false) {
                    me.parents('.layui-form-item').find('input').val('');
                    me.remove();
                } else {
                    var img = "/static/admin/images/guest.png";
                    me.parents('.layui-form-item').find('input.input-upload').val(img);
                    me.attr('src', img).removeAttr('lay-tips');
                }
            });
        },

    };


    exports("common", {formEvent, active, lay_upload, web_chunk_upload, web_upload,image_croppers})
});