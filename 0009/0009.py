#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/28 19:09
# @Author  : WIX
# @File    : 0009.py

#  一个HTML文件，找出里面的链接。

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
    proto = r.url.split('/')[0]
    domain = r.url.split('/')[2]
    print(proto)
    print(domain)
    if r.status_code == 200:
        print('getting html successful!')
    html = r.text

    print('staring to handle html...')
    # soup = bs(open(html, encoding='utf-8'), 'html.parser')
    soup = bs(html, 'html.parser')
    # print(soup.article.string)
    # content = soup.article.get_text('\n', strip=True).strip()
    a = soup.findAll('a')
    # print(href)
    # for i in href:
        # print(i.get('href'))
    href = [i.get('href') for i in a if i.get('href') != '']
    # href = [a.pop() for i in a if i == '']
    print(href)
    href = map(lambda i: proto + '//' + domain + i if i[0] == '/' else url + i if i[0] == '#' else i, href)
    print([i for i in href])
    # with open('%s-content.txt' % my_url.replace('/', '-').replace(':', ''), 'w', encoding='utf-8') as f:
        # f.write(content)
        # print('html content has save in %s-content.txt' % my_url.replace('/', '-').replace(':', ''))


if __name__ == '__main__':
    my_url = 'https://github.com/Yixiaohan/show-me-the-code' # input("please input a url you want to get content: ")
    scrap(my_url)
