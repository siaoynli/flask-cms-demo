"""
created  by  hzwlxy  at 2018/7/3 14:09
__author__: 西瓜哥
__QQ__ : 120235331
"""
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf import CSRFProtect

__author__ = '西瓜哥'

from app.vendor.sqlalchemy import SQLAlchemy, Query

db = SQLAlchemy(query_class=Query)
login_manager = LoginManager()
csrf = CSRFProtect()
mail = Mail()
