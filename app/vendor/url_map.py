"""
created  by  hzwlxy  at 2018/7/27 15:58
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from werkzeug.routing import BaseConverter

__author__ = '西瓜哥'


class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        return value

    def to_url(self, value):
        value = super(RegexConverter, self).to_url(value)
        return value
