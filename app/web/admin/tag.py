"""
created  by  hzwlxy  at 2018/7/4 12:26
__author__: 西瓜哥
__QQ__ : 120235331
__Tag__： 
"""
from flask import render_template

__author__ = '西瓜哥'
from app.web import admin_app as app

from app.libs.layui_response import Success
from app.libs.datagrid_response import AjaxResponse
from app.models.tag import Tag


@app.route('/tag', methods=['GET'])
def tag_index():
    return render_template('admin/tag/index.html')


@app.route('/tag/lists', methods=['GET'])
def tag_lists():
    total, result = Tag.get_limit_all()
    return AjaxResponse(data=result, count=total)


@app.route('/tag/<ids>', methods=['DELETE'])
def tag_delete(ids):
    ids = ids.split('-')
    tags = Tag.get_all_in_ids(ids=ids)
    for tag in tags:
        tag.destroy()
    return Success(message="成功删除")
