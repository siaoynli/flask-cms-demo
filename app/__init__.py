"""
created  by  hzwlxy  at 2018/7/3 11:24
__author__: 西瓜哥
__QQ__ : 120235331
"""
from flask import Flask

__author__ = '西瓜哥'
from app.libs.helper import read_ini_file
from app.vendor.url_map import RegexConverter


def create_app():
    app = Flask(__name__)
    # 路由支持正则
    app.url_map.converters['regex'] = RegexConverter
    app.config.from_object("app.setting.DevelopmentConfig")
    from app.ext import db, login_manager, mail, csrf
    csrf.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.session_protection = 'strong'
    login_manager.blueprint_login_views = {
        'user': "user.login",
        'admin': "admin.login",
    }
    update_config(app)
    register_blueprint(app)

    return app


def update_config(app):
    mail = read_ini_file('mail')
    tls = True if mail['link_model'] == 'tls' else False
    ssl = True if mail['link_model'] == 'ssl' else False
    app.config.update(
        MAIL_SERVER=mail['mail_server'],
        MAIL_PORT=int(mail['port']),
        MAIL_USERNAME=mail['username'],
        MAIL_PASSWORD=mail['password'],
        MAIL_USE_TLS=tls,
        MAIL_USE_SSL=ssl,
    )


def register_blueprint(app):
    from app.web import admin_app, user_app, web_app, upload_app
    from app.api.v1 import create_blueprint
    app.register_blueprint(web_app)
    app.register_blueprint(user_app)
    app.register_blueprint(admin_app)
    app.register_blueprint(upload_app)
    app.register_blueprint(create_blueprint())
