"""
created  by  hzwlxy  at 2018/7/3 11:25
__author__: 西瓜哥
__QQ__ : 120235331
__Note__: ORM 模型和表映射
"""
from app.ext import login_manager

__author__ = '西瓜哥'

from .role import Role
from .permission import Permission
from .admin import Admin
from .user import User
from .group import Group
from .menu import Menu
from .system import System
from .mail import Mail
from .column import Column
from .document import Document
from .focus import Focus
from .link import Link
from .message import Message
from .guestbook import Guestbook
from .note import Note
from .tag import Tag


# 验证登录
@login_manager.user_loader
def load_user(user_id):
    temp = user_id.split('.')
    try:
        uid = temp[1]
        if temp[0] == 'admin':
            return Admin.query.get(uid)
        elif temp[0] == 'user':
            return User.query.get(uid)
        else:
            return None
    except IndexError:
        return None
