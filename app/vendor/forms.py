#!/usr/bin/env python
# _*_coding:utf-8_*_
# __author__ = 'Administrator'

from wtforms import IntegerField as _IntegerField


class SignlessIntegerField(_IntegerField):

    def process_formdata(self, valuelist):
        if valuelist:
            try:
                if valuelist[0].isdigit():
                    self.data = int(valuelist[0])
                else:
                    self.data = None
                    raise ValueError(self.gettext('请输入正整数'))
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('请输入正整数'))
