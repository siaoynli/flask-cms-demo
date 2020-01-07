"""
created  by  hzwlxy  at 2018/7/4 12:26
__author__: 西瓜哥
__QQ__ : 120235331
__Guestbook__： 
"""
from flask import render_template, request

__author__ = '西瓜哥'
from app.web import admin_app as app
from app.forms.guestbook import GuestbookCreateForm, GuestbookEditForm, \
    GuestbookEditOneKeyForm
from app.libs.layui_response import Success, Fail
from app.libs.datagrid_response import AjaxResponse
from app.models.guestbook import Guestbook


@app.route('/guestbook', methods=['GET'])
def guestbook_index():
    return render_template('admin/guestbook/index.html')


@app.route('/guestbook/lists', methods=['GET'])
def guestbook_lists():
    id = request.args.get('id', None)

    if id:
        guestbook = Guestbook.get_by_id(id)
        if guestbook.root_id == 0:
            total, result = Guestbook.get_list_all_by_id(id)
        else:
            total, result = Guestbook.get_list_all_by_id(id)
    else:
        total, result = Guestbook.get_limit_all()
    return AjaxResponse(data=result, count=total)


@app.route('/guestbook/<int:id>/reply', methods=['GET'])
def guestbook_create(id):
    guestbook = Guestbook.get_by_id(id)
    pid = id
    return render_template('admin/guestbook/create.html', guestbook=guestbook, pid=pid)


@app.route('/guestbook', methods=['POST'])
def guestbook_store():
    form = GuestbookCreateForm(request.form)
    if form.validate():
        guestbook = Guestbook()
        guestbook.create(data=form.data)
        return Success(message="操作成功！")
    return Fail(message=form.first_error)


@app.route('/guestbook/<int:id>/edit', methods=['GET'])
def guestbook_edit(id):
    guestbook = Guestbook.get_by_id(id)
    return render_template('admin/guestbook/edit.html', guestbook=guestbook)


@app.route('/guestbook/<int:id>', methods=['PUT'])
def guestbook_update(id):
    edit_one_field = request.form.get('edit_one_field', None)
    if not edit_one_field:
        form = GuestbookEditForm(formdata=request.form, id=id)
    else:
        form = GuestbookEditOneKeyForm(formdata=request.form, id=id)
    if not form.validate():
        return Fail(message=form.first_error)
    guestbook = Guestbook.get_by_id(id=id)
    guestbook.update(form.data, edit_one_field)

    return Success(message="操作成功！")


@app.route('/guestbook/<ids>', methods=['DELETE'])
def guestbook_delete(ids):
    ids = ids.split('-')
    guestbooks = Guestbook.get_all_in_ids(ids=ids)
    for guestbook in guestbooks:
        guestbook.destroy()
    return Success(message="成功删除")
