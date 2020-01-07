"""
created  by  hzwlxy  at 2018/7/11 10:17
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import render_template, request

__author__ = '西瓜哥'

from app.web import admin_app as app
from app.models.menu import Menu
from app.libs.datagrid_response import AjaxResponse
from app.libs.layui_response import Success, Fail
from app.forms.menu import MenuCreateForm, MenuEditForm, MenuEditOneKeyForm


@app.route('/menu', methods=['GET'])
def menu_index():
    return render_template('admin/menu/index.html')


@app.route('/menu/lists', methods=['GET'])
def menu_lists():
    total, result = Menu.get_list_all(is_sort=True)
    return AjaxResponse(data=result, count=total)


@app.route('/menu/create', methods=['GET'])
def menu_create():
    menus = Menu.get_all_for_select(is_group=True)
    return render_template('admin/menu/create.html', menus=menus)


@app.route('/menu', methods=['POST'])
def menu_store():
    form = MenuCreateForm(request.form)
    if form.validate():
        menu = Menu()
        menu.create(data=form.data)
        return Success(message="操作成功！")
    return Fail(message=form.first_error)


@app.route('/menu/<int:id>/edit', methods=['GET'])
def menu_edit(id):
    menu = Menu.get_by_id(id)
    menus = Menu.get_all_except_by_id(id=id, is_sort=True)
    return render_template('admin/menu/edit.html', menu=menu, menus=menus)


@app.route('/menu/<int:id>', methods=['PUT'])
def menu_update(id):
    edit_one_field = request.form.get('edit_one_field', None)
    if not edit_one_field:
        form = MenuEditForm(formdata=request.form, id=id)
    else:
        form = MenuEditOneKeyForm(formdata=request.form, id=id)
    if not form.validate():
        return Fail(message=form.first_error)
    menu = Menu.get_by_id(id=id)
    menu.update(form.data, edit_one_field)

    return Success(message="操作成功！")


@app.route('/menu/<ids>', methods=['DELETE'])
def menu_delete(ids):
    ids = ids.split('-')
    menus = Menu.get_all_in_ids(ids=ids)
    for menu in menus:
        menu.destroy()
    return Success(message="成功删除")
