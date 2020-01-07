"""
created  by  hzwlxy  at 2018/7/4 11:11
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 管理员相关验证
"""

from wtforms import StringField

from wtforms.validators import ValidationError, InputRequired, Length

__author__ = '西瓜哥'
from app.libs.helper import get_request_field, between
from .base import Base
from app.models.permission import Permission
from app.vendor.forms import SignlessIntegerField as IntegerField

class PermissionCreateForm(Base):
    name = StringField(validators=[InputRequired(message="请输入权限名称"), Length(1, 20, message="权限名称长度2-20位")])
    endpoint_name = StringField(
        validators=[InputRequired(message="请输入endpoint名称"), Length(4, 20, message="endpoint名称长度4-20位")])
    label = StringField(validators=[Length(0, 255, message="权限简介最大长度255位")])
    level = IntegerField()
    menu_id = IntegerField()
    active = IntegerField()

    def validate_name(self, field):
        if Permission.query.filter_by(name=field.data).first():
            raise ValidationError("权限名称已经存在")
        if not between(field.data, 1, 20):
            raise ValidationError("权限名称长度2-20位")

    def validate_endpoint_name(self, field):
        if Permission.query.filter_by(endpoint_name=field.data).first():
            raise ValidationError("endpoint名称已经存在")
        if not between(field.data, 3, 20):
            raise ValidationError("endpoint名称长度4-20位")


class PermissionEditForm(PermissionCreateForm):
    def validate_name(self, field):
        if Permission.query.filter_by(name=field.data).filter(Permission.id != self.id).first():
            raise ValidationError("权限名称已经存在")
        if not between(field.data, 1, 20):
            raise ValidationError("权限名称长度2-20位")

    def validate_endpoint_name(self, field):
        if Permission.query.filter_by(endpoint_name=field.data).filter(Permission.id != self.id).first():
            raise ValidationError("endpoint名称已经存在")
        if not between(field.data, 3, 20):
            raise ValidationError("endpoint名称长度4-20位")


class PermissionEditOneKeyForm(Base):
    name = StringField()
    label = StringField()
    endpoint_name = StringField()
    active = IntegerField()

    def validate_name(self, field):
        if field.name in get_request_field():
            if not field.data:
                raise ValidationError("请输入权限名称")
            if Permission.query.filter_by(name=field.data).filter(Permission.id != self.id).first():
                raise ValidationError("权限名称已经存在")
            if not between(field.data, 1, 20):
                raise ValidationError("权限名称长度2-20位")

    def validate_endpoint_name(self, field):
        if field.name in get_request_field():
            if not field.data:
                raise ValidationError("请输入endpoint名称")
            if Permission.query.filter_by(endpoint_name=field.data).filter(Permission.id != self.id).first():
                raise ValidationError("endpoint名称已经存在")
            if not between(field.data, 3, 20):
                raise ValidationError("endpoint名称长度4-20位")

    def validate_label(self, field):
        if field.name in get_request_field():
            if field.data:
                if len(field.data) > 255:
                    raise ValidationError("权限简介最大长度255位")
