"""
created  by  hzwlxy  at 2018/7/4 16:06
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""

__author__ = '西瓜哥'

from app.web import user_app as app
from flask_login import current_user


@app.route('/index')
def index():
    print(current_user)
    return 'user.index'
