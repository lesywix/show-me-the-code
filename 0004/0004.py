#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 16:04
# @Author  : WIX
# @File    : 0004.py

#  任一个英文的纯文本文件，统计其中的单词出现的个数。
# 看了一下大家的答案，大概是我误解题意了哈哈


def statistics(file):
    with open(file) as f:
        en_list = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]
        result = dict.fromkeys(en_list, 0)
        f = f.read()
        for i in f:
            if result.get(i) is not None:
                result[i] += 1
        print(result)


if __name__ == '__main__':
    file = './all_en.txt'
    statistics(file)
