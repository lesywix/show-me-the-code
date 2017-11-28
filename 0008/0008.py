#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 15:04
# @Author  : WIX
# @File    : 0008.py

# 一个HTML文件，找出里面的正文
# only working with github page(html file which has <articles> element)

import requests
from bs4 import BeautifulSoup as bs


def scrap(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'DNT': '1',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    print('strating to parse url: %s...' % url)
    r = requests.get(url, headers=headers)
    if r.status_code == '200':
        print('getting html successful!')
    html = r.text
    return html


def handle_html(html):
    print('staring to handle html...')
    soup = bs(html, 'html.parser')
    # print(soup.article.string)
    content = soup.article.get_text('\n', strip=True).strip()
    with open('%s-content.txt' % my_url.replace('/', '-').replace(':', ''), 'w', encoding='utf-8') as f:
        f.write(content)
        print('html content has save in %s-content.txt' % my_url.replace('/', '-').replace(':', ''))


if __name__ == '__main__':
    my_url = input("please input a url you want to get content: ")  # 'https://github.com/Yixiaohan/show-me-the-code'
    my_html = scrap(my_url)
    handle_html(my_html)
    # handle_html('Yixiaohan_show-me-the-code.html')
