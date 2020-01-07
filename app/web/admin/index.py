"""
created  by  hzwlxy  at 2018/7/4 16:06
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import render_template


__author__ = '西瓜哥'

from app.web import admin_app as app


@app.route('/index')
def index():
    return render_template('admin/index/index.html')


@app.route('/console')
def console():
    return render_template('admin/index/console.html')
