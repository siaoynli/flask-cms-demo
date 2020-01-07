"""
created  by  hzwlxy  at 2018/7/3 14:41
__author__: 西瓜哥
__QQ__ : 120235331
__Note__: 登录验证
"""
from flask import request
from flask_login import current_user


class Auth:
    _endpoint = None
    _not_auth = set(('login', 'logout', 'get_avatar'))
    _view_name = None

    def __init__(self):
        self._endpoint = request.endpoint.split('.')

    def login_required(self):
        try:
            self._view_name = self._endpoint[1]
        except IndexError:
            return False
        if self._view_name in self._not_auth:
            return True
        if current_user.is_authenticated:
            blueprint = current_user.get_id()
            if request.blueprint in blueprint:
                return True
        return False
