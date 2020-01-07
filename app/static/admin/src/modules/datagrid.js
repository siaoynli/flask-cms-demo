layui.define(["table", "toastr", "laydate"], function (exports) {
    var $ = layui.$,
        toastr = layui.toastr,
        layer = layui.layer,
        object = (layui.laytpl, layui.setter, layui.view, layui.admin),
        table = layui.table,
        laydate = layui.laydate,
        tableIns = '',
        iframe_height = 0;

    var render = function (grid_id_filter, config, fn) {
        tableIns = table.render({
            elem: '#' + grid_id_filter
            , url: $('#' + grid_id_filter).attr('data-url') + '/lists'
            , cellMinWidth: 60
            , cols: [config]
            , page: true
            , even: true //开启隔行背景
            , limit: 20
            , toolbar: '#toolbar'
            , defaultToolbar: ['filter', 'print']
            , text: {
                none: '-' //默认：无数据。
            }
            , limits: [20, 30, 40, 50, 60]
            , height: 'full-105'
            , done: function (res, curr, count) {
                if (fn) {
                    fn(res, curr, count);
                }
            }
        });
    };


    var renderNoPage = function (grid_id_filter, config, fn) {
        tableIns = table.render({
            elem: '#' + grid_id_filter
            , url: $('#' + grid_id_filter).attr('data-url') + '/lists'
            , cellMinWidth: 60
            , cols: [config]
            , toolbar: '#toolbar'
            , defaultToolbar: ['filter', 'print']
            , text: {
                none: '-' //默认：无数据。
            }
            , even: true //开启隔行背景
            , height: 'full-105'
            , done: function (res, curr, count) {
                if (fn) {
                    fn(res, curr, count);
                }
            }
        });
    };

    // 修改table的某一行数据
    var tableEvent = function (grid_id_filter) {
            var filter = $('#' + grid_id_filter), btn_group = filter.parents('.layui-card-body').find('.layui-btn-group');
            //注：edit是固定事件名，grid_id_filter是 lay-filter="对应的值"
            table.on('tool(' + grid_id_filter + ')', function (obj) {
                var form = obj.data;
                var event = obj.event;
                switch (event) {
                    case 'edit':
                        dialog($(this), btn_group, filter.attr('data-url') + '/' + form.id + '/edit');
                        break;
                    case 'del':
                        delelte(grid_id_filter, '确定删除这条记录么', form.id, obj);
                        break;
                    case 'reply':

                        dialog($(this), btn_group, filter.attr('data-url') + '/' + form.id + '/reply');
                        break;
                    default:
                        layer.msg('未知操作!');
                }
            });

            table.on('toolbar(' + grid_id_filter + ')', function (obj) {
                var event = obj.event;
                var checkStatus = table.checkStatus(grid_id_filter);
                var me = $(this);
                switch (event) {
                    case 'create':
                        var btn_group = me.parents('.layui-btn-group');
                        dialog(me, btn_group, filter.attr('data-url') + '/create');
                        break;
                    case 'modify':
                        if (checkStatus.data.length === 0) {
                            toastr.error('没有选中任何记录！');
                            return false;
                        }
                        if (checkStatus.data.length > 1) {
                            toastr.error('不能同时编辑两条及以上记录！');
                            return false;
                        }
                        id = checkStatus.data[0].id;
                        var obj = me.parents('.layui-btn-group');
                        dialog(me, obj, filter.attr('data-url') + '/' + id + '/edit');
                        break;
                    case 'remove':
                        var ids = [], title = '';
                        if (checkStatus.data.length === 0) {
                            toastr.error('没有选中任何记录！');
                            return false;
                        }
                        for (var i = 0; i < checkStatus.data.length; i++) {
                            ids.push(checkStatus.data[i].id)
                        }
                        if (checkStatus.data.length === 1) {
                            title = "确定删除这条记录么"
                        } else {
                            title = "确定删除这些记录么"
                        }
                        delelte(grid_id_filter, title, ids.join('-'));
                        break;
                    case 'search':
                        var keyword = filter.parents('.layui-card-body').find('input[name=keyword]');
                        var note = filter.parents('.layui-card-body').find('.layui-elem-quote');
                        var data = keyword.val(), height = "full-105";
                        if (data) {
                            note.removeClass('layui-hide').html('关键字:&nbsp;&nbsp;<cite  style="font-size: 14px; color: #FF5722;">' + data + '</cite>&nbsp;&nbsp;的搜索结果');
                            height = "full-170";
                        } else {
                            note.addClass('layui-hide').html("");
                        }
                        tableIns = table.render({
                            elem: '#' + grid_id_filter
                            , url: filter.attr('data-url') + '/lists'
                            , cellMinWidth: 60
                            , cols: tableIns.config.cols
                            , where: {
                                keyword: data
                            }
                            , toolbar: '#toolbar'
                            , defaultToolbar: ['filter', 'print']
                            , text: {
                                none: '-' //默认：无数据。
                            }
                            , even: true //开启隔行背景
                            , height: height
                            , done: function (res, curr, count) {

                            }
                        });
                        break;
                    case 'reload':
                        tableIns.reload();
                        break;
                    case 'export':
                        layer.msg('export');
                        break;
                    case 'reflash':
                        window.location.reload();
                        break;
                    case 'show':
                        if (checkStatus.data.length === 0) {
                            toastr.error('没有选中任何记录！');
                            return false;
                        }
                        if (checkStatus.data.length > 1) {
                            toastr.error('不能同时查看两条及以上记录！');
                            return false;
                        }
                        id = checkStatus.data[0].id;

                        var note = filter.parents('.layui-card-body').find('.layui-elem-quote');

                        note.removeClass('layui-hide').html('回复 ' + checkStatus.data[0].username + ':<cite  style="font-size: 14px; color: #FF5722;">' + checkStatus.data[0].content + '</cite>&nbsp;&nbsp;的所有留言');

                        tableIns = table.render({
                            elem: '#' + grid_id_filter
                            , url: filter.attr('data-url') + '/lists'
                            , cellMinWidth: 60
                            , cols: tableIns.config.cols
                            , where: {
                                id: id,
                            }
                            , toolbar: '#toolbar'
                            , defaultToolbar: ['filter', 'print']
                            , text: {
                                none: '-' //默认：无数据。
                            }
                            , even: true //开启隔行背景
                            , height: 'full-170'
                            , done: function (res, curr, count) {

                            }
                        });
                        break;
                    case 'LAYTABLE_COLS':
                        return;
                    case 'LAYTABLE_EXPORT':
                        return;
                    case 'LAYTABLE_PRINT':
                        return;
                    default:
                        layer.msg('没有这个方法！');
                }

            });


            table.on('sort(' + grid_id_filter + ')', function (obj) {
                //尽管我们的 table 自带排序功能，但并没有请求服务端。
                //有些时候，你可能需要根据当前排序的字段，重新向服务端发送请求，从而实现服务端排序，如：
                table.reload(grid_id_filter, {
                    initSort: obj //记录初始排序，如果不设的话，将无法标记表头的排序状态。 layui 2.1.1 新增参数
                    , where: { //请求参数（注意：这里面的参数可任意定义，并非下面固定的格式）
                        field: obj.field //排序字段
                        , order: obj.type //排序方式
                    }
                });
            });

            table.on('edit(' + grid_id_filter + ')', function (obj) {
                //注：edit是固定事件名，grid_id_filter是 lay-filter="对应的值"
                //  obj.data //得到所在行所有键值
                var value = obj.value //得到修改后的值
                    , field = obj.field, filter = $('#' + grid_id_filter); //得到字段
                var url = filter.attr('data-url');
                var data = {};
                data[field] = value;
                //做一个标识
                data['edit_one_field'] = 1;
                data['id'] = obj.data.id;
                editOneLine(grid_id_filter, url + '/' + obj.data.id, data, obj);
            });
        }
    ;


    var delelte = function (grid_id_filter, title, ids, obj) {
        obj = obj || '';
        layer.confirm(title, {
            btn: ['是', '否'],
            icon: 3,
            title: '提示'
        }, function (index) {
            layer.close(index);
            object.req({
                url: $('#' + grid_id_filter).attr('data-url') + '/' + ids,
                type: "delete",
                beforeSend: function (xhr, settings) {
                    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf-token]').attr('content'))
                    }
                    layer.load();
                },
                data: '',
                done: function (e) {
                    layer.closeAll('loading');
                    if (e.error_code === 0) {
                        toastr.success(e.msg);
                        table.reload(grid_id_filter);
                        if (obj) {
                            obj.del();
                        }
                    } else {
                        toastr.error(e.msg);
                    }
                }
            });
        });
    };

    var dialog = function (me, btn_group, url) {
        var maxmin = true;
        var content = [url];
        if (btn_group.hasClass("nomaxmin")) {
            maxmin = false;
            content = [url, 'no'];
        }
        var index = layer.open({
            type: 2
            , title: me.attr('title')
            , content: content
            , maxmin: false
            , resize: false
            , shadeClose: true
            , area: [btn_group.attr('width') + 'px', btn_group.attr('height') + 'px']
            , btn: ['确定', '取消']
            , yes: function (index, layero) {
                // var body = layer.getChildFrame('body', index);
                // var submit=$(body).find("#app-form-submit");
                var submit = layero.find('iframe').contents().find("#app-form-submit");
                submit.click();
            }, success(layero, index) {
                if (maxmin === false) {
                    var obj = $(layero).find('.layui-layer-content');
                    obj.css('position', 'relative');
                    obj.css('z-index', 198912345);
                    // obj.css('height', $(window).height() + 'px');
                    obj.css('overflow', 'hidden');

                    layer.iframeAuto(index);
                    var btn = obj.parents('.layui-layer').find('.layui-layer-btn');
                    btn.css('bottom', 0);
                    btn.css('right', 0);
                    btn.css('position', 'absolute');
                    btn.css('z-index', '198912346');
                    // layero.find('iframe').css('height', $(window).height() + 'px');
                }
            }
        });
        if (maxmin) {
            layer.full(index);
        }
    };


    var submit = function (data, grid_id_filter, url, method) {
        method = method || 'post';
        object.req({
            url: url,
            type: method,
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf-token]').attr('content'))
                }
                layer.load();
            },
            data: $(data.form).serialize(),
            done: function (e) {
                layer.closeAll('loading');
                if (e.error_code === 0) {
                    var index = parent.layer.getFrameIndex(window.name);
                    parent.layer.close(index);
                    parent.layui.toastr.success(e.msg);
                    if (method === 'post') {
                        //如果class标志为nopage，表示不分页
                        if ($(window.parent.document).find('#' + grid_id_filter).hasClass("nopage")) {
                            parent.layui.table.reload(grid_id_filter);
                        } else {
                            //分页显示第一页
                            parent.layui.table.reload(grid_id_filter, {
                                page: {
                                    curr: 1
                                }
                            });
                        }
                    } else {
                        parent.layui.table.reload(grid_id_filter);
                    }

                } else {
                    // toastr.error(e.msg);
                    layer.msg(e.msg, {icon: 2, time: 1000});
                }
            }
        });
    };


    var editOneLine = function (grid_id_filter, url, data, obj, index) {
        obj = obj || '';
        index = index || '';
        object.req({
            url: url,
            type: "put",
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf-token]').attr('content'))
                }
            },
            data: data,
            done: function (e) {
                if (e.error_code != 0) {
                    if (index) {
                        layer.msg(e.msg, {icon: 2, time: 1000});
                    } else {
                        table.reload(grid_id_filter);
                        toastr.error(e.msg);
                    }

                } else {
                    if (obj) {
                        obj.update(data);
                    } else {
                        table.reload(grid_id_filter);
                    }
                    if (index) {
                        layer.close(index);
                    }
                }
            }
        });

    };

    var active = {
        save: function (data, grid_id_filter) {
            var url = $(window.parent.document).find('#' + grid_id_filter).attr('data-url');
            submit(data, grid_id_filter, url);
        },
        update: function (data, grid_id_filter) {
            var me = $(this);
            var id = me.parents('.layui-form').find('input[name=id]').val();
            var url = $(window.parent.document).find('#' + grid_id_filter).attr('data-url');
            submit(data, grid_id_filter, url + '/' + id, 'put');

        },
        checkbox: function (obj, grid_id_filter) {
            var url = $('#' + grid_id_filter).attr('data-url');
            var id = this.value;
            var value = obj.elem.checked ? 1 : 0;
            var field = this.name;

            var data = {};
            data[field] = value;
            //做一个标识
            data['edit_one_field'] = 1;
            data['id'] = id;
            editOneLine(grid_id_filter, url + '/' + id, data, obj);
        },
        chooseSelect: function () {
             //父级窗口还原
            var p = $(window.parent.document);
            p.find('.layui-layer-content').css('height', 'auto');
            p.find('iframe').css('height', iframe_height + 'px');
        }, dropSelect: function () {
            //弹窗 iframe 和 layui-layer-content 高度变高,以显示下拉
            var p = $(window.parent.document);
            var iframe_box=p.find('.layui-layer-iframe');
            var h=p.height()-iframe_box.offset().top-62;
            p.find('.layui-layer-content').css('height', h+'px');
            iframe_height = p.find('iframe').height();
            p.find('iframe').css('height', h+'px');
        }
    };

    var lay_date = function (elem) {
        var p = $(window.parent.document);
        lay(elem).each(function () {
            laydate.render({
                elem: this
                , trigger: 'click'
                , min: -365
                ,max:365,
                done: function(value, date, endDate){
                        if(p) {
                            //父级窗口还原
                            p.find('.layui-layer-content').css('height', 'auto');
                            p.find('iframe').css('height', iframe_height + 'px');
                        }
                  }
            });
        });

    };

    var lay_datetime = function (elem) {
        lay(elem).each(function () {
            laydate.render({
                elem: this
                , trigger: 'click'
                ,type: 'datetime'
                 , min: -365
                ,max:365
            });
        });

    };


    exports("datagrid", {render, renderNoPage, active, tableEvent,lay_date,lay_datetime})
})
;