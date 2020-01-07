"""
created  by  hzwlxy  at 2018/7/4 11:33
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 蓝图，模块分类
"""
from flask import Blueprint, render_template, current_app
from flask_wtf.csrf import CSRFError

__author__ = '西瓜哥'

from app.libs.layui_response import Fail
from app.libs.helper import read_ini_file
from app.libs.auth import Auth

system = read_ini_file('system')

admin_app = Blueprint('admin', __name__, url_prefix="/" + system['admin_prefix'])
user_app = Blueprint('user', __name__, url_prefix="/user")
upload_app = Blueprint('upload', __name__, url_prefix="/uploads")
web_app = Blueprint('web', __name__)


# errorhandler 是对于蓝图起作用的， app_errorhandler 是对于全局的异常处理,随便用哪个蓝图定义都行
@admin_app.app_errorhandler(CSRFError)
def csrf_error(e):
    return Fail(message="CsrfToken错误，请刷新页面重试")

# 后台
@admin_app.before_request
def process_request():
    auth = Auth()
    if not auth.login_required():
        return current_app.login_manager.unauthorized()

@admin_app.errorhandler(404)
def page_not_found(e):
    print(e)
    return Fail(message="page not found")


# 用户
@user_app.before_request
def process_request():
    auth = Auth()
    if not auth.login_required():
        return current_app.login_manager.unauthorized()

@user_app.errorhandler(404)
def page_not_found(e):
    print('user')
    return Fail(message="page not found")


# 前台
@web_app.errorhandler(404)
def page_not_found1(e):
    print('web')
    return '404', 404


from app.web import admin
from app.web import user
from app.web import home
from app.web import upload