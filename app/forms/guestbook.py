"""
created  by  hzwlxy  at 2018/7/4 11:11
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 留言
"""
from flask_login import current_user
from wtforms import StringField
from wtforms.validators import ValidationError, InputRequired, Length

__author__ = '西瓜哥'

from .base import Base
from app.libs.helper import get_request_field, between
from app.models.guestbook import Guestbook
from app.vendor.forms import SignlessIntegerField as IntegerField

class GuestbookCreateForm(Base):
    content = StringField(validators=[InputRequired(message="请输入留言内容"), Length(1, 255, message="留言内容长度最大255位")])
    pid = IntegerField()
    root_id = StringField()

    def validate_pid(self, field):
        if field.data:
            guestbook = Guestbook.get_by_id(field.data)
            if guestbook.user_id == current_user.id:
                raise ValidationError("您不能回复您自己！")

    def validate_root_id(self, field):
        if not field.data:
            raise ValidationError("参数错误！")
        arr = field.data.split('-')
        pid = arr.pop()
        guestbook = Guestbook.get_by_id(pid)
        if not guestbook:
            raise ValidationError("参数错误！")
        if len(arr) == 0:
            raise ValidationError("参数错误！")
        root_id = "-".join(arr)
        guestbook = Guestbook.get_by_root_id(root_id)
        if not guestbook:
            raise ValidationError("参数错误！")


class GuestbookEditForm(Base):
    content = StringField(validators=[InputRequired(message="请输入留言内容"), Length(1, 255, message="留言内容长度最大255位")])
    good = IntegerField()
    active = IntegerField()


class GuestbookEditOneKeyForm(Base):
    content = StringField()
    active = IntegerField()
    good = IntegerField()

    def validate_content(self, field):
        if field.name in get_request_field():
            if field.data:
                if not between(field.data, 0, 255):
                    raise ValidationError("留言内容长度最大255位")
