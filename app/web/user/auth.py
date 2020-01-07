"""
created  by  hzwlxy  at 2018/7/4 15:19
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user

__author__ = '西瓜哥'
from app.web import user_app as app
from app.forms.user import UserLoginForm
from app.models.user import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        form = UserLoginForm(request.form)
        if form.validate():
            user = User.query.filter_by(name=form.name.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=True)
                next = url_for('user.index')
                return redirect(next)
            return '用户名或密码错误'

        return '表单验证错误'
    else:
        if current_user.is_authenticated and request.blueprint in current_user.get_id():
            return redirect(url_for('user.index'))
        return render_template("user/auth/login.html")


@app.route('/logout')
@login_required
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    logout_user()
    return 'ok'
