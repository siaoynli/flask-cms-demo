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


class Link(Base):
    """
    友情链接表
    """
    __tablename__ = "links"

    site_name = db.Column(db.String(20), nullable=False, comment="网站名称", unique=True)
    site_url = db.Column(db.String(100), default="", comment="网址")
    label = db.Column(db.String(255), default="", comment="网站说明")
    logo = db.Column(db.String(100), default="", comment="网站logo")
    site_admin = db.Column(db.String(20), default="", comment="网站管理员")
    site_admin_email = db.Column(db.String(100), default="", comment="网站管理员邮箱")
    site_admin_qq = db.Column(db.String(20), default="", comment="网站管理员QQ")
    site_admin_phone = db.Column(db.String(20), default="", comment="网站管理员电话")
    home_show = db.Column(db.Boolean(), default=0, comment="首页显示")
    level = db.Column(db.Integer(), default=0, comment="排序")

    @classmethod
    def _query_search(cls, query, _keyword):
        if _keyword is not None:
            keyword = '%' + str(_keyword) + '%'
            return query.filter(or_(cls.site_name.like(keyword), cls.site_admin.like(keyword),
                                    cls.site_admin_email.like(keyword), cls.site_admin_qq.like(keyword),
                                    cls.site_admin_phone.like(keyword), cls.label.like(keyword), ))
        return query
