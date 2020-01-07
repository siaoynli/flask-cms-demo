"""
created  by  hzwlxy  at 2018/7/4 11:33
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
import os
from flask import abort, send_from_directory, request, current_app

__author__ = '西瓜哥'

from app.web import upload_app as app
from app.ext import csrf
from app.libs.layui_response import Success, Fail
from app.libs.upload import Upload
from app.libs.image import Images
from app.libs.ueditor import Ueditor

# 上传后的图片访问
@app.route('/<path:filename>')
def load_file(filename):
    if filename == '..' or filename.startswith('../'):
        abort(404)
    try:
        arr = filename.rsplit('/', 1)
        save_path = os.path.join('storage', 'uploads', arr[0])
        filename = arr[1]
        return send_from_directory(save_path, filename)
    except Exception as e:
        abort(404)


@app.route('/avatar', methods=['post'])
def upload_avatar():
    upload_type = request.form.get('file_type', 'images')
    upload = Upload(upload_type=upload_type)
    upload.upload()
    info = upload.info()
    if info['state'] == "SUCCESS":
        # if upload_type == 'images':
        #     Images(old_file_name=info['filename']).clip(dst_w=100, dst_h=100).thumb(width=250, height=250).save()
        return Success(data=info)
    else:
        return Fail(message=info['state'])


@app.route('/thumb', methods=['post'])
def upload_thumb():
    upload_type = request.form.get('file_type', 'images')
    upload = Upload(upload_type=upload_type)
    upload.upload()
    info = upload.info()
    if info['state'] == "SUCCESS":
        if upload_type == 'images':
            Images(old_file_name=info['filename']).thumb(width=640, height=480).save()
        return Success(data=info)
    else:
        return Fail(message=info['state'])


@app.route('/attach', methods=['post'])
def upload_attach():
    upload_type = request.form.get('file_type', 'attach')
    upload = Upload(upload_type=upload_type)
    upload.upload()
    info = upload.info()
    if info['state'] == "SUCCESS":
        return Success(data=info)
    else:
        return Fail(message=info['state'])


@app.route('/ueditor', methods=['get', 'post'])
@csrf.exempt
def upload_ueditor():
    config_path = os.path.join(current_app.static_folder, 'js', 'ueditor', 'config.json')
    ueditor = Ueditor(config_path)
    ueditor.upload()
    output = ueditor.output()
    return output


@app.route('/files', methods=['post'])
def upload_file():
    action = request.form.get('action', 'chunk_upload')
    upload_type = request.form.get('file_type', None)
    promise = {
        'chunk_upload': __chunk_upload,
        'md5check': __md5check,
        'chunk': __chunk,
        'merge': __merge,
    }
    info = promise[action]()
    if info['state'] == "SUCCESS":
        if action == 'merge' and upload_type == "images":
            image = Images(old_file_name=info['filename'])
            image.clip(dst_w=100, dst_h=100).thumb(width=250, height=250).save()
        return Success(data=info)
    else:
        return Fail(message=info['state'])


def __upload():
    upload_type = request.form.get('file_type', None)
    upload = Upload(upload_type=upload_type)
    upload.upload()
    return upload.info()


def __md5check():
    # 查询数据库校验md5
    info = {
        'state': 'SUCCESS',
        'is_file_exist': 0,
    }
    return info


def __chunk_upload():
    upload_type = request.form.get('file_type', None)
    upload = Upload(upload_type=upload_type)
    upload.chunk_upload()
    info = upload.info()
    return info


def __chunk():
    upload_type = request.form.get('file_type', None)
    upload = Upload(upload_type=upload_type)
    upload.chunk()
    return upload.info()


def __merge():
    upload_type = request.form.get('file_type', None)
    upload = Upload(upload_type=upload_type)
    upload.merge()
    return upload.info()
