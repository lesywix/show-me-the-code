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
    # 获取协议和主机域名
    proto = r.url.split('/')[0]
    domain = r.url.split('/')[2]
    if r.status_code == 200:
        print('getting html successful!')
    html = r.text

    print('staring to handle html...')
    soup = bs(html, 'html.parser')
    a = soup.findAll('a')
    # 获取所有href列表,并将空的值去除（若不去除，会影响影响到后面取索引）
    """
    这里遇到了一个坑：
    for i, j in enumerate(a):
        if not j:
            a.pop(i)
    print(a)
    运行如上代码去除空字符串，始终会有一个空字符串不能删除，这是因为随着删除元素，列表的长度也会随着改变，循环并不会完全遍历整个列表，不妨调试一下就能真相大白！
    """
    href = [i.get('href') for i in a if i.get('href') != '']
    # 若href以‘/’开头，则加上协议，域名，若以‘#’开头，则加上url，否则返回href
    href = map(lambda i: proto + '//' + domain + i if i[0] == '/' else url + i if i[0] == '#' else i, href)
    print([i for i in href])


if __name__ == '__main__':
    my_url = 'https://github.com/weixianglin' # input("please input a url you want to get content: ")
    scrap(my_url)
