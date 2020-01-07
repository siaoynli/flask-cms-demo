"""
created  by  hzwlxy  at 2018/7/10 10:31
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import request, json

__author__ = '西瓜哥'

from app.libs.exception import ApiException


class AjaxResponse(ApiException):
    code = 200
    message = "success"
    error_code = 0
    redirect_to = ''
    data = {}

    def __init__(self, code=None, error_code=None, message=None, redirect_to=None, data=None):
        if code:
            self.code = code
        if message:
            self.message = message
        if error_code:
            self.error_code = error_code
        if redirect_to:
            self.redirect_to = redirect_to
        if data:
            self.data = data
        super(AjaxResponse, self).__init__(code=self.code, error_code=self.error_code, message=self.message)

    def get_body(self, environ=None):
        body = dict(
            error_code=self.error_code,
            message=self.message,
            request=request.method,
            url=self.get_url_no_param(),
            redirect_to=self.redirect_to,
            data=self.data
        )
        return json.dumps(body)


class Success(AjaxResponse):
    code = 200
    error_code = 0


class Fail(AjaxResponse):
    code = 200
    message = ""
    error_code = 1




