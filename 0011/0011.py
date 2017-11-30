#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/30 22:45
# @Author  : WIX
# @File    : 0011.py

# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。


def do_loop(file):
    with open(file, encoding='utf-8') as f:
        # 读取文件，去除‘\n’，返回列表
        word_list = list(map(lambda i: i.strip(), f.readlines()))
        while 1:
            in_word = input('>>>')
            if in_word in word_list:
                print('Freedom')
            else:
                print('Human Right')


if __name__ == '__main__':
    file = 'naive.txt'
    do_loop(file)
