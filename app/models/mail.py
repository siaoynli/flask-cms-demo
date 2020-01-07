"""
created  by  hzwlxy  at 2018/7/4 10:56
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""

__author__ = '西瓜哥'

from app.ext import db
from app.models.base import Base


class Mail(Base):
    """
    网站配置表
    """
    __tablename__ = "mails"

    mail_server = db.Column(db.String(100), nullable=False, comment="邮箱服务器")
    port = db.Column(db.Integer(), default=0, comment="端口")
    link_model = db.Column(db.String(10), default=0, comment="连接类型")
    username = db.Column(db.String(100), nullable=False, comment="邮箱用户名")
    password = db.Column(db.String(100), nullable=False, comment="邮箱密码或秘钥")
