#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/10 22:56
# @Author  : WIX
# @File    : 0021.py

# 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

import os
from hashlib import sha256
from hmac import HMAC


def encrypt_password(password, salt=None):
    if salt is None:
        # 64 bits
        salt = os.urandom(8)

    assert 8 == len(salt)
    # assert isinstance(salt, str)
    if isinstance(password, str):
        password = password.encode('utf-8')
    # assert isinstance(password, str)
    result = password
    for i in range(10):
        result = HMAC(result, salt, sha256).digest()
    return salt + result


def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])


my_pass = encrypt_password('my password')
try:
    assert validate_password(my_pass, 'my password')
    print('validate password')
except AssertionError as e:
    print('invalidate password')
