#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 10:59
# @Author  : WIX
# @File    : 0000.py
# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
from PIL import Image, ImageDraw, ImageFont


def add_num(img):
    draw = ImageDraw.Draw(img)

    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=66)
    filecolor = "#ff0000"
    width, height = img.size
    draw.text((width * 0.75, height * 0.075), '99', font=myfont, fill=filecolor)
    img.save("result.jpg", 'jpeg')
    return 0


if __name__ == '__main__':
    image = Image.open('image.jpeg')
    add_num(image)
