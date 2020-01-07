"""
created  by  hzwlxy  at 2018/7/4 15:19
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
import datetime
from flask import render_template, request, url_for, redirect
from flask_login import login_user, current_user, logout_user

__author__ = '西瓜哥'
from app.web import admin_app as app
from app.forms.admin import AdminLoginForm
from app.models.admin import Admin
from app.libs.response import Success, Fail
from app.libs.layui_response import Success as LayuiSuccess


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = AdminLoginForm(request.form)
    if request.method == "POST":
        if form.validate():
            admin = Admin.query.filter_by(name=form.name.data).first()
            if admin and admin.check_password(form.password.data):
                login_user(admin)
                admin.login_ip = request.remote_addr
                admin.login_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                admin.login_count += 1
                next = request.args.get('next')
                if not next or not next.startswith('/'):
                    next = url_for('admin.index')
                return Success(message="登录成功", redirect_to=next)
            return Fail(message="用户名或密码错误")
        return Fail(message=form.first_error)
    else:
        if current_user.is_authenticated and request.blueprint in current_user.get_id():
            return redirect(url_for('admin.index'))
        return render_template("admin/auth/login.html")


@app.route('/auth/get_avatar/<name>')
def get_avatar(name):
    admin = Admin.query.filter_by(name=name).first()
    avatar = 'admin/images/guest.png'
    if admin and admin.avatar:
        avatar = admin.avatar
    data = {'image': avatar}
    return Success(data=data)


@app.route('/logout')
def logout():
    """
    退出登录，不用 login_required 防止 退出时候链接带上next
    :return:
    """
    if not current_user.is_authenticated:
        return redirect(url_for('admin.login'))
    logout_user()
    return LayuiSuccess(message="退出成功")
