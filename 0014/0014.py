#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 23:37
# @Author  : WIX
# @File    : 0014.py

# 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

import os
import json
import xlwt
from collections import OrderedDict

# 存放文件的目录
filepath = r'f:\work2\leetcode\show me code\0014'


def run():
    os.chdir(filepath)
    # 读取文件内容
    with open('student.txt', encoding='utf-8') as f:
        content = f.read()
    # 转为json, 注意转化后的dict的元素位置和转化前可能会不一致，因此要使用OrderedDict
    d = json.loads(content, object_pairs_hook=OrderedDict)
    # print(d)
    file = xlwt.Workbook()
    # 添加sheet
    table = file.add_sheet('test')
    for row, i in enumerate(list(d)):
        table.write(row, 0, i)
        for col, j in enumerate(d[i]):
            table.write(row, col + 1, j)
    file.save('student.xls')


if __name__ == "__main__":
    run()
