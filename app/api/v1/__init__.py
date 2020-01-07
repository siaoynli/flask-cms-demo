"""
created  by  hzwlxy  at 2018/7/4 11:27
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import Blueprint

__author__ = '西瓜哥'

from app.api.v1 import user


def create_blueprint():
    bp = Blueprint('v1', "__name__", url_prefix='/v1')
    user.api.register(bp)

    return bp
