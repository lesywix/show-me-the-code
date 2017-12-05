#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 22:43
# @Author  : WIX
# @File    : 0016.py

# 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

import os
import json
import xlwt
from collections import OrderedDict

# 存放文件的目录
filepath = 'f:/work2/leetcode/show me code/0016'


def run():
    os.chdir(filepath)
    # 读取文件内容
    with open('numbers.txt', encoding='utf-8') as f:
        content = f.read()
    # 转为json, 注意转化后的dict的元素位置和转化前可能会不一致，因此要使用OrderedDict
    d = json.loads(content, object_pairs_hook=OrderedDict)
    file = xlwt.Workbook()
    # 添加sheet
    table = file.add_sheet('test')
    for row, i in enumerate(d):
        for col, j in enumerate(i):
            table.write(row, col, j)
    file.save('numbers.xls')


if __name__ == "__main__":
    run()
