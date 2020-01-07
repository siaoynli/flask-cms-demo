"""
created  by  hzwlxy  at 2018/7/4 12:26
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import render_template, request

__author__ = '西瓜哥'
from app.web import admin_app as app
from app.forms.note import NoteCreateForm, NoteEditForm, \
    NoteEditOneKeyForm
from app.libs.layui_response import Success, Fail
from app.libs.datagrid_response import AjaxResponse
from app.models.note import Note
from app.models.column import Column


@app.route('/note', methods=['GET'])
def note_index():
    return render_template('admin/note/index.html')


@app.route('/note/lists', methods=['GET'])
def note_lists():
    total, result = Note.get_limit_all()
    return AjaxResponse(data=result, count=total)


@app.route('/note/create', methods=['GET'])
def note_create():
    columns = Column.get_all_for_select(is_group=True)
    return render_template('admin/note/create.html', columns=columns)


@app.route('/note', methods=['POST'])
def note_store():
    form = NoteCreateForm(request.form)
    if form.validate():
        note = Note()
        note.create(data=form.data)
        return Success(message="操作成功！")
    return Fail(message=form.first_error)


@app.route('/note/<int:id>/edit', methods=['GET'])
def note_edit(id):
    note = Note.get_by_id(id)
    columns = Column.get_all_for_select(is_group=True)
    return render_template('admin/note/edit.html', note=note, columns=columns)


@app.route('/note/<int:id>', methods=['PUT'])
def note_update(id):
    edit_one_field = request.form.get('edit_one_field', None)
    if not edit_one_field:
        form = NoteEditForm(formdata=request.form, id=id)
    else:
        form = NoteEditOneKeyForm(formdata=request.form, id=id)
    if not form.validate():
        return Fail(message=form.first_error)
    note = Note.get_by_id(id=id)
    note.update(form.data, edit_one_field)

    return Success(message="操作成功！")


@app.route('/note/<ids>', methods=['DELETE'])
def note_delete(ids):
    ids = ids.split('-')
    notes = Note.get_all_in_ids(ids=ids)
    for note in notes:
        note.destroy()
    return Success(message="成功删除")
