"""
created  by  hzwlxy  at 2018/7/3 14:28
__author__: 西瓜哥
__QQ__ : 120235331
__Note__: 自定义异常类
"""
from flask import request, json
from werkzeug.exceptions import HTTPException

__author__ = '西瓜哥'


class ApiException(HTTPException):
    code = 500
    message = "未知错误"
    error_code = 1000

    def __init__(self, code=None, error_code=None, message=None):
        if code:
            self.code = code
        if message:
            self.message = message
        if error_code:
            self.error_code = error_code
        super(ApiException, self).__init__(description=self.message, response=None)

    def get_body(self, environ=None):
        body = dict(
            error_code=self.error_code,
            message=self.message,
            request=request.method,
            url=self.get_url_no_param()
        )
        return json.dumps(body)

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]


class Success(ApiException):
    code = 200
    message = "success"
    error_code = 0
