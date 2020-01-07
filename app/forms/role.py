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
from app.models.role import Role
from app.vendor.forms import SignlessIntegerField as IntegerField

class RoleCreateForm(Base):
    name = StringField(validators=[InputRequired(message="请输入角色名称"), Length(1, 20, message="角色名称长度2-20位")])
    label = StringField(validators=[Length(0, 255, message="角色简介最大长度255位")])
    active = IntegerField()

    def validate_name(self, field):
        if Role.query.filter_by(name=field.data).first():
            raise ValidationError("角色名称已经存在")
        if not between(field.data, 1, 20):
            raise ValidationError("角色名称长度2-20位")

    def validate_label(self, field):
        if field.data:
            if len(field.data) > 255:
                raise ValidationError("角色简介最大长度255位")


class RoleEditForm(RoleCreateForm):

    def validate_name(self, field):
        if Role.query.filter_by(name=field.data).filter(Role.id != self.id).first():
            raise ValidationError("角色名称已经存在")
        if not between(field.data, 1, 20):
            raise ValidationError("角色名称长度2-20位")


class RoleEditOneKeyForm(Base):
    name = StringField()
    label = StringField()
    active = IntegerField()

    def validate_name(self, field):
        if field.name in get_request_field():
            if not field.data:
                raise ValidationError("请输入角色名称")
            if Role.query.filter_by(name=field.data).filter(Role.id != self.id).first():
                raise ValidationError("角色名称已经存在")
            if not between(field.data, 1, 20):
                raise ValidationError("角色名称长度2-20位")

    def validate_label(self, field):
        if field.name in get_request_field():
            if field.data:
                if len(field.data) > 255:
                    raise ValidationError("角色简介最大长度255位")



