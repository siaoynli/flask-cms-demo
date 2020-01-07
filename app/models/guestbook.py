"""
created  by  hzwlxy  at 2018/7/4 10:56
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask_login import current_user
from sqlalchemy import or_, func

__author__ = '西瓜哥'

from app.ext import db
from app.models.base import Base
from app.libs.helper import time_now, get_client_ip, array_sort_by_pid, list_result_with_html


class Guestbook(Base):
    """
    留言表
    """
    __tablename__ = "guestbooks"

    content = db.Column(db.String(255), nullable=False, comment="留言内容", )
    user_id = db.Column(db.Integer(), default=0, comment="留言者")
    user_type = db.Column(db.String(5), default="user", comment="用户类型")
    username = db.Column(db.String(20), default="游客", comment="留言着用户名")
    ip = db.Column(db.String(20), default="", comment="ip地址")
    published_at = db.Column(db.DateTime(), default="", comment="留言时间")
    pid = db.Column(db.Integer(), default=0, comment="所属父级留言id")
    root_id = db.Column(db.String(255),index=True, default=0, comment="节点数据")
    open_comment = db.Column(db.Boolean(), default=0, comment="允许回复我留言")
    good = db.Column(db.Integer(), default=0, comment="点赞")
    read = db.Column(db.Integer(), default=0, comment="是否已读")
    label = db.Column(db.String(100), default="", comment="预留")

    @classmethod
    def _query_search(cls, query, _keyword):
        if _keyword is not None:
            keyword = '%' + str(_keyword) + '%'
            return query.filter(or_(cls.content.like(keyword), cls.username.like(keyword), ))
        return query

    def create(self, data):
        with db.auto_commit():
            self.set_attrs(data)
            self.active = 1
            self.open_comment = 1
            self.ip = get_client_ip()
            self.user_id = current_user.id
            self.username = current_user.name
            self.user_type = 'admin'
            self.published_at = time_now()
            self.created_at = time_now()
            self.updated_at = time_now()
            db.session.add(self)

    @classmethod
    def get_list_all_by_id(cls, id=id):
        query = cls.query.filter(cls.is_delete == 0, cls.root_id.like('%' + str(id) + '%'))
        total = query.with_entities(func.count(cls.id)).scalar()
        result = query.all()
        result = array_sort_by_pid(arrays=result, html="", pid=int(id))
        return total, result

    @classmethod
    def get_by_root_id(cls, root_id=root_id):
        return cls.query.filter(cls.is_delete == 0, cls.root_id == root_id).first()
