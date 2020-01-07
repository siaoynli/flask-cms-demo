layui.config({
    base: '/static/admin/src/',
}).use(['index', 'datagrid'], function () {

    var $ = layui.$,
        datagrid = layui.datagrid,
        active = datagrid.active;


    var  grid_id_filter = "LAY-app-content-list";


    var config = [
        {checkbox: true, fixed: true}
        , {field: 'title', title: '标签'}
        , {
            field: 'type', width: 120, align: 'center', title: '类型', templet: function (d) {
                if (d.type === 'document') {
                    return '<i class="layui-icon layui-icon-file-b" title="文章"></i>';
                } else if (d.type === 'video') {
                    return  '<i class="layui-icon layui-icon-video" title="视频"></i>';
                } else if (d.type === 'video') {
                    return  '<i class="layui-icon layui-icon-picture" title="图片"></i>';
                } else{
                    return '-';
                }
            }
        }

        , {title: '操作', width: 140, align: 'center', toolbar: '#action_menu', fixed: 'right', unresize: true,}
    ];


    datagrid.render(grid_id_filter, config);

    datagrid.tableEvent(grid_id_filter);


});