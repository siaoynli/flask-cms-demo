"""
created  by  hzwlxy  at 2018/7/3 14:08
__author__: 西瓜哥
__QQ__ : 120235331
__Note__: sqlalchemy 一些方法重写
"""
from flask import current_app
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from contextlib import contextmanager

__author__ = '西瓜哥'

from app.libs.layui_response import Fail


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self, throw=True):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            current_app.logger.exception('%r' % e)
            if throw:
                raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'is_delete' not in kwargs.keys():
            kwargs['is_delete'] = 0
        return super(Query, self).filter_by(**kwargs)

    def api_get_or_404(self, ident):
        rv = self.get(ident)
        if rv is None:
            raise Fail(message="找不到该记录！")
        return rv

    def api_first_or_404(self):

        rv = self.first()
        if rv is None:
            raise Fail(message="找不到该记录！")
        return rv
