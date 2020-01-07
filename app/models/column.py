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


class Column(Base):
    """
    栏目表
    """
    __tablename__ = "columns"

    title = db.Column(db.String(20), nullable=False, comment="栏目名称", unique=True)
    keyword = db.Column(db.String(255), default="", comment="META关键字")
    description = db.Column(db.String(255), default="", comment="META描述")
    column_type = db.Column(db.String(20), default="", comment="栏目类型")
    thumb_image = db.Column(db.String(100), default="", comment="栏目缩略图")
    label = db.Column(db.String(255), default="", comment="栏目说明")
    external_link = db.Column(db.String(100), default="", comment="外部链接")
    level = db.Column(db.Integer(), default=0, comment="排序")
    pid = db.Column(db.Integer(), default=0, comment="父级节点id")
    target = db.Column(db.Boolean(), default=0, comment="新窗口打开")

    @classmethod
    def _query_search(cls, query, _keyword):
        if _keyword is not None:
            keyword = '%' + str(_keyword) + '%'
            return query.filter(or_(cls.title.like(keyword), cls.keyword.like(keyword),
                                    cls.description.like(keyword), cls.label.like(keyword), ))
        return query

