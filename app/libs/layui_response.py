"""
created  by  hzwlxy  at 2018/7/10 10:31
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import json, Response

__author__ = '西瓜哥'

from app.libs.exception import ApiException


class LayuiResponse(ApiException):
    code = 0
    message = "success"
    data = {}
    error_code = 0

    def __init__(self, code=None, message=None, data=None, error_code=None):
        if code:
            self.code = code
        if message:
            self.message = message
        if data:
            self.data = data
        if error_code:
            self.error_code = error_code
        super(LayuiResponse, self).__init__(code=self.code, error_code=self.error_code, message=self.message)

    def get_body(self, environ=None):
        body = dict(
            code=self.code,
            error_code=self.error_code,
            msg=self.message,
            data=self.data
        )
        return json.dumps(body)

    def get_response(self, environ=None):

        if self.response is not None:
            return self.response
        headers = self.get_headers(environ)
        return Response(self.get_body(environ), 200, headers)


class Success(LayuiResponse):
    error_code = 0


class Fail(LayuiResponse):
    error_code = 1

