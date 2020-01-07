"""
created  by  hzwlxy  at 2018/7/27 13:54
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
__author__ = '西瓜哥'
from app.libs.helper import read_ini_file

config = read_ini_file(field="database")


class Config:
    DEBUG = False
    SECRET_KEY = 'k9kcOdx8r8ei&7k@Z$rCay^ik!OuhhqFbr4fJ7MXaHWBomk#m2Zgm5mGisX@'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(Config):
    DEBUG = False
    TEMPLATES_AUTO_RELOAD = False
    SQLALCHEMY_DATABASE_URI = "{dbtype}://{username}:{password}@{host}:{port}/{dbname}".format(
        dbtype=config['DB_CONNECTION'], username=config['DB_USERNAME'], password=config['DB_PASSWORD'],
        host=config['DB_HOST'], port=config['DB_PORT'], dbname=config['DB_DATABASE'])


class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = "{dbtype}://{username}:{password}@{host}:{port}/{dbname}".format(
        dbtype=config['DB_CONNECTION'], username=config['DB_USERNAME'], password=config['DB_PASSWORD'],
        host=config['DB_HOST'], port=config['DB_PORT'], dbname=config['DB_DATABASE'])

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///{dbname}'.format(dbname=config['DB_DATABASE'] + '.sqlite3')
