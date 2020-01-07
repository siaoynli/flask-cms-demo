"""
created  by  hzwlxy  at 2018/7/4 10:56
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from sqlalchemy import or_

__author__ = '西瓜哥'

from app.ext import db
from app.models.base import Base


class Message(Base):
    """
    短信表
    """
    __tablename__ = "messages"

    content = db.Column(db.String(255), nullable=False, comment="短信内容", )
    user_id = db.Column(db.Integer(), default=0, comment="短信发布者")
    username = db.Column(db.String(20), nullable=False, comment="短信发布者用户名")
    ip = db.Column(db.String(20), default="", comment="ip地址")
    published_at = db.Column(db.DateTime(), default="", comment="发布时间")
    pid = db.Column(db.Integer(), default=0, comment="所属短信id")
    label = db.Column(db.String(100), default="", comment="预留")

    @classmethod
    def _query_search(cls, query, _keyword):
        if _keyword is not None:
            keyword = '%' + str(_keyword) + '%'
            return query.filter(or_(cls.content.like(keyword), cls.username.like(keyword), ))
        return query
