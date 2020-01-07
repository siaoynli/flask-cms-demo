"""
created  by  hzwlxy  at 2018/6/21 15:38
__author__: 西瓜哥
__QQ__ : 120235331
不支持python3.7
"""
# 队列也可以使用新的app，但是mail之类要重新注册到app里
from celery import Celery
from flask_mail import Message

__author__ = '西瓜哥'
from app import create_app
from app.libs.helper import read_ini_file

app = create_app()
mail = app.extensions['mail']
db = app.extensions['sqlalchemy']


def make_celery(app):
    system = read_ini_file('system', app.root_path)
    celery = Celery(app.import_name, backend=system['celery_broker_url'],
                    broker=system['celery_result_backend'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(app)


@celery.task
def send_email(to, subject, body):
    msg = Message(subject=subject, sender="120235331@qq.com",
                  recipients=[to])
    msg.body = body
    mail.send(msg)
    print("发送成功")
