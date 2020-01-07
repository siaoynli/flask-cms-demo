"""
created  by  hzwlxy  at 2018/7/19 15:15
__author__: 西瓜哥
__QQ__ : 120235331
__Note__： 
"""
import os, math
from flask import current_app
from PIL import Image, ImageDraw, ImageFont

__author__ = '西瓜哥'

from app.libs.layui_response import Fail
from app.libs.helper import read_ini_file


class Images:
    _thumb_width = 600
    _thumb_height = 600
    _img = None
    _ext = 'jpg'
    _old_file_name = ""
    _new_file_image = ""
    _storage_path = ""

    def __init__(self, old_file_name=None):
        if old_file_name:
            self._ext = old_file_name.rsplit('.', 1)[1].lower()
            self._old_file_name = old_file_name
            self._storage_path = os.path.join(current_app.root_path, 'storage')
            self._system = read_ini_file('system')
            try:
                self._img = Image.open(os.path.join(self._storage_path, old_file_name))
            except IOError:
                raise Fail(message="图片不能打开")

    @property
    def image(self):
        return self._img

    @image.setter
    def image(self, raw):
        self._img = raw

    def thumb(self, width=None, height=None):
        """
        保持图片的宽高比例缩略图片大小
        :param width:
        :param height:
        :return:
        """
        if width is None:
            width = int(self._system['images_max_width'])
        if height is None:
            height = int(self._system['images_max_height'])
        self._img.thumbnail((width, height))
        return self

    def clip(self, dst_w=2, dst_h=1):
        """
        按比例裁剪
        :param dst_w:
        :param dst_h:
        :return:
        """
        ori_w, ori_h = self._img.size

        dst_scale = float(dst_w) / dst_h
        ori_scale = float(ori_w) / ori_h
        if ori_scale <= dst_scale:
            width = ori_w
            height = int(width / dst_scale)
            x = 0
            y = (ori_h - height) / 2
        else:
            height = ori_h
            width = int(height * dst_scale)
            x = (ori_w - width) / 2
            y = 0
        box = (x, y, width + x, height + y)
        self._img = self._img.crop(box)

        ratio = float(dst_w) / width
        newWidth = int(width * ratio)
        newHeight = int(height * ratio)

        self._img.resize((newWidth, newHeight), Image.ANTIALIAS)
        return self

    def water(self, logo_path=None, local=5, offset_x=10, offset_y=10, water_font=None):
        """
        打水印
        :param logo_path: 图片水印地址
        :param local: 水印位置
        :param offset_x: x偏移
        :param offset_y: y偏移
        :param water_font: True 字体水印 ,值为文字，就是水印文字
        :return:
        """
        bw, bh = self._img.size
        if self._system['water_type'] == 'image':
            if logo_path is None:
                logo_path = os.path.join(current_app.root_path, 'static', self._system['images_water'])
            else:
                logo_path = os.path.join(current_app.root_path, logo_path)
            try:
                mark = Image.open(logo_path)
            except IOError as e:
                raise Fail(message="水印文件找不到")
            layer = Image.new('RGBA', self._img.size, (0, 0, 0, 0))
            lw, lh = mark.size
        else:
            water_txt = self._system['txt_water']
            font_file = os.path.join(current_app.root_path, 'static', self._system['txt_water_font'])
            if not os.path.exists(font_file):
                raise Fail(message="水印字体不存在")
            n_font = ImageFont.truetype(font_file, size=int(self._system['txt_water_size']))
            lw, lh = n_font.getsize(water_txt)

        x = bw - lw - offset_x
        y = bh - lh - offset_y

        if x and y:
            if local == 1:
                x = offset_x
                y = offset_y
            elif local == 2:
                x = math.ceil((bw - lw) / 2)
                y = offset_y
            elif local == 3:
                x = bw - lw - offset_x
                y = offset_y
            elif local == 4:
                x = offset_x
                y = math.ceil((bh - lh) / 2)
            elif local == 5:
                x = math.ceil((bw - lw) / 2)
                y = math.ceil((bh - lh) / 2)
            elif local == 6:
                x = bw - lw - offset_x
                y = math.ceil((bh - lh) / 2)
            elif local == 7:
                x = offset_x
                y = bh - lh - offset_y
            elif local == 8:
                x = math.ceil((bw - lw) / 2)
                y = bh - lh - offset_y

            if self._system['water_type'] == 'image':
                layer.paste(mark, (x, y))
                self._img = Image.composite(layer, self._img, layer)
            else:
                draw = ImageDraw.Draw(self._img)
                draw.text((x, y), water_txt, font=n_font, fill=self._system['txt_water_color'])
        return self

    def save(self, new_filename=None, quality=95):
        """
        保存
        :param new_filename: 新文件地址
        :param quality: 图片质量
        :return:
        """
        self._new_file_image = self._old_file_name
        if new_filename:
            self._new_file_image = new_filename
        if self._img.mode == 'RGBA':
            self._ext = 'png'
        elif self._img.mode == 'RGB':
            self._ext = 'jpeg'
        elif self._img.mode == 'CMYK':
            self._ext = 'jpeg'
        else:
            self._ext = 'png'
        try:
            self._img.save(os.path.join(self._storage_path, self._new_file_image), self._ext, quality=quality)
        except Exception as e:
            os.remove(os.path.join(self._storage_path, self._new_file_image))
            raise Fail(message="图片处理失败")
        return self._new_file_image
