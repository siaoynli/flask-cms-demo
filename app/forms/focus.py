"""
created  by  hzwlxy  at 2018/7/4 11:11
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 管理员相关验证
"""
import re
from wtforms import StringField, SelectField
from wtforms.validators import ValidationError, InputRequired, Length, URL

__author__ = '西瓜哥'

from .base import Base
from app.models.focus import Focus
from app.libs.helper import get_request_field, between
from app.vendor.forms import SignlessIntegerField as IntegerField


class FocusCreateForm(Base):
    title = StringField(validators=[InputRequired(message="请输入焦点图标题"), Length(0, 100, message="焦点图标题长度最大100位")])
    label = StringField(validators=[Length(0, 255, message="焦点图说明长度最大255位")])
    link = StringField()
    thumb_image = StringField(validators=[Length(0, 255, message="缩略图地址长度最大100位")])
    level = IntegerField()
    target = IntegerField()
    column_id = IntegerField()

    def validate_title(self, field):
        if Focus.query.filter_by(title=field.data).first():
            raise ValidationError("焦点图标题已经存在")

    def validate_link(self, field):
        if field.data:
            regex = re.compile(r'^[a-z]+://(?P<host>[^/:]+)(?P<port>:[0-9]+)?(?P<path>\/.*)?$')
            if not regex.match(field.data):
                raise ValidationError('外链不是有效的链接')


class FocusEditForm(FocusCreateForm):
    active = IntegerField()

    def validate_title(self, field):
        if Focus.query.filter_by(title=field.data).filter(Focus.id != self.id).first():
            raise ValidationError("焦点图标题已经存在")


class FocusEditOneKeyForm(Base):
    title = StringField()
    label = StringField()
    level = IntegerField()
    target = IntegerField()
    active = IntegerField()

    def validate_title(self, field):
        if field.name in get_request_field():
            if not field.data:
                raise ValidationError("请输入焦点图标题")
            if not between(field.data, 0, 100):
                raise ValidationError("焦点图标题长度最大100位")
            if Focus.query.filter_by(title=field.data).filter(Focus.id != self.id).first():
                raise ValidationError("焦点图标题已经存在")

    def validate_label(self, field):
        if field.name in get_request_field():
            if field.data:
                if not between(field.data, 0, 255):
                    raise ValidationError("焦点图说明长度最大255位")
