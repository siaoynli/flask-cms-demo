"""
created  by  hzwlxy  at 2018/7/4 10:42
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 角色表
"""
from flask import request
from sqlalchemy import or_

__author__ = '西瓜哥'

from app.ext import db
from app.models.base import Base
from app.libs.helper import time_now
from .permission import Permission
from .menu import Menu

role_permission = db.Table(
    "role_permission",
    db.Column('permission_id', db.Integer, db.ForeignKey('permissions.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True),
)


class Role(Base):
    """
    角色表
    """
    __tablename__ = "roles"

    name = db.Column(db.String(length=20), nullable=False, comment="角色名", unique=True)
    label = db.Column(db.String(length=50), nullable=False, comment="角色介绍", unique=True)

    permissions = db.relationship('Permission', backref="roles", lazy="dynamic", secondary=role_permission)

    @staticmethod
    def get_menu_for_role():
        return Menu.query.filter_by().filter(Menu.active == 1, Menu.pid > 0).order_by(Menu.level.asc()).all()

    def _get_permissions(self, ids):
        return Permission.query.filter_by().filter(Permission.id.in_(ids),
                                                   Permission.active == 1).all()

    def create(self, data):
        permission_ids = request.form.getlist('permissions[]')
        # 添加时把权限添加进去
        with db.auto_commit():
            self.set_attrs(data)
            self.active = 1
            self.created_at = time_now()
            self.updated_at = time_now()
            if permission_ids:
                self.permissions = self._get_permissions(permission_ids)
            db.session.add(self)

    def update(self, data, edit_one_field=None):
        """
        edit_one_field 是否表内单个编辑 标识
        :param data:
        :param flag:
        :return:
        """
        permission_ids = request.form.getlist('permissions[]')
        # 添加时把权限添加进去

        with db.auto_commit():
            if not edit_one_field:
                self.set_attrs(data)
                self.permissions = self._get_permissions(permission_ids)
            else:
                self.set_attr(data)

    @classmethod
    def _query_search(cls, query, _keyword):
        if _keyword is not None:
            keyword = '%' + str(_keyword) + '%'
            return query.filter(or_(cls.name.like(keyword), cls.label.like(keyword)))
        return query
