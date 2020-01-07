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


class Menu(Base):
    """
    后台菜单表
    """
    __tablename__ = "menus"

    name = db.Column(db.String(20), nullable=False, comment="菜单名称", unique=True)
    label = db.Column(db.String(255), nullable=True, default="", comment="菜单说明")
    level = db.Column(db.Integer(), default=0, comment="排序")
    pid = db.Column(db.Integer(), default=0, comment="父级节点id")
    icon = db.Column(db.String(20), nullable=True, default="", comment="图标")
    endpoint_name = db.Column(db.String(50), nullable=True, default="", comment="endpoint名称")
    target = db.Column(db.Boolean(), default=0, comment="新窗口打开")


    @classmethod
    def _query_search(cls, query, _keyword):
        if _keyword is not None:
            keyword = '%' + str(_keyword) + '%'
            return query.filter(or_(cls.name.like(keyword), cls.label.like(keyword),
                                    cls.endpoint_name.like(keyword)))
        return query




