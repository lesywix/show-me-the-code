#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 14:54
# @Author  : WIX
# @File    : 0005.py

# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

import os, sys
from PIL import Image, ImageOps


# 遍历文件夹，返回图片名列表
def read_all_img(path):
    img_list = []
    path_list = os.listdir(path)
    for i in path_list:
        if not os.path.isdir(i):
            if os.path.splitext(i)[1] in ['.jpg']:
                img_list.append(i)
        else:
            sub_path = os.path.join(path, i)
            img_list += read_all_img(sub_path)

    return img_list


# 重置图片分辨率
def resize_img(img_list):
    # iphone分辨率
    width = 640
    height = 1136
    for i in img_list:
        with Image.open(i) as img:
            x, y = img.size
            if x > width:
                y = width * y // x
                x = width
            if y > height:
                x = height * x // y
                y = height

            img = ImageOps.fit(img, (x, y))
            img.save("out" + i, 'JPEG')


if __name__ == '__main__':
    all_img = read_all_img(r'F:\work2\leetcode\show me code\0005')
    resize_img(all_img)
