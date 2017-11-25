#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/25 11:21
# @Author  : WIX
# @File    : 0006.py
# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
# txt取自bbc，红黄蓝事件http://www.bbc.com/news/world-asia-china-42105443

import os,re
from collections import Counter

STOP_WORD = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 'this', 's', 'is', 'are', 'a', 'with', 'as', 'an', 'on',
             'was', 'were', 'have', 'also', 'for', 'the']
PATH = r'F:\work2\leetcode\show me code\0006'


def get_word(file):
    reg = re.compile('[A-Za-z0-9\']+')
    with open(file) as f:
        content = f.read()
        word = reg.findall(content)
        c = Counter(word)
        for i in STOP_WORD:
            c[i] = 0
        return c.most_common(3)


def run(path):
    txt_list = os.listdir(path)
    for each in txt_list:
        if os.path.splitext(each)[1] == ".txt":
            top3 = get_word(each)
            print('TOP 3 word and count in %s is %s' % (each, str(top3)))


if __name__ == '__main__':
    run(PATH)
