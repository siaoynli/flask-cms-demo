"""
created  by  hzwlxy  at 2018/7/4 12:26
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import render_template, request


__author__ = '西瓜哥'

from app.web import admin_app as app
from app.forms.mail import MailForm
from app.libs.layui_response import Success, Fail
from app.models.mail import Mail
from app.libs.helper import write_ini_file


@app.route('/mail', methods=['get', 'post'])
def admin_mail():
    form = MailForm(request.form)

    if request.method == "POST":
        if form.validate():
            mail = Mail.query.first()
            mail.update(form.data)
            write_ini_file('mail', form.data)
            return Success(message="操作成功！")
        return Fail(message=form.first_error)
    else:

        mail = Mail.query.first()
        return render_template('admin/mail/index.html', mail=mail)
