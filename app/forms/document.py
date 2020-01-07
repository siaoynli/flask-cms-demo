"""
created  by  hzwlxy  at 2018/7/4 11:11
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 管理员相关验证
"""
import re
from wtforms import StringField, DateTimeField, TextAreaField
from wtforms.validators import ValidationError, InputRequired, Length, URL
from app.vendor.forms import SignlessIntegerField as IntegerField

__author__ = '西瓜哥'

from .base import Base
from app.models.document import Document
from app.libs.helper import get_request_field, between


class DocumentCreateForm(Base):
    title = StringField(validators=[InputRequired(message="请输入文档标题"), Length(0, 100, message="文档标题长度最大100位")])
    uuid = StringField()
    sub_title = StringField()
    keyword = StringField(validators=[Length(0, 100, message="META关键字长度最大100位")])
    description = StringField(validators=[Length(0, 200, message="META描述长度最大200位")])
    label = StringField(validators=[Length(0, 200, message="摘要长度最大200位")])
    external_link = StringField()
    published_at = DateTimeField()
    thumb_image = StringField(validators=[Length(0, 255, message="缩略图地址长度最大100位")])
    author = StringField(validators=[Length(0, 20, message="作者长度最大20位")])
    source = StringField(validators=[Length(0, 100, message="来源长度最大100位")])
    source_link = StringField(validators=[Length(0, 100, message="来源链接长度最大100位")])
    attribute = StringField()
    content = TextAreaField()
    tags = StringField()
    target = IntegerField()
    click = IntegerField()
    editor = StringField(validators=[Length(0, 20, message="编辑长度最大20位")])
    is_original = IntegerField()
    open_comment = IntegerField()
    attach_file = StringField(validators=[Length(0, 100, message="附件长度最大100位")])
    attach_name = StringField(validators=[Length(0, 100, message="附件名称长度最大100位")])
    column_id = IntegerField()
    login_show = IntegerField()
    password_txt = StringField(validators=[Length(0, 50, message="密码长度最大50位")])
    user_group = IntegerField()

    def validate_title(self, field):
        if Document.query.filter_by(title=field.data).first():
            raise ValidationError("文档标题已经存在")

    def validate_uuid(self, field):
        if Document.query.filter_by(uuid=field.data).first():
            raise ValidationError("文档别名已经存在")

    def validate_external_link(self, field):
        if field.data:
            regex = re.compile(r'^[a-z]+://(?P<host>[^/:]+)(?P<port>:[0-9]+)?(?P<path>\/.*)?$')
            if not regex.match(field.data):
                raise ValidationError('外部链接不是有效的链接')

    def validate_source_link(self, field):
        if field.data:
            regex = re.compile(r'^[a-z]+://(?P<host>[^/:]+)(?P<port>:[0-9]+)?(?P<path>\/.*)?$')
            if not regex.match(field.data):
                raise ValidationError('来源链接不是有效的链接')


class DocumentEditForm(DocumentCreateForm):
    active = IntegerField()

    def validate_title(self, field):
        if Document.query.filter_by(title=field.data).filter(Document.id != self.id).first():
            raise ValidationError("文档标题已经存在")

    def validate_uuid(self, field):
        if Document.query.filter_by(uuid=field.data).filter(Document.id != self.id).first():
            raise ValidationError("文档别名已经存在")


class DocumentEditOneKeyForm(Base):
    title = StringField()
    keyword = StringField()
    description = StringField()
    label = StringField()
    author = StringField()
    source = StringField()
    click = IntegerField()
    published_at = DateTimeField()
    editor = StringField()
    is_original = IntegerField()
    open_comment = IntegerField()
    login_show = IntegerField()
    password_txt = StringField()
    target = IntegerField()
    active = IntegerField()

    def validate_title(self, field):
        if field.name in get_request_field():
            if not field.data:
                raise ValidationError("请输入文档标题")
            if not between(field.data, 0, 100):
                raise ValidationError("文档标题长度最大100位")
            if Document.query.filter_by(title=field.data).filter(Document.id != self.id).first():
                raise ValidationError("文档标题已经存在")

    def validate_keyword(self, field):
        if field.name in get_request_field():
            if field.data:
                if not between(field.data, 0, 100):
                    raise ValidationError("META关键字长度最大100位")

    def validate_description(self, field):
        if field.name in get_request_field():
            if field.data:
                if not between(field.data, 0, 200):
                    raise ValidationError("META描述长度最大200位")

    def validate_label(self, field):
        if field.name in get_request_field():
            if field.data:
                if not between(field.data, 0, 200):
                    raise ValidationError("摘要长度最大200位")

    def validate_author(self, field):
        if field.name in get_request_field():
            if field.data:
                if not between(field.data, 0, 20):
                    raise ValidationError("作者长度最大20位")

    def validate_source(self, field):
        if field.name in get_request_field():
            if field.data:
                if not between(field.data, 0, 100):
                    raise ValidationError("来源长度最大100位")

    def validate_editor(self, field):
        if field.name in get_request_field():
            if field.data:
                if not between(field.data, 0, 20):
                    raise ValidationError("编辑长度最大20位")

    def validate_password_txt(self, field):
        if field.name in get_request_field():
            if field.data:
                if not between(field.data, 0, 50):
                    raise ValidationError("密码长度最大50位")
