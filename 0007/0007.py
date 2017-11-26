#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/26 14:40
# @Author  : WIX
# @File    : 0007.py
# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
# 用到面向对象编程，并学习使用了一下装饰器

import os

PATH = r'F:\work2\leetcode'


class Statistics(object):
    def __init__(self):
        self.comment_count = 0
        self.blank_count = 0
        self.code_count = 0
        self.path = PATH

    # 返回py文件列表
    @property
    def file_list(self):
        py_file = []
        all_file = os.listdir(self.path)
        for i in all_file:
            if os.path.splitext(i)[1] == '.py':
                py_file.append(i)
        return py_file

    # 处理每一个文件
    def handle_each_file(self, file):
        each_result = {'file_code': 0, 'file_comment': 0, 'file_blank': 0}
        with open(os.path.join(self.path, file), encoding="utf8") as f:
            all_line = f.readlines()
            each_result['file_code'] = len(all_line)
            comment_index = 0
            is_block_comment = False
            for index, line in enumerate(all_line):
                line = line.strip()
                # 判断是否为注释块
                if not is_block_comment:
                    if line.startswith("'''") or line.startswith('"""'):
                        is_block_comment = True
                        comment_index = index
                    elif line.startswith('#'):
                        each_result['file_comment'] += 1
                    elif line == '':
                        each_result['file_blank'] += 1
                # 若为注释块，则找到注释块的结尾，并计算注释块的行数
                else:
                    if line.endswith("'''") or line.endswith('"""'):
                        is_block_comment = False
                        each_result['file_comment'] += (index - comment_index + 1)
            print('----------\nfile: %s result:\nfile_code: %s\nfile_comment: %s\nfile_blank: %s' % (
                f.name, each_result['file_code'], each_result['file_comment'], each_result['file_blank']))

        return each_result

    def calc(self):
        # 　最终结果
        for each in self.file_list:
            each_result = self.handle_each_file(each)
            self.code_count += each_result['file_code']
            self.comment_count += each_result['file_comment']
            self.blank_count += each_result['file_blank']
        print('\n**********\ntotal result:\ntotal line: %s, total comment: %s, total blank: %s\n**********' % (
            self.code_count, self.comment_count, self.blank_count))


if __name__ == '__main__':
    calc = Statistics()
    calc.calc()
