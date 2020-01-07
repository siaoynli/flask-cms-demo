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
from app.models.column import Column
from app.libs.helper import time_now


class Focus(Base):
    """
    焦点图表
    """
    __tablename__ = "focuses"

    title = db.Column(db.String(20), nullable=False, comment="焦点图名称", unique=True)
    label = db.Column(db.String(255), default="", comment="焦点图说明")
    link = db.Column(db.String(100), default="", comment="链接")
    thumb_image = db.Column(db.String(100), default="", comment="缩略图")
    target = db.Column(db.Boolean(), default=0, comment="新窗口打开")
    column_id = db.Column(db.Integer(), db.ForeignKey('columns.id'))
    level = db.Column(db.Integer(), default=0, comment="排序")

    column = db.relationship('Column', backref=db.backref('focuses', lazy="dynamic"))

    @classmethod
    def _query_search(cls, query, _keyword):
        if _keyword is not None:
            keyword = '%' + str(_keyword) + '%'
            return query.filter(or_(cls.title.like(keyword), cls.label.like(keyword), ))
        return query

    def create(self, data):
        with db.auto_commit():
            self.column = Column.query.filter_by(id=data['column_id']).api_first_or_404()
            self.set_attrs(data)
            self.active = 1
            self.created_at = time_now()
            self.updated_at = time_now()
            db.session.add(self)

    def update(self, data, edit_one_field=None):
        """
        edit_one_field 是否表内单个编辑 标识
        :param data:
        :param flag:
        :return:
        """
        with db.auto_commit():
            if not edit_one_field:
                self.column = Column.query.filter_by(id=data['column_id']).api_first_or_404()
                self.set_attrs(data)
            else:
                self.set_attr(data)
            self.updated_at = time_now()

