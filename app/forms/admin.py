"""
created  by  hzwlxy  at 2018/7/4 11:11
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 管理员相关验证
"""
import re
from wtforms import StringField, RadioField, SelectField
from wtforms.validators import ValidationError, InputRequired, Length, Email

__author__ = '西瓜哥'

from .base import Base
from app.models.admin import Admin
from app.libs.helper import get_request_field, between
from app.vendor.forms import SignlessIntegerField as IntegerField

class AdminLoginForm(Base):
    name = StringField(validators=[InputRequired(message="请输入用户名"), Length(4, 20, message="用户名长度4-20位")])
    password = StringField(validators=[InputRequired(message="请输入密码"), Length(4, 20, message="密码长度4-20位")])


class AdminPasswordForm(Base):
    oldpassword = StringField(validators=[InputRequired(message="请输入旧密码"), Length(6, 20, message="旧密码长度6-20位")])
    password = StringField(validators=[InputRequired(message="请输入新密码"), Length(6, 20, message="新密码长度6-20位")])
    repassword = StringField(validators=[InputRequired(message="请确认新密码")])

    def validate_repassword(self, field):
        if self.password.data != field.data:
            raise ValidationError('两次密码不一致')
        return True


class AdminProfileForm(Base):
    nick_name = StringField(validators=[InputRequired(message="请输入昵称"), Length(3, 20, message="昵称长度3-20位")])
    sex = RadioField(choices=[('1', 'man'), ('2', 'woman'), ('0', 'unknow')])
    chinese_name = StringField()
    phone = StringField()
    qq = StringField()
    remarks = StringField(validators=[Length(0, 255, message="备注字符长度最大255字节")])
    email = StringField(validators=[Email(message="邮箱格式不正确")])

    def validate_chinese_name(self, field):
        if field.data:
            regex = re.compile(r'^[\u4e00-\u9fa5]{2,6}$')
            if not regex.match(field.data):
                raise ValidationError('真实姓名为2-6位中文字符')

    def validate_phone(self, field):
        if field.data:
            regex = re.compile(r'^[1][3,4,5,7,8][0-9]{9}$')
            if not regex.match(field.data):
                raise ValidationError('手机号码格式不正确')

    def validate_qq(self, field):
        if field.data:
            regex = re.compile(r'^\d{5,20}$')
            if not regex.match(field.data):
                raise ValidationError('QQ号码为5位以上数字')


class AdminAvatarForm(Base):
    avatar = StringField(validators=[InputRequired(message="请上传头像"), Length(3, 100, message="头像长度不合法")])

    def validate_avatar(self, field):
        if not field.data.startswith('/'):
            raise ValidationError('头像参数不合法')
        return True


class AdminCreateForm(Base):
    name = StringField(validators=[InputRequired(message="请输入用户名"), Length(3, 20, message="用户名长度2-20位")])
    nick_name = StringField(validators=[InputRequired(message="请输入昵称")])
    chinese_name = StringField()
    password = StringField()
    email = StringField(validators=[InputRequired(message="请输入邮箱"), Email(message="邮箱格式不正确")])
    phone = StringField()
    qq = StringField()
    avatar = StringField()
    sex = IntegerField()
    role_id = IntegerField()
    remarks = StringField()

    def validate_name(self, field):
        if Admin.query.filter_by(name=field.data).first():
            raise ValidationError("用户名已经存在")

    def validate_nick_name(self, field):
        if field.data:
            if not between(field.data, 3, 20):
                raise ValidationError("昵称长度3-20位之间")

    def validate_email(self, field):
        if field.name in get_request_field():
            if Admin.query.filter_by(email=field.data).filter().first():
                raise ValidationError("邮箱已经存在")

    def validate_chinese_name(self, field):
        if field.data:
            regex = re.compile(r'^[\u4e00-\u9fa5]{2,6}$')
            if not regex.match(field.data):
                raise ValidationError('真实姓名为2-6位中文字符')

    def validate_email(self, field):
        if field.data:
            regex = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')
            if not regex.match(field.data):
                raise ValidationError('邮箱是不正确')

    def validate_phone(self, field):
        if field.data:
            if Admin.query.filter_by(phone=field.data).filter().first():
                raise ValidationError("手机号码已经存在")
            regex = re.compile(r'^[1][3,4,5,7,8][0-9]{9}$')
            if not regex.match(field.data):
                raise ValidationError('手机号码格式不正确')

    def validate_qq(self, field):
        if field.data:
            regex = re.compile(r'^\d{5,20}$')
            if not regex.match(field.data):
                raise ValidationError('QQ号码为5位以上数字')


class AdminEditForm(AdminCreateForm):
    active = IntegerField()

    def validate_name(self, field):
        if Admin.query.filter_by(name=field.data).filter(Admin.id != self.id).first():
            raise ValidationError("用户名已经存在")

    def validate_email(self, field):
        if field.name in get_request_field():
            if Admin.query.filter_by(email=field.data).filter(Admin.id != self.id).first():
                raise ValidationError("邮箱已经存在")

    def validate_phone(self, field):
        if field.data:
            if Admin.query.filter_by(phone=field.data).filter(Admin.id != self.id).first():
                raise ValidationError("手机号码已经存在")
            regex = re.compile(r'^[1][3,4,5,7,8][0-9]{9}$')
            if not regex.match(field.data):
                raise ValidationError('手机号码格式不正确')


class AdminEditOneKeyForm(Base):
    nick_name = StringField()
    chinese_name = StringField()
    email = StringField()
    phone = StringField()
    qq = StringField()
    active = IntegerField()

    def validate_nick_name(self, field):
        if field.name in get_request_field():
            if field.data:
                if not between(field.data, 3, 20):
                    raise ValidationError("昵称长度3-20位之间")

    def validate_chinese_name(self, field):
        if field.name in get_request_field():
            if field.data:
                regex = re.compile(r'^[\u4e00-\u9fa5]{2,6}$')
                if not regex.match(field.data):
                    raise ValidationError('真实姓名为2-6位中文字符')

    def validate_email(self, field):
        if field.name in get_request_field():
            if Admin.query.filter_by(email=field.data).filter(Admin.id != self.id).first():
                raise ValidationError("邮箱已经存在")
            if field.data:
                regex = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')
                if not regex.match(field.data):
                    raise ValidationError('邮箱是不正确')

    def validate_phone(self, field):
        if field.name in get_request_field():
            if field.data:
                if Admin.query.filter_by(phone=field.data).filter(Admin.id != self.id).first():
                    raise ValidationError("手机号码已经存在")
                regex = re.compile(r'^[1][3,4,5,7,8][0-9]{9}$')
                if not regex.match(field.data):
                    raise ValidationError('手机号码格式不正确')

    def validate_qq(self, field):
        if field.name in get_request_field():
            if field.data:
                regex = re.compile(r'^\d{5,20}$')
                if not regex.match(field.data):
                    raise ValidationError('QQ号码为5位以上数字')
