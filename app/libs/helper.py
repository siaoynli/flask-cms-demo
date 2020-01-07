#!/usr/bin/env python
# _*_coding:utf-8_*_
# __author__ = 'Administrator'
import datetime, os, time, string, hashlib, random
from flask import request
from configobj import ConfigObj


def write_ini_file(field, data, path=None):
    if not path:
        path = os.path.dirname(os.path.dirname(__file__))
    config = ConfigObj(os.path.join(path, 'config/' + field + '.ini'), encoding='UTF8')
    for item, value in config[field].items():
        config[field][item] = data[item]
    config.write()


def read_ini_file(field, path=None):
    if not path:
        path = os.path.dirname(os.path.dirname(__file__))
    config = ConfigObj(os.path.join(path, 'config/' + field + '.ini'), encoding='UTF8')
    return config[field]


def random_filename(rawfilename):
    letters = string.ascii_letters
    random_filename = str(time.time()) + "".join(random.sample(letters, 5))
    filename = hashlib.md5(random_filename.encode('utf-8')).hexdigest()
    # 分离扩展名
    subffix = os.path.splitext(rawfilename)[-1]
    return filename + subffix


def get_date_dir(file_type='images'):
    _date = datetime.datetime.now().strftime("%Y-%m-%d")
    return os.path.join(file_type, _date)


def get_upload_path(upload_dir, file_type="images"):
    return os.path.join(upload_dir, get_date_dir(file_type))


def get_upload_abspath(root_path, upload_dir, file_type="images"):
    return os.path.join(root_path, 'storage', upload_dir, get_date_dir(file_type))


def time_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_client_ip():
    return request.remote_addr


def between(str, min, max):
    if len(str) > int(min) and len(str) < int(max):
        return True
    return False


def get_request_field():
    temp = list()
    for k, v in request.form.items():
        temp.append(k)
    return temp


def array_sort_by_pid(arrays, html='', pid=0, rank=0):
    temp = list()
    for item in arrays:
        if item.pid == pid:
            item.rank = rank + 1
            if rank > 0:
                html = '<div class="x-elbow-line"></div>' * (rank - 1)
                item.html = html + '<div class="x-elbow"></div>'
            else:
                item.html = html
            temp.append(item)
            temp.extend(array_sort_by_pid(arrays, html, item.id, rank + 1))
    return temp


def array_sort_to_tree(trees, pid=0, level=1):
    temp = list()
    for leaf in trees:
        if leaf.pid == pid:
            leaf.level = level
            for item in trees:
                if item.pid == leaf.id:
                    leaf.children = array_sort_to_tree(trees=trees, pid=leaf.id, level=level + 1)
                    break
                leaf.children = ""
            temp.append(leaf)
    return temp


def array_sort_by_pid_whitespace(arrays, html='', pid=0, rank=0):
    temp = list()
    for item in arrays:
        if item.pid == pid:
            item.rank = rank + 1
            if rank > 0:
                html = '|' * (rank - 1)
                item.html = html + '—'
            else:
                item.html = html
            temp.append(item)
            temp.extend(array_sort_by_pid_whitespace(arrays, html, item.id, rank + 1))
    return temp


def list_result_with_html(arrays):
    temp = list()
    for item in arrays:
        item.html = ""
        temp.append(item)
    return temp
