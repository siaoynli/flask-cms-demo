"""
created  by  hzwlxy  at 2018/7/4 11:11
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 管理员相关验证
"""

from wtforms import StringField, DateField
from wtforms.validators import ValidationError, InputRequired, Length

__author__ = '西瓜哥'

from .base import Base
from app.libs.helper import get_request_field, between
from app.vendor.forms import SignlessIntegerField as IntegerField
from app.models.note import Note


class NoteCreateForm(Base):
    content = StringField(validators=[InputRequired(message="请输入公告内容"), Length(1, 255, message="公告内容长度最大255位")])
    start_date = DateField(validators=[InputRequired(message="请输入起始时间")])
    end_date = DateField(validators=[InputRequired(message="请输入结束时间")])
    level = IntegerField()


class NoteEditForm(NoteCreateForm):
    active = IntegerField()


class NoteEditOneKeyForm(Base):
    content = StringField()
    start_date = DateField()
    end_date = DateField()
    active = IntegerField()
    level = IntegerField()

    def validate_content(self, field):
        if field.name in get_request_field():
            if field.data:
                if not between(field.data, 0, 255):
                    raise ValidationError("公告内容长度最大255位")

    def validate_start_date(self, field):
        if field.name in get_request_field():
            if field.data:
                note = Note.query.filter_by(id=self.id).first()
                if field.data > note.end_date:
                    raise ValidationError("起始时间不能大于结束时间")

    def validate_end_date(self, field):
        if field.name in get_request_field():
            if field.data:
                note = Note.query.filter_by(id=self.id).first()
                if field.data < note.start_date:
                    raise ValidationError("结束时间不能小于起始时间")
