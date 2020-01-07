"""
created  by  hzwlxy  at 2018/7/4 11:11
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 管理员相关验证
"""
import re
from wtforms import StringField
from wtforms.validators import ValidationError, InputRequired, Length, URL

__author__ = '西瓜哥'

from .base import Base
from app.models.link import Link
from app.libs.helper import get_request_field, between
from app.vendor.forms import SignlessIntegerField as IntegerField


class LinkCreateForm(Base):
    site_name = StringField(validators=[InputRequired(message="请输入网站名称"), Length(2, 100, message="网站名称2-100位")])
    site_url = StringField(validators=[InputRequired(message="请输入网站网址"), URL(message="网站网址有误")])
    label = StringField(validators=[Length(0, 255, message="网站介绍最长255字符")])
    logo = StringField(validators=[Length(0, 100, message="网站logo地址最长100字符")])
    site_admin = StringField(validators=[Length(0, 20, message="网站管理员昵称最长20字符")])
    site_admin_email = StringField(validators=[Length(0, 100, message="管理员邮箱最长100字符")])
    site_admin_qq = StringField(validators=[Length(0, 20, message="管理员qq最长20字符")])
    site_admin_phone = StringField(validators=[Length(0, 20, message="管理员电话最长20字符")])
    home_show = IntegerField()
    level = IntegerField()

    def validate_site_name(self, field):
        if Link.query.filter_by(site_name=field.data).first():
            raise ValidationError("网站名称已经存在")

    def validate_site_admin_phone(self, field):
        if field.data:
            regex = re.compile(r'^[1][3,4,5,7,8][0-9]{9}$')
            if not regex.match(field.data):
                raise ValidationError('手机格式不正确')

    def validate_site_admin_email(self, field):
        if field.data:
            regex = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')
            if not regex.match(field.data):
                raise ValidationError('管理员邮箱不是有效的邮箱')


class LinkEditForm(LinkCreateForm):
    active = IntegerField()

    def validate_site_name(self, field):
        if Link.query.filter_by(site_name=field.data).filter(Link.id != self.id).first():
            raise ValidationError("网站名称已经存在")


class LinkEditOneKeyForm(Base):
    site_name = StringField()
    label = StringField()
    site_admin_email = StringField()
    site_admin_qq = StringField()
    site_admin_phone = StringField()
    level = IntegerField()
    home_show = IntegerField()
    active = IntegerField()

    def validate_site_name(self, field):
        if field.name in get_request_field():
            if not field.data:
                raise ValidationError("请输入网站名称")
            if not between(field.data, 0, 100):
                raise ValidationError("网站名称长度最大100位")
            if Link.query.filter_by(site_name=field.data).filter(Link.id != self.id).first():
                raise ValidationError("网站名称已经存在")

    def validate_label(self, field):
        if field.name in get_request_field():
            if field.data:
                if not between(field.data, 0, 255):
                    raise ValidationError("网站说明长度最大255位")

    def validate_site_admin_phone(self, field):
        if field.name in get_request_field():
            if field.data:
                regex = re.compile(r'^[1][3,4,5,7,8][0-9]{9}$')
                if not regex.match(field.data):
                    raise ValidationError('手机格式不正确')

    def validate_site_admin_qq(self, field):
        if field.name in get_request_field():
            if field.data:
                regex = re.compile(r'^\d{5,12}$')
                if not regex.match(field.data):
                    raise ValidationError('qq号码为5位以上数字')
