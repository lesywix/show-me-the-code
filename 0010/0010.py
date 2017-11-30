#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 20:10
# @Author  : WIX
# @File    : 0010.py

# 使用 Python 生成类似于下图中的字母验证码图片
# 感想：我是在做色盲识别图？？？

import string, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

IMG_SIZE = (240, 60)  # 图片大小
IMG_TYPE = 'GIF'  # 验证码格式
LETTER_NUM = 4  # 验证码字符个数
LETTER_FONT = 'C:/windows/fonts/Arial.ttf'  # 字体
IF_LINE = True  # 是否有干扰线
LN_NUM = (1, 4)  # 干扰线条数
LN_COLOR = (255, 0, 0)  # 干扰线颜色（红）
BG_COLOR = (255, 255, 255)  # 背景色（白）


class VerifyCode(object):
    def __init__(self):
        self.img_size = IMG_SIZE
        self.img_type = IMG_TYPE
        self.letter_num = LETTER_NUM
        self.letter_font = LETTER_FONT
        self.if_line = IF_LINE
        self.ln_num = LN_NUM
        self.ln_color = LN_COLOR
        self.bg_color = BG_COLOR
        self.img = Image.new('RGB', self.img_size, self.bg_color)
        self.draw = ImageDraw.Draw(self.img)

    # 随机字体颜色
    @staticmethod
    def ran_color():
        return (random.randint(50, 150), random.randint(50, 150), random.randint(50, 150))

    # 获取字符
    def __get_letter(self):
        source = string.ascii_letters + '3456789'
        letters = random.sample(source, self.letter_num)
        return letters

    # 创建干扰线
    def create_line(self):
        line_num = random.randint(*self.ln_num)
        for i in range(line_num):
            begin = (random.randint(0, self.img_size[0] - 5), random.randint(0, self.img_size[1] - 5))
            end = (random.randint(0 + 5, self.img_size[0]), random.randint(0 + 5, self.img_size[1]))
            self.draw.line([begin, end], fill=self.ln_color)

    def create_verify(self):
        # 填充背景色
        for x in range(self.img_size[0]):
            for y in range(self.img_size[1]):
                self.draw.point((x, y),
                                fill=(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
        font = ImageFont.truetype(self.letter_font, 40)

        # 每个字符都有随机颜色
        for i, t in enumerate(self.__get_letter()):
            self.draw.text((60 * i + 10, 10), t, font=font, fill=self.ran_color())
        # text = '  '.join(self.__get_letter())
        # font_width, font_height = font.getsize(text)
        # self.draw.text(
        #     ((self.img_size[0] - font_width) / self.letter_num, (self.img_size[1] - font_height) / self.letter_num),
        #     text, font=font, fill=self.ft_color)  # 填充字符串

        if self.if_line:
            self.create_line()
        params = [1 - float(random.randint(1, 2)) / 100,
                  0,
                  0,
                  0,
                  1 - float(random.randint(1, 10)) / 100,
                  float(random.randint(1, 2)) / 500,
                  0,
                  float(random.randint(1, 2)) / 1000
                  ]
        # 图像扭曲(未完成...)
        self.img = self.img.transform(self.img_size, Image.PERSPECTIVE, params)
        # self.img = self.img.transform((self.img_size[0] + 10, self.img_size[1] + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)
        self.img = self.img.filter(ImageFilter.SMOOTH)
        self.img.save('test.gif', self.img_type)


if __name__ == '__main__':
    verify = VerifyCode()
    verify.create_verify()
