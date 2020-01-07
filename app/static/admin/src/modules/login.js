layui.define(function(exports) {
    var $ = layui.jquery;

    var csrf_token = $('meta[name=csrf-token]').attr('content');
    var obj = $("form");
    var submit = obj.find('button.submit');
    var html = submit.html();
    var name = obj.find('input[name=name]');
    var password = obj.find('input[name=password]');
    var notice = obj.find('.ui-notice');
    var avatar = obj.find('.ui-avatar');
    var cache = '';
    var avatar_url = avatar.attr('data-url');
    var avatarImg = avatar.find('img');
    var old_img = avatarImg.attr('src');
    var me=login = {
        loginClick: function() {
            if (submit.hasClass('disabled')) return false;
            if (!this.checkForm()) return false;
            this.submitForm();
        },
        showErrorNotice: function(msg) {
            notice.css('opacity', 1).html('').show();
            $('<div class="alert alert-danger alert-dismissable"><button aria-hidden="true" data-dismiss="alert" class="close" type="button">×</button>' + msg + '</div>').appendTo(notice);
            notice.stop().animate({
                'opacity': 0
            }, 3000);
        },
        showSuccessNotice: function(msg) {
            notice.css('opacity', 1).html('').show();
            $('<div class="alert alert-success alert-dismissable"><button aria-hidden="true" data-dismiss="alert" class="close" type="button">×</button>' + msg + '</div>').appendTo(notice);
            notice.stop().animate({
                'opacity': 0
            }, 3000);
        },
        checkForm: function() {
            if (name.val() === '') {
                this.showErrorNotice('请输入用户名或邮箱');
                name.focus();
                return false;
            }
            if (password.val() === '') {
                this.showErrorNotice('请输入密码');
                password.focus();
                return false;
            }
            return true;
        },
        removeDisabled: function() {
            submit.html(html);
            submit.removeClass('disabled');
            name.removeAttr('disabled');
            password.removeAttr('disabled');
        },
        loading: function() {
            submit.addClass('disabled').html('');
            var ol = $('<ol class="ui-ball-fall"></ol>');
            $("<li></li><li></li><li></li>").appendTo(ol);
            ol.appendTo(submit);
        },
        submitForm: function() {
            $.ajax({
                url: obj.attr('action'),
                data: obj.serialize(),
                cache: false,
                type: 'post',
                dataType: "json",
                beforeSend: function(xhr, settings) {
                    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrf_token)
                    }
                    name.attr('disabled', 'disabled');
                    password.attr('disabled', 'disabled');
                    me.loading();
                },
                success: function(result) {
                    if (result.error_code === 0) {
                        me.showSuccessNotice(result.message);
                        setTimeout(function() {
                            window.location = result.redirect_to;
                        }, 500);
                        submit.html('<span>登录成功</span>');
                    } else {
                        me.removeDisabled();
                        me.showErrorNotice(result.message);
                    }
                },
                error: function(XmlHttpRequest) {
                    me.removeDisabled();
                    me.showErrorNotice('出现错误，请联系管理员');
                }
            });
        },
        blur: function() {
            if (name.val() === '' || cache === name.val()) return;
            $.ajax({
                url: avatar_url + name.val(),
                cache: false,
                type: 'get',
                dataType: "json",
                beforeSend: function(xhr, settings) {
                    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrf_token)
                    }
                },
                success: function(result) {
                    cache = name.val();
                    if (result.error_code === 0) {
                        let img = new Image();
                        let image = result.data.image;
                        img.src = image;
                        avatarImg.animate({
                            'opacity': 0
                        }, 200, function() {
                            if (img.complete) {
                                avatarImg.attr('src', image).animate({
                                    'opacity': 1
                                }, 200);
                            } else {
                                img.onload = function() {
                                    avatarImg.attr('src', image).animate({
                                        'opacity': 1
                                    }, 200);
                                }
                            }
                        });
                    } else {
                        if (avatarImg.attr('src') === old_img) {
                            avatarImg.attr('src', old_img);
                        } else {
                            avatarImg.animate({
                                'opacity': 0
                            }, 200, function() {
                                avatarImg.attr('src', old_img).animate({
                                    'opacity': 1
                                }, 200);
                            });
                        }
                    }
                },
                error: function() {
                    me.showErrorNotice('出现错误，请联系管理员');
                }
            });
        },
        avatarClick: function() {
            var username = avatar.attr('data-name');
            if (username === '') return;
            if (avatar.hasClass('show')) {
                obj.find('.ui-form-group').eq(0).slideDown();
                avatar.removeClass('show');
                avatar.find('em').remove();
            } else {
                obj.find('.ui-form-group').eq(0).slideUp();
                $("<em>" + username + "</em>").appendTo(avatar);
                name.val(username);
                avatar.addClass('show');
            }
        },
    };
    exports('login', login);
});