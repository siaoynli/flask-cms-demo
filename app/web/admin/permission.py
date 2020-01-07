"""
created  by  hzwlxy  at 2018/7/11 10:17
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import render_template, request


__author__ = '西瓜哥'

from app.web import admin_app as app
from app.models.permission import Permission
from app.libs.datagrid_response import LayuiResponse
from app.libs.layui_response import Success, Fail
from app.forms.permission import PermissionCreateForm, PermissionEditForm, PermissionEditOneKeyForm
from app.models.menu import Menu


@app.route('/permission', methods=['GET'])
def permission_index():
    return render_template('admin/permission/index.html')


@app.route('/permission/lists', methods=['GET'])
def permission_lists():
    total, result = Permission.get_limit_all()
    return LayuiResponse(data=result, count=total)


@app.route('/permission/create', methods=['GET'])
def permission_create():
    menus = Menu.get_all(is_group=True)
    return render_template('admin/permission/create.html', menus=menus)


@app.route('/permission', methods=['POST'])
def permission_store():
    form = PermissionCreateForm(request.form)
    if form.validate():
        permission = Permission()
        permission.create(data=form.data)
        return Success(message="操作成功！")
    return Fail(message=form.first_error)


@app.route('/permission/<int:id>/edit', methods=['GET'])
def permission_edit(id):
    permission = Permission.get_by_id(id)
    menus = Menu.get_all(is_group=True)
    return render_template('admin/permission/edit.html', permission=permission, menus=menus)


@app.route('/permission/<int:id>', methods=['PUT'])
def permission_update(id):
    edit_one_field = request.form.get('edit_one_field', None)
    if not edit_one_field:
        form = PermissionEditForm(formdata=request.form, id=id)
    else:
        form = PermissionEditOneKeyForm(formdata=request.form, id=id)
    if not form.validate():
        return Fail(message=form.first_error)
    permission = Permission.get_by_id(id=id)
    permission.update(form.data, edit_one_field)

    return Success(message="操作成功！")


@app.route('/permission/<ids>', methods=['DELETE'])
def permission_delete(ids):
    ids = ids.split('-')
    permissions = Permission.get_all_in_ids(ids=ids);
    for permission in permissions:
        permission.destroy()
    return Success(message="成功删除")
