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

document_tag = db.Table(
    "document_tag",
    db.Column('document_id', db.Integer, db.ForeignKey('documents.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True),
)


class Tag(Base):
    """
   标签表
    """
    __tablename__ = "tags"
    title = db.Column(db.String(255), nullable=False, comment="标签文字")
    type = db.Column(db.String(20), nullable=False, default="document", comment="标签类型")

    @classmethod
    def _query_search(cls, query, _keyword):
        if _keyword is not None:
            keyword = '%' + str(_keyword) + '%'
            return query.filter(or_(cls.title.like(keyword), ))
        return query
