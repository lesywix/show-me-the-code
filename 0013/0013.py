#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/3 15:55
# @Author  : WIX
# @File    : 0013.py

# 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)

import requests
from bs4 import BeautifulSoup as bs


def get_link(url):
    print('staring to parser html...')
    page = requests.get(url)
    html = page.text
    soup = bs(html, 'html.parser')
    img_link = soup.findAll('img')
    img_src = [i.get('src') for i in img_link if
               i.get('src').endswith('jpg') and i.get('class') is not None and i.get('class')[0] == 'BDE_Image']
    return img_src


def save_img(link):
    print('staring to save image...')
    for i, j in enumerate(link):
        ir = requests.get(j)
        if ir.status_code == 200:
            with open('./img/%s.jpg' % i, 'wb') as f:
                f.write(ir.content)
    print('all done...')


if __name__ == '__main__':
    page_url = 'http://tieba.baidu.com/p/2166231880'
    all_link = get_link(page_url)
    save_img(all_link)
