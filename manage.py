#!/usr/bin/env python3
"""
created  by  hzwlxy  at 2018/7/3 14:13
__author__: 西瓜哥
__QQ__ : 120235331
__Note__: 命令
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

__author__ = '西瓜哥'
from app import create_app
from app.ext import db
from command import CustomCommand
from app import  models

app = create_app()
manager = Manager(app)

Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command('artisan', CustomCommand)

if __name__ == '__main__':
    manager.run()
