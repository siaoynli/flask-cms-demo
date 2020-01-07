"""
created  by  hzwlxy  at 2018/7/18 17:04
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
import os, shutil, datetime, hashlib, tempfile
from flask import request, current_app
from PIL import Image
from uuid import uuid4

__author__ = '西瓜哥'
from app.libs.helper import read_ini_file, get_upload_abspath, get_upload_path, random_filename


class Upload:
    _file = None
    _type = "images"
    _ext = ""
    _water = False
    _info = {}
    _origin_file_name = ""
    _thumb = ""
    _temp_file = ''
    _size = 0
    _uuid = ''
    _file_field = "file"
    _allow_images_ext = ('jpg', 'png', 'jpeg', 'gif')
    _allow_media_ext = ('mov', 'avi', 'mp4', 'mkv')
    _allow_attach_ext = ('pdf', 'doc', 'zip', 'rar', 'docx')

    def __init__(self, upload_type="images", water=False, file_field="file"):
        self._type = upload_type
        self._water = water
        self._system = read_ini_file('system')
        self._uuid = str(uuid4())
        self._file_field = file_field

    def info(self):
        return self._info

    def _is_valid(self, file):
        if self._file_field not in file:
            return False
        if file[self._file_field].filename == '':
            return False
        if '.' not in file[self._file_field].filename:
            return False
        self._file = file[self._file_field]
        return True

    def _check_ext(self):
        if self._type == "images":
            return self._ext in self._allow_images_ext
        if self._type == "avatar":
            return self._ext in self._allow_images_ext
        elif self._type == "media":
            return self._ext in self._allow_media_ext
        elif self._type == "attach":
            return self._ext in self._allow_attach_ext
        return False

    def _check_size(self):
        if self._type == "images":
            return self._size < int(self._system['images_size']) * 1024
        if self._type == "avatar":
            return self._size < int(self._system['images_size']) * 1024
        elif self._type == "media":
            return self._size < int(self._system['media_size']) * 1024
        elif self._type == "attach":
            return self._size < int(self._system['attach_size']) * 1024
        return False

    def _split_filename(self):
        self._ext = self._file.filename.rsplit('.', 1)[1].lower()

    def _get_storage_dir(self):
        return os.path.join(current_app.root_path, 'storage')

    def upload(self, file=None):
        if file is None:
            file = request.files
        else:
            file = file
        if not self._is_valid(file):
            self._info = {'state': '上传文件失败'}
            return
        self._split_filename()
        if not self._check_ext():
            self._info = {'state': '不允许的上传类型'}
            return
        temp_dir = tempfile.mkdtemp()
        self._temp_file = os.path.join(temp_dir, self._uuid)
        try:
            self._file.save(self._temp_file)
        except Exception as e:
            self._info = {'state': '服务器临时文件夹不可写！'}
            return
        self._size = os.stat(self._temp_file).st_size
        if not self._check_size():
            self._info = {'state': '上传文件超过限制大小'}
            os.remove(self._temp_file)
            return

        # 设置上传目录
        upload_dir = get_upload_abspath(root_path=current_app.root_path, upload_dir=self._system['upload_path'],
                                        file_type=self._type)
        if not os.path.exists(upload_dir):
            try:
                os.makedirs(upload_dir)
            except Exception as e:
                self._info = {'state': '请确保上传目录可写'}
                return
        new_filename = random_filename(self._file.filename)
        file_path = os.path.join(upload_dir, new_filename)
        try:
            shutil.move(self._temp_file, file_path)
        except Exception as e:
            self._info = {'state': '上传失败！'}
            return
        if self._type == "images":
            try:
                Image.open(file_path)
            except Exception as e:
                os.remove(file_path)
                self._info = {'state': '不是标准图片，上传失败！'}
                return

        path = os.path.join(get_upload_path(upload_dir=self._system['upload_path'], file_type=self._type), new_filename)
        path = path.replace('\\', '/')
        self._info = {
            'state': 'SUCCESS',
            'original_name': self._file.filename,
            'title': self._file.filename,
            'ext': self._ext,
            "url": '/' + path,
            "filename": path,
        }
        return

    def chunk_upload(self, file=None):
        if file is None:
            file = request.files
        else:
            file = file
        if not self._is_valid(file):
            self._info = {'state': '上传文件失败'}
            return
        self._split_filename()
        if not self._check_ext():
            self._info = {'state': '不允许的上传类型'}
            return

        is_chunked = request.form.get('is_chunked', 'false')
        chunk = request.form.get('chunk', 0)
        chunks = request.form.get('chunks')
        size = request.form.get('size')
        unique_file_name = request.form.get('unique_file_name')

        dir_abspath = os.path.join(current_app.root_path, 'storage/chunk_temp_files', unique_file_name)

        if is_chunked == 'false':
            try:
                self._file.save(os.path.join(dir_abspath, 'temp.tmp'))
            except Exception as e:
                self._info = {'state': '上传失败！'}
                return
            self._info = {'state': 'success', 'status': 'success', 'chunked': True, 'ext': self._ext,
                          'original_name': self._file.filename}
            return
        if is_chunked == 'true':
            name = str(100000000 + int(chunk)) + '.tmp'
            try:
                self._file.save(os.path.join(dir_abspath, name))
            except Exception as e:
                self._info = {'state': '上传失败！'}
                return

            if int(chunks) == int(chunk) + 1:
                self._info = {'state': 'success', 'status': 'success', 'chunked': True, 'ext': self._ext,
                              'original_name': self._file.filename}
            else:
                self._info = {'state': 'success', 'status': 'chunked', 'chunked': True}
            return

        self._info = {'state': 'is_chunked值错误，上传失败！'}
        return

    def chunk(self):
        dir_name = request.form.get('unique_file_name', None)
        chunk_index = request.form.get('chunk_index', 0)
        size = request.form.get('size', 0)
        dir_abspath = os.path.join(current_app.root_path, 'storage/chunk_temp_files', dir_name)

        if not os.path.exists(dir_abspath):
            try:
                os.makedirs(dir_abspath)
            except Exception as e:
                self._info = {'state': '请确保上传目录可写'}
                return

        name = str(100000000 + int(chunk_index)) + '.tmp'
        chunk_file = os.path.join(dir_abspath, name)

        if os.path.exists(chunk_file):
            if os.path.getsize(chunk_file) == int(size):
                self._info = {'state': 'success', 'is_file_exist': 1}
                return
        self._info = {'state': 'success', 'is_file_exist': 0}
        return

    def merge(self):
        self._ext = request.form.get('ext', 'jpg').lower()
        dir_name = request.form.get('unique_file_name', None)
        chunks = request.form.get('chunks', 0)
        size = request.form.get('size', 0)
        original_name = request.form.get('original_name', None)
        if not self._check_ext():
            self._info = {'state': '不允许的上传类型'}
            return
        self._set_upload_dir()
        if not os.path.exists(self._get_upload_dir()):
            try:
                os.makedirs(self._get_upload_dir())
            except Exception as e:
                self._info = {'state': '请确保上传目录可写'}
                return
        new_filename = hashlib.md5(str(datetime.datetime.now()).encode('utf-8')).hexdigest() + '.' + self._ext

        new_file_abspath = os.path.join(self._get_upload_dir(), new_filename)

        dir_abspath = os.path.join(current_app.root_path, 'storage/chunk_temp_files',
                                   dir_name)

        if not os.path.exists(dir_abspath):
            self._info = {'state': '分片目录不存在'}
            return

        files = os.listdir(dir_abspath)
        file_size = 0
        if len(files) == int(chunks):
            with open(new_file_abspath, 'wb') as output:
                for eachfile in files:
                    filepath = os.path.join(dir_abspath, eachfile)
                    file_size = file_size + os.path.getsize(filepath)
                    with open(filepath, 'rb') as infile:
                        data = infile.read()
                        output.write(data)

            # 检测合并后的文件大小
            if os.path.getsize(new_file_abspath) == file_size and os.path.getsize(new_file_abspath) == int(size):
                for eachfile in files:
                    filepath = os.path.join(dir_abspath, eachfile)
                    if os.path.exists(filepath):
                        os.remove(filepath)
                #         删除空目录
                os.rmdir(dir_abspath)
                path = os.path.join(current_app.config['UPLOAD_FOLDER'], self._upload_dir, new_filename)
                path = path.replace('\\', '/')
                self._info = {
                    'state': 'success',
                    'original_name': original_name,
                    'ext': self._ext,
                    "url": '/' + path,
                    "filename": path,
                }
            else:
                self._info = {'state': '合并文件出错'}
                return
        else:
            self._info = {'state': '分片文件丢失'}
            return
