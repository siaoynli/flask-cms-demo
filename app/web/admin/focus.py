"""
created  by  hzwlxy  at 2018/7/4 12:26
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import render_template, request

__author__ = '西瓜哥'
from app.web import admin_app as app
from app.forms.focus import FocusCreateForm, FocusEditForm, \
    FocusEditOneKeyForm
from app.libs.layui_response import Success, Fail
from app.libs.datagrid_response import AjaxResponse
from app.models.focus import Focus
from app.models.column import Column


@app.route('/focus', methods=['GET'])
def focus_index():
    return render_template('admin/focus/index.html')


@app.route('/focus/lists', methods=['GET'])
def focus_lists():
    total, result = Focus.get_limit_all()
    return AjaxResponse(data=result, count=total)


@app.route('/focus/create', methods=['GET'])
def focus_create():
    columns = Column.get_all_for_select(is_group=True)
    return render_template('admin/focus/create.html', columns=columns)


@app.route('/focus', methods=['POST'])
def focus_store():
    form = FocusCreateForm(request.form)
    if form.validate():
        focus = Focus()
        focus.create(data=form.data)
        return Success(message="操作成功！")
    return Fail(message=form.first_error)


@app.route('/focus/<int:id>/edit', methods=['GET'])
def focus_edit(id):
    focus = Focus.get_by_id(id)
    columns = Column.get_all_for_select(is_group=True)
    return render_template('admin/focus/edit.html', focus=focus, columns=columns)


@app.route('/focus/<int:id>', methods=['PUT'])
def focus_update(id):
    edit_one_field = request.form.get('edit_one_field', None)
    if not edit_one_field:
        form = FocusEditForm(formdata=request.form, id=id)
    else:
        form = FocusEditOneKeyForm(formdata=request.form, id=id)
    if not form.validate():
        return Fail(message=form.first_error)
    focus = Focus.get_by_id(id=id)
    focus.update(form.data, edit_one_field)

    return Success(message="操作成功！")


@app.route('/focus/<ids>', methods=['DELETE'])
def focus_delete(ids):
    ids = ids.split('-')
    focuses = Focus.get_all_in_ids(ids=ids)
    for focus in focuses:
        focus.destroy()
    return Success(message="成功删除")
