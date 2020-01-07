"""
created  by  hzwlxy  at 2018/7/11 10:17
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import render_template, request


__author__ = '西瓜哥'

from app.web import admin_app as app
from app.models.role import Role
from app.libs.datagrid_response import LayuiResponse
from app.libs.layui_response import Success, Fail
from app.forms.role import RoleCreateForm, RoleEditForm, RoleEditOneKeyForm


@app.route('/role', methods=['GET'])
def role_index():
    return render_template('admin/role/index.html')


@app.route('/role/lists', methods=['GET'])
def role_lists():
    total, result = Role.get_list_all()
    return LayuiResponse(data=result, count=total)


@app.route('/role/create', methods=['GET'])
def role_create():
    menus = Role.get_menu_for_role()
    return render_template('admin/role/create.html', menus=menus)


@app.route('/role', methods=['POST'])
def role_store():
    form = RoleCreateForm(request.form)
    if form.validate():
        role = Role()
        role.create(data=form.data)
        return Success(message="操作成功！")
    return Fail(message=form.first_error)


@app.route('/role/<int:id>/edit', methods=['GET'])
def role_edit(id):
    role = Role.get_by_id(id)
    menus = Role.get_menu_for_role()
    temp = []
    for menu in menus:
        menu.checkbox = False
        permissions = menu.permissions
        if permissions:
            for permission in permissions:
                if role in permission.roles:
                    menu.checkbox = True
                    break
        temp.append(menu)

    permission_ids = []
    if role.permissions:
        for permission in role.permissions:
            permission_ids.append(permission.id)

    return render_template('admin/role/edit.html', role=role, menus=temp, permission_ids=permission_ids)


@app.route('/role/<int:id>', methods=['PUT'])
def role_update(id):
    edit_one_field = request.form.get('edit_one_field', None)
    if not edit_one_field:
        form = RoleEditForm(formdata=request.form, id=id)
    else:
        form = RoleEditOneKeyForm(formdata=request.form, id=id)
    if not form.validate():
        return Fail(message=form.first_error)
    role = Role.get_by_id(id=id)
    role.update(form.data, edit_one_field)

    return Success(message="操作成功！")


@app.route('/role/<ids>', methods=['DELETE'])
def role_delete(ids):
    ids = ids.split('-')
    if '1' in ids:
        return Fail(message="不能删除超级管理员角色")
    roles = Role.get_all_in_ids(ids=ids)
    for role in roles:
        role.destroy()
    return Success(message="成功删除")
