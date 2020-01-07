"""
created  by  hzwlxy  at 2018/7/4 10:56
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from sqlalchemy import or_
from flask_login import current_user
from flask import request

__author__ = '西瓜哥'

from app.ext import db
from app.models.base import Base
from app.libs.helper import time_now


class Document(Base):
    """
    文档表
    """
    __tablename__ = "documents"

    uuid = db.Column(db.String(100), nullable=False, comment="别名", unique=True, index=True)
    title = db.Column(db.String(100), nullable=False, comment="文档标题", unique=True)
    use_title = db.Column(db.String(100), comment="文档标题带样式")
    sub_title = db.Column(db.String(100), nullable=False, comment="副标题")
    keyword = db.Column(db.String(255), default="", comment="META关键字")
    description = db.Column(db.String(255), default="", comment="META描述")
    label = db.Column(db.String(255), default="", comment="摘要")
    external_link = db.Column(db.String(100), default="", comment="外部链接")
    published_at = db.Column(db.DateTime(), default="", comment="发布时间")
    thumb_image = db.Column(db.String(100), default="", comment="缩略图")
    author = db.Column(db.String(20), default="", comment="作者")
    source = db.Column(db.String(100), default="", comment="来源")
    source_link = db.Column(db.String(100), default="", comment="来源链接")
    attribute = db.Column(db.String(100), default="", comment="属性")
    content = db.Column(db.Text(), default="", comment="正文")
    tags = db.Column(db.String(100), default="", comment="标签", index=True)
    target = db.Column(db.Boolean(), default=0, comment="新窗口打开")
    click = db.Column(db.Integer(), default=0, comment="阅读数")
    editor = db.Column(db.String(100), default="", comment="编辑")
    is_original = db.Column(db.Boolean(), default=0, comment="是否原创")
    open_comment = db.Column(db.Boolean(), default=0, comment="允许评论")
    attach_file = db.Column(db.String(100), default="", comment="附件地址")
    attach_name = db.Column(db.String(100), default="", comment="附件名称")

    column_id = db.Column(db.Integer(), db.ForeignKey('columns.id'), comment="栏目id")
    admin_id = db.Column(db.Integer(), db.ForeignKey('admins.id'), comment="管理员id")

    column = db.relationship('Column', backref=db.backref('documents', lazy="dynamic"))
    admin = db.relationship('Admin', backref=db.backref('documents', lazy="dynamic"))

    login_show = db.Column(db.Boolean(), default=0, comment="登录可见")
    password_txt = db.Column(db.String(100), default=0, comment="不为空为密码可见")
    user_group = db.Column(db.Boolean(), default=0, comment="VIP可见")

    @classmethod
    def _query_search(cls, query, _keyword):
        if _keyword is not None:
            keyword = '%' + str(_keyword) + '%'
            return query.filter(or_(cls.title.like(keyword), cls.label.like(keyword), cls.keyword.like(keyword),
                                    cls.description.like(keyword), cls.author.like(keyword), ))
        return query

    def create(self, data):
        attributes = request.form.getlist('attribute[]')
        with db.auto_commit():
            self.set_attrs(data)
            self.active = 1
            self.admin = current_user
            self.attribute = ",".join(attributes)
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
        attributes = request.form.getlist('attribute[]')
        with db.auto_commit():
            if not edit_one_field:
                self.set_attrs(data)
                self.attribute = ",".join(attributes)
            else:
                self.set_attr(data)
            self.updated_at = time_now()
