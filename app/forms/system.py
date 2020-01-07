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

class SystemForm(Base):
    site_name = StringField(validators=[InputRequired(message="请输入网站名称"), Length(1, 100, message="网站名称长度2-100位")])
    title = StringField(validators=[InputRequired(message="请输入网站标题"), Length(1, 100, message="网站标题长度2-100位")])
    keyword = StringField(validators=[InputRequired(message="请输入META关键词"), Length(6, 255, message="META关键词长度6-255位")])
    description = StringField(validators=[InputRequired(message="请输入META描述"), Length(6, 255, message="META描述长度6-255位")])
    icp = StringField(validators=[Length(0, 100, message="备案信息长度最大100位")])
    census_code = StringField(validators=[Length(0, 255, message="统计代码长度最大255位")])
    copyright = StringField(validators=[Length(0, 255, message="版权信息长度最大255位")])
    upload_path = StringField(
        validators=[InputRequired(message="请输入上传路径"), Length(0, 255, message="请输入上传路径长度最大100位")])
    images_water = StringField(validators=[Length(0, 255, message="水印文件长度最大255位")])
    water_type = SelectField(choices=[('image', '图片'), ('txt', '文字')])
    txt_water = StringField()
    txt_water_size = IntegerField()
    txt_water_font = StringField()
    txt_water_color = StringField()
    images_size = IntegerField(validators=[InputRequired(message="请输入图片大小")])
    images_extensions = StringField(
        validators=[InputRequired(message="请输入图片类型"), Length(0, 255, message="图片类型长度最大255位")])
    images_max_width = IntegerField(validators=[InputRequired(message="请输入图片最大宽度")])
    images_max_height = IntegerField(validators=[InputRequired(message="请输入图片最大高度")])
    media_size = IntegerField(validators=[InputRequired(message="请输入媒体大小")])
    media_extensions = StringField(
        validators=[InputRequired(message="请输入媒体类型"), Length(0, 255, message="媒体类型长度最大255位")])
    video_water = StringField(validators=[Length(0, 255, message="视频水印地址长度最大255位")])
    attach_size = IntegerField(validators=[InputRequired(message="请输入附件大小")])
    attach_extensions = StringField(
        validators=[InputRequired(message="请输入附件类型"), Length(0, 255, message="附件类型长度最大255位")])
    open_comment = IntegerField()
    comment_captcha = IntegerField()
    document_water = IntegerField()
    user_comment = IntegerField()
    guest_comment = IntegerField()
    comment_audit = IntegerField()
    comment_time_interval = IntegerField(validators=[InputRequired(message="请输入评论时间间隔")])
    admin_prefix = StringField(
        validators=[InputRequired(message="请输入后台管理地址"), Length(1, 100, message="后台管理地址最大100位")])
    open_register = IntegerField()
    open_cache = IntegerField()
    cache_time = IntegerField(validators=[InputRequired(message="请输入缓存时间")])
    pagination_number = IntegerField(validators=[InputRequired(message="请输入分页大小")])
    celery_broker_url = StringField(
        validators=[Length(0, 255, message="celery_broker_url长度最大255位")])
    celery_result_backend = StringField(
        validators=[Length(0, 255, message="celery_result_backend长度最大255位")])
