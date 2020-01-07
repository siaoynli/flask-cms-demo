"""
created  by  hzwlxy  at 2018/7/4 10:38
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 管理員表
"""
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

__author__ = '西瓜哥'
from app.ext import db
from app.models.base import Base


class User(Base, UserMixin):
    """
   用户表
    """
    __tablename__ = "users"

    name = db.Column(db.String(length=20), nullable=False, comment="用户名", index=True, unique=True)
    email = db.Column(db.String(length=20), nullable=False, comment="用户邮箱", index=True, unique=True)
    """
    属性名用 _password ，创建的字段未password
    """
    _password = db.Column('password', db.String(length=128), nullable=False, comment="密码")
    nick_name = db.Column(db.String(length=20), default='', comment="昵称")
    chinese_name = db.Column(db.String(length=20), default='', comment="中文姓名")
    avatar = db.Column(db.String(length=100), default='', comment="头像")
    sex = db.Column(db.Boolean(), comment="性别", default=0)
    phone = db.Column(db.String(length=20), default='', comment="电话", index=True, unique=True)
    qq = db.Column(db.String(length=20), default='', comment="QQ")
    remarks = db.Column(db.String(length=255), default='', comment="备注")
    login_ip = db.Column(db.String(length=20), default='', comment="登录ip")
    login_time = db.Column(db.String(length=20), default='', comment="登录时间")
    login_count = db.Column(db.Integer(), default=0, comment="登录次数")
    integral = db.Column(db.Integer(), default=0, comment="积分")
    group_id = db.Column(db.Integer(), db.ForeignKey("groups.id"))

    # 属性的getter
    @property
    def password(self):
        return self._password

    # 属性的setter
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 校验密码
    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    # get_id 返回str字符串，通过 user 来做标识
    def get_id(self):
        return 'user.' +str( self.id)
