"""
created  by  hzwlxy  at 2018/7/4 12:26
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import render_template, request
from uuid import uuid4

__author__ = '西瓜哥'
from app.web import admin_app as app
from app.forms.document import DocumentCreateForm, DocumentEditForm, \
    DocumentEditOneKeyForm
from app.libs.layui_response import Success, Fail
from app.libs.datagrid_response import AjaxResponse
from app.models.document import Document
from app.models.column import Column


@app.route('/document', methods=['GET'])
def document_index():
    return render_template('admin/document/index.html')


@app.route('/document/lists', methods=['GET'])
def document_lists():
    total, result = Document.get_limit_all()
    return AjaxResponse(data=result, count=total)


@app.route('/document/create', methods=['GET'])
def document_create():
    columns = Column.get_all_for_select(is_group=True)
    uuid = uuid4()
    return render_template('admin/document/create.html', columns=columns, uuid=uuid)



@app.route('/document', methods=['POST'])
def document_store():
    form = DocumentCreateForm(request.form)
    if form.validate():
        document = Document()
        document.create(data=form.data)
        return Success(message="操作成功！")
    return Fail(message=form.first_error)


@app.route('/document/<int:id>/edit', methods=['GET'])
def document_edit(id):
    document = Document.get_by_id(id)
    columns = Column.get_all_for_select(is_group=True)
    attribute = document.attribute.split(',')
    return render_template('admin/document/edit.html', document=document, columns=columns, attribute=attribute)


@app.route('/document/<int:id>', methods=['PUT'])
def document_update(id):
    edit_one_field = request.form.get('edit_one_field', None)
    if not edit_one_field:
        form = DocumentEditForm(formdata=request.form, id=id)
    else:
        form = DocumentEditOneKeyForm(formdata=request.form, id=id)
    if not form.validate():
        return Fail(message=form.first_error)
    document = Document.get_by_id(id=id)
    document.update(form.data, edit_one_field)

    return Success(message="操作成功！")


@app.route('/document/<ids>', methods=['DELETE'])
def document_delete(ids):
    ids = ids.split('-')
    documentes = Document.get_all_in_ids(ids=ids)
    for document in documentes:
        document.destroy()
    return Success(message="成功删除")
