"""
created  by  hzwlxy  at 2018/7/4 12:26
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import render_template, request
from flask_login import current_user

__author__ = '西瓜哥'
from app.ext import db
from app.web import admin_app as app
from app.forms.admin import AdminProfileForm, AdminPasswordForm, AdminAvatarForm, AdminCreateForm, AdminEditForm, \
    AdminEditOneKeyForm
from app.libs.layui_response import Success, Fail
from app.libs.datagrid_response import AjaxResponse
from app.models.admin import Admin
from app.models.role import Role


@app.route('/admin', methods=['GET'])
def admin_index():
    return render_template('admin/admin/index.html')


@app.route('/admin/lists', methods=['GET'])
def admin_lists():
    total, result = Admin.get_list_all()
    return AjaxResponse(data=result, count=total)


@app.route('/admin/create', methods=['GET'])
def admin_create():
    roles = Role.get_all()
    return render_template('admin/admin/create.html', roles=roles)


@app.route('/admin', methods=['POST'])
def admin_store():
    form = AdminCreateForm(request.form)
    if form.validate():
        admin = Admin()
        admin.create(data=form.data)
        return Success(message="操作成功！")
    return Fail(message=form.first_error)


@app.route('/admin/<int:id>/edit', methods=['GET'])
def admin_edit(id):
    admin = Admin.get_by_id(id)
    roles = Role.get_all()
    return render_template('admin/admin/edit.html', admin=admin, roles=roles)


@app.route('/admin/<int:id>', methods=['PUT'])
def admin_update(id):
    edit_one_field = request.form.get('edit_one_field', None)
    if not edit_one_field:
        form = AdminEditForm(formdata=request.form, id=id)
    else:
        form = AdminEditOneKeyForm(formdata=request.form, id=id)
    if not form.validate():
        return Fail(message=form.first_error)
    admin = Admin.get_by_id(id=id)
    admin.update(form.data, edit_one_field)

    return Success(message="操作成功！")


@app.route('/admin/<ids>', methods=['DELETE'])
def admin_delete(ids):
    ids = ids.split('-')
    if '1' in ids:
        return Fail(message="网站创始人不能删除")
    admins = Admin.get_all_in_ids(ids=ids)
    for admin in admins:
        admin.destroy()
    return Success(message="成功删除")


@app.route('/admin/profile', methods=['get', 'post'])
def admin_profile():
    form = AdminProfileForm(request.form)
    if request.method == "POST":
        if form.validate():
            user = current_user
            with db.auto_commit():
                user.set_attrs(form.data)
            return Success(message="操作成功！")
        return Fail(message=form.first_error)
    else:
        roles = Role.get_all()
        return render_template('admin/admin/profile.html', roles=roles)


@app.route('/admin/avatar/edit', methods=['get', 'post'])
def admin_edit_avatar():
    if request.method == "POST":

        form = AdminAvatarForm(request.form)
        if form.validate():
            user = current_user
            with db.auto_commit():
                user.set_attrs(form.data)
            return Success(message="操作成功！")
        return Fail(message=form.first_error)
    else:
        user = current_user
        avatar = user.avatar
        return render_template('admin/admin/avatar.html', avatar=avatar)


@app.route('/admin/password/edit', methods=['get', 'post'])
def admin_edit_password():
    """
    修改密码
    :return:
    """
    form = AdminPasswordForm(request.form)
    if request.method == "POST":
        if form.validate():
            user = current_user
            if not user.check_password(form.oldpassword.data):
                return Fail(message="原始密码错误！")
            if form.oldpassword.data == form.password.data:
                return Fail(message="新旧密码必须不一样！")
            with db.auto_commit():
                user.set_password(form.password.data)
            return Success(message="操作成功！")

        return Fail(message=form.first_error)
    else:
        return render_template('admin/admin/password.html')
