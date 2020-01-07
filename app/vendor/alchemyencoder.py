"""
created  by  hzwlxy  at 2018/7/13 10:06
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
import time
import datetime, json
from sqlalchemy.ext.declarative import DeclarativeMeta

__author__ = '西瓜哥'


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:

                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:  # 添加了对datetime的处理
                    if isinstance(data, datetime.datetime):
                        fields[field] = str(data)
                    elif isinstance(data, datetime.date):
                        fields[field] = str(data)
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (datetime.datetime.min + data).time().isoformat()
                    elif isinstance(data.__class__,DeclarativeMeta):
                        fields[field] = json.dumps(data, cls=AlchemyEncoder)
                    else:
                        fields[field] = None
            return fields

        return json.JSONEncoder.default(self, obj)
