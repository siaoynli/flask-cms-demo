"""
created  by  hzwlxy  at 2018/7/10 11:13
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from wtforms import Form

__author__ = '西瓜哥'


class Base(Form):

    def __init__(self, formdata=None, obj=None, prefix='', data=None, meta=None, id=None, **kwargs):
        self.id = id
        super(Base, self).__init__(formdata=formdata, obj=obj, prefix=prefix, data=data, meta=meta, **kwargs)

    @property
    def first_error(self):
        """
        循环出form 第一个error信息并返回
        :return:
        """
        for k, v in self.errors.items():
            return v[0]
