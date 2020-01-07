"""
created  by  hzwlxy  at 2018/7/3 14:49
__author__: 西瓜哥
__QQ__ : 120235331
"""
from flask import request
from sqlalchemy import func

__author__ = '西瓜哥'
from app.ext import db
from app.libs.helper import get_request_field, time_now, array_sort_by_pid, list_result_with_html, array_sort_to_tree, \
    array_sort_by_pid_whitespace


class Base(db.Model):
    """
    __abstract__设置为True,不会创建Base表
    """
    __abstract__ = True

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, comment="id")
    is_delete = db.Column(db.Boolean(), index=True, default=0, nullable=False, comment="软删除，0未删除，1删除")
    active = db.Column('is_active', db.Boolean(), index=True, default=0, nullable=False, comment="状态")
    created_at = db.Column(db.DateTime(), nullable=True, comment="创建时间")
    updated_at = db.Column(db.DateTime(), nullable=True, comment="修改时间")

    @classmethod
    def get_limit_all(cls):
        limit = int(request.args.get('limit', 10))
        page = int(request.args.get('page', 1))
        field = request.args.get('field', 'id')
        order = request.args.get('order', 'desc')
        _keyword = request.args.get('keyword', None)
        query = cls.query.filter(cls.is_delete == 0)
        query = cls._query_search(query, _keyword)

        if field and order:
            _obj = getattr(cls, field)
            if order == 'desc':
                query = query.order_by(_obj.desc())
            else:
                query = query.order_by(_obj.asc())
        total = query.with_entities(func.count(cls.id)).scalar()
        result = query.limit(limit).offset((page - 1) * limit).all()
        return total, result

    @classmethod
    def get_list_all(cls, is_sort=False):
        """
        不分页，is_sort 指定是否根据pid排序
        :param is_sort:
        :return:
        """
        _keyword = request.args.get('keyword', None)

        query = cls.query.filter(cls.is_delete == 0)
        query = cls._query_search(query, _keyword)
        total = query.with_entities(func.count(cls.id)).scalar()
        result = query.all()
        if _keyword:
            is_sort = False
        # 搜索的话,结果的 html设置为"" ,防止table渲染问题
        result = array_sort_by_pid(result) if is_sort else list_result_with_html(result)
        return total, result

    @classmethod
    def get_all_for_select(cls, is_group=False):
        # is_group 是否分组
        result = cls.query.filter_by().all()
        return array_sort_by_pid_whitespace(result) if is_group else result

    @classmethod
    def get_all(cls, is_group=False):
        # is_group 是否分组
        result = cls.query.filter_by().all()
        return array_sort_to_tree(result) if is_group else result

    @classmethod
    def get_all_in_ids(cls, ids=list()):
        return cls.query.filter(cls.id.in_(ids), cls.is_delete == 0).all()

    def create(self, data):

        with db.auto_commit():
            self.set_attrs(data)
            self.active = 1
            self.created_at = time_now()
            self.updated_at = time_now()
            db.session.add(self)

    def update(self, data, edit_one_field=None):
        """
        edit_one_field 是否表内单个编辑 标识
        :param data:
        :param flag:
        :return:
        """
        with db.auto_commit():
            if not edit_one_field:
                self.set_attrs(data)
            else:
                self.set_attr(data)
            self.updated_at = time_now()

    def destroy(self):
        with db.auto_commit():
            self.is_delete = 1

    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                if value is None:
                    setattr(self, key, 0)
                elif isinstance(value, str):
                    setattr(self, key, value.strip())
                else:
                    setattr(self, key, value)

    def set_attr(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id' and key in get_request_field():
                if isinstance(value, str):
                    setattr(self, key, value.strip())
                else:
                    setattr(self, key, value)

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).api_first_or_404()

    @classmethod
    def get_all_except_by_id(cls, id, is_sort=True):
        """
        查询除了某个id之外的所有结果
         is_sort是根据pid排序，id和未激活的子集都会清除
        :param id:
        :param is_sort:
        :return:
        """
        result = cls.query.filter_by().filter(cls.id != id, cls.active == 1).all()
        return array_sort_by_pid_whitespace(result) if is_sort else result
