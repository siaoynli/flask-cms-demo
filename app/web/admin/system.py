"""
created  by  hzwlxy  at 2018/7/4 12:26
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import render_template, request


__author__ = '西瓜哥'

from app.web import admin_app as app
from app.forms.system import SystemForm
from app.libs.layui_response import Success, Fail
from app.models.system import System
from app.libs.helper import write_ini_file


@app.route('/system', methods=['get', 'post'])
def admin_system():
    form = SystemForm(request.form)
    if request.method == "POST":
        if form.validate():
            system = System.query.first()
            system.update(form.data)
            write_ini_file('system', form.data)
            return Success(message="操作成功！")
        return Fail(message=form.first_error)
    else:
        system = System.query.first()
        return render_template('admin/system/index.html', system=system)
