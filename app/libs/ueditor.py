"""
created  by  hzwlxy  at 2018/8/31 10:26
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
import json, re, html, base64, os
from flask import request, jsonify, current_app

__author__ = '西瓜哥'
from app.libs.upload import Upload
from app.libs.image import Images
from app.libs.helper import read_ini_file, random_filename, get_upload_abspath, get_upload_path


class Ueditor:
    __result = {}
    __action = ''
    __config_path = ''
    __output = ''
    __system = ''

    def __init__(self, config_path):
        self.__config_path = config_path
        self.__system = read_ini_file('system')

    def upload(self):
        self.__action = request.args.get('action')
        promise = {
            'config': self.__config,
            'uploadimage': self.__uploadimage,
            'uploadscrawl': self.__uploadscrawl,
            'uploadfile': self.__uploadfile,
            'uploadvideo': self.__uploadvideo,
            'listimage': self.__listimage,
            'listfile': self.__listfile,
            'catchimage': self.__catchimage,
        }
        try:
            promise[self.__action]()
        except Exception as e:
            self.__result = {'state': '请求地址出错'}

        callback = request.args.get('callback')
        if callback:
            regex = re.compile(r'^[\w_]+$')
            if regex.match(callback):
                self.__output = html.escape(callback) + '(' + self.__result + ')'
            else:
                self.__result = {'state': 'callback参数不合法'}
        else:
            self.__output = self.__result

    def output(self):

        return jsonify(self.__output)

    def __config(self):
        with open(self.__config_path, 'r', encoding='utf-8') as fp:
            self.__result = json.loads(re.sub(r'\/\*.*\*\/', '', fp.read()))

    def __uploadimage(self):
        upload = Upload(upload_type="images", file_field='upfile')
        upload.upload()
        info = upload.info()
        if info['state'] == "SUCCESS":
            try:
                img = Images(old_file_name=info['filename']).thumb(width=int(self.__system['images_max_width']))
                if int(self.__system['document_water']) == 1:
                    img = img.water()
                img.save()
                self.__result = upload.info()
            except Exception as e:
                self.__result = {'state': '图片压缩失败！'}
        else:
            self.__result = info

    def __uploadscrawl(self):
        base64data = request.form.get("upfile")
        img = base64.b64decode(base64data)
        filename = random_filename('xx.png')
        filepath = os.path.join(
            get_upload_abspath(root_path=current_app.root_path, upload_dir=self.__system['upload_path']), filename)
        with open(filepath, 'wb') as fp:
            fp.write(img)
        path = os.path.join(get_upload_path(upload_dir=self.__system['upload_path']), filename)
        path = path.replace('\\', '/')
        self.__result = {
            'state': 'SUCCESS',
            'original_name': filename,
            'title': filename,
            'ext': 'png',
            "url": '/' + path,
            "filename": path,
        }
        return

    def __uploadfile(self):
        upload = Upload(upload_type="attach", file_field='upfile')
        upload.upload()
        info = upload.info()
        if info['state'] == "SUCCESS":
            self.__result = upload.info()
        else:
            self.__result = info

    def __uploadvideo(self):
        upload = Upload(upload_type="media", file_field='upfile')
        upload.upload()
        info = upload.info()
        if info['state'] == "SUCCESS":
            self.__result = upload.info()
        else:
            self.__result = info

    def __listimage(self):
        self.__list_all_file(file_type="images")

    def __listfile(self):
        self.__list_all_file(file_type="attach")

    def __list_all_file(self, file_type):
        path = os.path.join(current_app.root_path, 'storage', self.__system['upload_path'], file_type)
        files = self.__get_list_file(path=path, temps=[])

        if not len(files):
            self.__result = {'state': '没有找到文件！'}
            return
        size = int(request.args.get("size", 20))
        start = int(request.args.get("start", 0))
        end = start + size
        lens = len(files)
        lists = []
        i = min(end, lens) - 1
        while i < lens and i >= 0 and i >= start:
            lists.append(files[i])
            i -= 1
        self.__result = {'state': 'SUCCESS',
                         "list": lists,
                         "start": start,
                         "total": len(files)}
        return

    def __get_list_file(self, path='', temps=[]):
        dir_list = os.listdir(path)
        for filename in dir_list:
            sub_path = os.path.join(path, filename)
            if os.path.isfile(sub_path):
                temp = sub_path.split('storage')[1]
                temp = temp.replace('\\', '/')
                mtime = str(os.path.getctime(sub_path)).split('.')[0]

                temps.append({'url': temp, 'mtime': mtime})
            else:
                self.__get_list_file(sub_path, temps)
        return temps

    def __catchimage(self):
        self.__result = {'state': '功能未开放！'}
