"""
created  by  hzwlxy  at 2018/7/3 15:13
__author__: 西瓜哥
__QQ__ : 120235331
__Note__: 自定义命令
"""
from flask_script import Manager

__author__ = '西瓜哥'
from app.ext import db
from app.models.admin import Admin
from app.models.role import Role
from app.models.user import User
from app.models.group import Group
from app.models.menu import Menu

CustomCommand = Manager()


@CustomCommand.option('-n', '--name', dest='name', default='超级管理员', help=("请设置角色名称"))
@CustomCommand.option('-l', '--label', dest='label', default='超级管理员', help=("请设置角色介绍"))
def create_role(name, label):
    """
    设置角色
    :param name:
    :param label:
    :return:
    """
    with db.auto_commit():
        role = Role()
        role.name = name
        role.label = label
        db.session.add(role)
    print("成功创建管理员角色: %s " % (name,))


@CustomCommand.option('-n', '--name', dest='name', default='admin', help=("请设置管理员用户名"))
@CustomCommand.option('-p', '--password', dest='password', default='123456', help=("请设置密码"))
@CustomCommand.option('-e', '--email', dest='email', default='admin@admin.com', help=("请设置邮箱"))
def create_admin(name, password, email):
    """
    设置管理员
    :param name:
    :param password:
    :param email:
    :return:
    """
    with db.auto_commit():
        admin = Admin()
        admin.name = name
        admin.password = password
        admin.email = email
        admin.avatar = '/static/admin/images/guest.png'
        admin.role = Role.query.get(1)
        db.session.add(admin)
    print("成功添加管理员,用户名:%s 密码:%s 邮箱：%s" % (name, password, email))


@CustomCommand.option('-n', '--name', dest='name', default='游客', help=("请设置用户分组"))
@CustomCommand.option('-l', '--label', dest='label', default='游客', help=("请设置用户分组介绍"))
def create_group(name, label):
    """
    设置用户分组
    :param name:
    :param label:
    :return:
    """
    with db.auto_commit():
        group = Group()
        group.name = name
        group.label = label
        db.session.add(group)
    print("成功创建用户分组：%s " % (name,))


@CustomCommand.option('-n', '--name', dest='name', default='test001', help=("请设置用户名"))
@CustomCommand.option('-p', '--password', dest='password', default='123456', help=("请设置密码"))
@CustomCommand.option('-e', '--email', dest='email', default='test001@admin.com', help=("请设置邮箱"))
def create_user(name, password, email):
    """
    设置用户
    :param name:
    :param password:
    :param email:
    :return:
    """
    with db.auto_commit():
        user = User()
        user.name = name
        user.password = password
        user.email = email
        user.avatar = '/static/user/images/guest.png'
        user.group = Group.query.get(1)
        db.session.add(user)
    print("成功添加用户,用户名:%s 密码:%s 邮箱：%s" % (name, password, email))


@CustomCommand.option('-n', '--name', dest='name', default='后台导航', help=("请设置导航名称"))
@CustomCommand.option('-e', '--endpoint', dest='endpoint', default='menu_index', help=("请设置endpoint名称"))
def create_menu(name, endpoint):
    """
    设置角色
    :param name:
    :param label:
    :return:
    """
    with db.auto_commit():
        menu = Menu()
        menu.name = name
        menu.endpoint = endpoint
        menu.pid = 0
        menu.active = 1
        menu.target = 1
        db.session.add(menu)
    print("成功创建后台导航: %s " % (name,))
