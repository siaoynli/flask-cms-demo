"""
created  by  hzwlxy  at 2018/7/4 11:27
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： api 模块
"""

__author__ = '西瓜哥'


class ApiBluePrint:
    def __init__(self, name):
        self.name = name
        self.mounds = []

    def route(self, rule, **options):
        def decorator(f):
            self.mounds.append((f, rule, options))
            return f

        return decorator

    def register(self, blueprint, url_prefix=None):
        if url_prefix is None:
            url_prefix = "".join(('/', self.name))

        for f, rule, options in self.mounds:
            endpoint = options.pop("endpoint", f.__name__)
            blueprint.add_url_rule(''.join((url_prefix, rule)), endpoint, f, **options)
