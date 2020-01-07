"""
created  by  hzwlxy  at 2018/7/4 12:26
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import render_template, request

__author__ = '西瓜哥'
from app.web import admin_app as app
from app.forms.link import LinkCreateForm, LinkEditForm, \
    LinkEditOneKeyForm
from app.libs.layui_response import Success, Fail
from app.libs.datagrid_response import AjaxResponse
from app.models.link import Link
from app.models.column import Column


@app.route('/link', methods=['GET'])
def link_index():
    return render_template('admin/link/index.html')


@app.route('/link/lists', methods=['GET'])
def link_lists():
    total, result = Link.get_limit_all()
    return AjaxResponse(data=result, count=total)


@app.route('/link/create', methods=['GET'])
def link_create():
    columns = Column.get_all_for_select(is_group=True)
    return render_template('admin/link/create.html', columns=columns)


@app.route('/link', methods=['POST'])
def link_store():
    form = LinkCreateForm(request.form)
    if form.validate():
        link = Link()
        link.create(data=form.data)
        return Success(message="操作成功！")
    return Fail(message=form.first_error)


@app.route('/link/<int:id>/edit', methods=['GET'])
def link_edit(id):
    link = Link.get_by_id(id)
    columns = Column.get_all_for_select(is_group=True)
    return render_template('admin/link/edit.html', link=link, columns=columns)


@app.route('/link/<int:id>', methods=['PUT'])
def link_update(id):
    edit_one_field = request.form.get('edit_one_field', None)
    if not edit_one_field:
        form = LinkEditForm(formdata=request.form, id=id)
    else:
        form = LinkEditOneKeyForm(formdata=request.form, id=id)
    if not form.validate():
        return Fail(message=form.first_error)
    link = Link.get_by_id(id=id)
    link.update(form.data, edit_one_field)

    return Success(message="操作成功！")


@app.route('/link/<ids>', methods=['DELETE'])
def link_delete(ids):
    ids = ids.split('-')
    links = Link.get_all_in_ids(ids=ids)
    for link in links:
        link.destroy()
    return Success(message="成功删除")
