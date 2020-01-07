"""
created  by  hzwlxy  at 2018/7/4 12:58
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""

__author__ = '西瓜哥'

from app.api import ApiBluePrint

api = ApiBluePrint('user')


@api.route('/index')
def index():
    return 'user.index'
