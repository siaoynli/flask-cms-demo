"""
created  by  hzwlxy  at 2018/7/12 17:29
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
from flask import  render_template
from flask_mail import current_app
from flask_mail import Message

__author__ = '西瓜哥'

from app.web import web_app as app
from app.libs.image import Images
from tasks import send_email


@app.route('/')
def index():
    return render_template('home/index/index.html')


@app.route('/test')
def test():
    image = Images(old_file_name="uploads/images/2018-07-19/1e5e0a27f4bfd1d1378744eeefc51048.jpg")
    image.thumb().water().save(new_filename="uploads/images/2018-07-19/aa.jpg")
    return '图片ok'


@app.route("/mail")
def mail():
    # app=current_app._get_current_object()
    # mail = current_app.extensions['mail']
    # msg = Message(subject='Email test by flask-email', sender="120235331@qq.com",
    #               recipients=['siaoynli@126.com'])
    # msg.body = 'hello test'
    # msg.html = '<b>测试Flask发送邮件<b>'
    # mail.send(msg)
    send_email.delay('siaoynli@126.com', "新的标题2", "新的信息2")
    return 'ok'


@app.route('/test/<regex("\d+"):nid>')
def user_show(nid):
    return nid
