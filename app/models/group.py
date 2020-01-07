"""
created  by  hzwlxy  at 2018/7/4 14:50
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""

__author__ = '西瓜哥'

from app.ext import db
from app.models.base import Base


class Group(Base):
    """
    用户组
    """
    __tablename__ = "groups"

    name = db.Column(db.String(length=20), nullable=False, comment="用户组名", unique=True)
    label = db.Column(db.String(length=50), nullable=False, comment="用户组介绍", unique=True)

