"""
created  by  hzwlxy  at 2018/7/4 10:56
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from sqlalchemy import or_
from flask_login import current_user

__author__ = '西瓜哥'

from app.ext import db
from app.models.base import Base
from app.libs.helper import time_now


class Note(Base):
    """
   公告表
    """
    __tablename__ = "notes"

    content = db.Column(db.String(255), nullable=False, comment="公告内容")
    level = db.Column(db.Integer(), default=0, comment="排序")
    start_date = db.Column(db.Date(), default="", comment="起始时间")
    end_date = db.Column(db.Date(), default="", comment="结束时间")

    admin_id = db.Column(db.Integer(), db.ForeignKey('admins.id'))

    admin = db.relationship('Admin', backref=db.backref('notes', lazy="dynamic"))

    @classmethod
    def _query_search(cls, query, _keyword):
        if _keyword is not None:
            keyword = '%' + str(_keyword) + '%'
            return query.filter(or_(cls.content.like(keyword), ))
        return query

    def create(self, data):
        with db.auto_commit():
            self.set_attrs(data)
            self.active = 1
            self.admin = current_user
            self.created_at = time_now()
            self.updated_at = time_now()
            db.session.add(self)
