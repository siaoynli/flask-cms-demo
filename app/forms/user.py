"""
created  by  hzwlxy  at 2018/7/4 11:11
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 管理员相关验证
"""
from wtforms import StringField, PasswordField
from wtforms.validators import ValidationError, InputRequired, Length

__author__ = '西瓜哥'

from .base import Base
from app.vendor.forms import SignlessIntegerField as IntegerField

class UserLoginForm(Base):
    name = StringField(validators=[InputRequired(message="请输入用户名"), Length(4, 20, message="用户名长度4-20位")])
    password = PasswordField(validators=[InputRequired(message="请输入密码"), Length(4, 20, message="密码长度4-20位")])
