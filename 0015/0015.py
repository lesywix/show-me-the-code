#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 22:33
# @Author  : WIX
# @File    : 0015.py

# 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

import os
import json
import xlwt
from collections import OrderedDict

# 存放文件的目录
filepath = 'f:/work2/leetcode/show me code/0015'


def run():
    os.chdir(filepath)
    # 读取文件内容
    with open('city.txt', encoding='utf-8') as f:
        content = f.read()
    # 转为json, 注意转化后的dict的元素位置和转化前可能会不一致，因此要使用OrderedDict
    d = json.loads(content, object_pairs_hook=OrderedDict)
    file = xlwt.Workbook()
    # 添加sheet
    table = file.add_sheet('test')
    for row, i in enumerate(list(d)):
        table.write(row, 0, i)
        table.write(row, 1, d[i])
    file.save('city.xls')


if __name__ == "__main__":
    run()
