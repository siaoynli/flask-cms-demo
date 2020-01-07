"""
created  by  hzwlxy  at 2018/7/4 10:56
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""

__author__ = '西瓜哥'

from app.ext import db
from app.models.base import Base


class System(Base):
    """
    网站配置表
    """
    __tablename__ = "systems"

    site_name = db.Column(db.String(100), nullable=False, comment="网站名称", unique=True)
    title = db.Column(db.String(100), nullable=False, comment="网站标题", )
    keyword = db.Column(db.String(100), nullable=False, comment="META关键词", )
    description = db.Column(db.String(100), nullable=False, comment="META描述", )
    icp = db.Column(db.String(100), default="", comment="备案信息", )
    census_code = db.Column(db.String(255), default="", comment="统计代码", )
    copyright = db.Column(db.String(255), default="", comment="版权信息", )
    upload_path = db.Column(db.String(100), default="", comment="上传路径", )
    water_type = db.Column(db.String(10), default='', comment="水印类型", )
    images_water = db.Column(db.String(255), default="", comment="水印文件", )
    txt_water = db.Column(db.String(100), default="", comment="水印文字", )
    txt_water_size = db.Column(db.String(100), default="", comment="水印文字大小", )
    txt_water_font = db.Column(db.String(100), default="", comment="文字水印字体", )
    txt_water_color = db.Column(db.String(20), default="", comment="文字水印颜色", )
    images_size = db.Column(db.Integer(), default=0, comment="最大图片大小", )
    images_extensions = db.Column(db.String(255), default="", comment="图片类型", )
    images_max_width = db.Column(db.Integer(), default=0, comment="图片最大宽度", )
    images_max_height = db.Column(db.Integer(), default=0, comment="图片最大高度", )
    media_size = db.Column(db.Integer(), default=0, comment="媒体大小", )
    media_extensions = db.Column(db.String(255), default="", comment="媒体类型", )
    video_water = db.Column(db.String(255), default="", comment="视频水印地址", )
    attach_size = db.Column(db.Integer(), default=0, comment="附件大小", )
    attach_extensions = db.Column(db.String(255), default="", comment="附件类型", )
    admin_prefix = db.Column(db.String(50), default='', comment="后台访问地址", )
    open_register = db.Column(db.Boolean(), default=0, comment="允许注册", )
    open_comment = db.Column(db.Boolean(), default=0, comment="开启评论", )
    comment_captcha = db.Column(db.Boolean(), default=0, comment="评论开启验证码", )
    document_water = db.Column(db.Boolean(), default=0, comment="文档水印", )
    user_comment = db.Column(db.Boolean(), default=0, comment="开启用户评论", )
    guest_comment = db.Column(db.Boolean(), default=0, comment="开启游客评论", )
    comment_audit = db.Column(db.Boolean(), default=0, comment="评论开启审核", )
    comment_time_interval = db.Column(db.Integer(), default=0, comment="评论时间间隔", )
    open_cache = db.Column(db.Integer(), default=0, comment="开启缓存", )
    cache_time = db.Column(db.Integer(), default=0, comment="缓存时间", )
    pagination_number = db.Column(db.Integer(), default=0, comment="分页大小", )
    celery_broker_url = db.Column(db.String(255), default="", comment="celery 配置 ", )
    celery_result_backend = db.Column(db.String(255), default="", comment="celery 配置 ", )
