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



class Permission(Base):
    """
    权限表
    """
    __tablename__ = "permissions"

    name = db.Column(db.String(20), nullable=False, comment="权限名称", unique=True)
    endpoint_name = db.Column(db.String(20), nullable=False, comment="endpoint名称", unique=True)
    label = db.Column(db.String(20), nullable=True, default="", comment="权限说明")
    level = db.Column(db.Integer(), default=0, comment="排序")
    menu_id = db.Column(db.Integer(), db.ForeignKey('menus.id'), default=0, comment="后台菜单ID")

    menu = db.relationship("Menu", backref=db.backref("permissions",lazy="dynamic"))

    @classmethod
    def _query_search(cls, query, _keyword):
        if _keyword is not None:
            keyword = '%' + str(_keyword) + '%'
            return query.filter(or_(cls.name.like(keyword), cls.label.like(keyword), cls.endpoint_name.like(keyword)))
        return query


