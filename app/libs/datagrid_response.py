"""
created  by  hzwlxy  at 2018/7/13 10:19
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
import json
from flask import Response

__author__ = '西瓜哥'

from app.vendor.alchemyencoder import AlchemyEncoder
from app.libs.exception import ApiException


class LayuiResponse(ApiException):
    code = 0
    message = ""
    data = {}
    count = 0
    error_code = 0

    def __init__(self, code=None, message=None, data=None, count=None):
        if code:
            self.code = code
        if message:
            self.message = message
        if data:
            self.data = data
        if count:
            self.count = count
        super(LayuiResponse, self).__init__(code=self.code, error_code=self.error_code, message=self.message)

    def get_body(self, environ=None):

        body = dict(
            code=self.code,
            count=self.count,
            msg=self.message,
            data=self.data
        )
        # data是sqlalchemy对象，需要特殊处理
        return json.dumps(body, cls=AlchemyEncoder)

    def get_response(self, environ=None):

        if self.response is not None:
            return self.response
        headers = self.get_headers(environ)
        return Response(self.get_body(environ), 200, headers)


class AjaxResponse(LayuiResponse):
    pass
