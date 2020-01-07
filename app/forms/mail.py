"""
created  by  hzwlxy  at 2018/7/4 11:11
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 管理员相关验证
"""

from wtforms import StringField, SelectField

from wtforms.validators import ValidationError, InputRequired, Length

__author__ = '西瓜哥'
from .base import Base
from app.vendor.forms import SignlessIntegerField as IntegerField

class MailForm(Base):
    mail_server = StringField(validators=[InputRequired(message="请输入邮箱服务器"), Length(1, 100, message="邮箱服务器长度2-100位")])
    port = IntegerField(validators=[InputRequired(message="请输入端口")])
    link_model = SelectField(choices=[('tls', 'TLS'), ('ssl', 'SSL')], validators=[InputRequired(message="请输入传送类型")])
    username = StringField(validators=[InputRequired(message="请输入邮箱用户名"), Length(6, 100, message="邮箱用户名长度2-100位")])
    password = StringField(validators=[InputRequired(message="请输入邮箱密码或秘钥"), Length(6, 100, message="邮箱密码或秘钥长度2-100位")])
