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
from app.models.menu import Menu
from app.vendor.forms import SignlessIntegerField as IntegerField

class MenuCreateForm(Base):
    name = StringField(validators=[InputRequired(message="请输入导航名称"), Length(1, 20, message="导航名称长度2-20位")])
    label = StringField(validators=[Length(0, 255, message="导航简介最大长度255位")])
    level = IntegerField()
    pid = IntegerField()
    icon = StringField()
    endpoint_name = StringField()
    target = IntegerField()
    active = IntegerField()

    def validate_name(self, field):
        if Menu.query.filter_by(name=field.data).first():
            raise ValidationError("导航名称已经存在")

    def validate_endpoint_name(self, field):
        if field.data:
            if Menu.query.filter_by(endpoint_name=field.data).first():
                raise ValidationError("endpoint名称已经存在")

            if not between(field.data, 3, 20):
                raise ValidationError("endpoint名称长度4-20位")


class MenuEditForm(MenuCreateForm):

    def validate_name(self, field):
        if Menu.query.filter_by(name=field.data).filter(Menu.id != self.id).first():
            raise ValidationError("导航名称已经存在")

    def validate_endpoint_name(self, field):
        if field.data:
            if Menu.query.filter_by(endpoint_name=field.data).filter(Menu.id != self.id).first():
                raise ValidationError("endpoint名称已经存在")

            if not between(field.data, 3, 20):
                raise ValidationError("endpoint名称长度4-20位")


class MenuEditOneKeyForm(Base):
    name = StringField()
    label = StringField()
    level = IntegerField()
    icon = StringField()
    endpoint_name = StringField()
    target = IntegerField()
    active = IntegerField()

    def validate_name(self, field):
        if field.name in get_request_field():
            if not field.data:
                raise ValidationError("请输入导航名称")
            if Menu.query.filter_by(name=field.data).filter(Menu.id != self.id).first():
                raise ValidationError("导航名称已经存在")
            if not between(field.data, 1, 20):
                raise ValidationError("导航名称长度2-20位")

    def validate_label(self, field):
        if field.name in get_request_field():
            if field.data:
                if len(field.data) > 255:
                    raise ValidationError("导航简介最大长度255位")

    def validate_level(self, field):
        if field.name in get_request_field():
            if isinstance(field.data, int) and field.data < 0:
                raise ValidationError("请输入正整数")

    def validate_endpoint_name(self, field):
        if field.name in get_request_field():
            if Menu.query.filter_by(endpoint_name=field.data).filter(Menu.id != self.id).first():
                raise ValidationError("endpoint名称已经存在")
            if field.data and not between(field.data, 3, 20):
                raise ValidationError("endpoint名称长度4-20位")
