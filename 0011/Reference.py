#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/1 11:47
# @Author  : WIX
# @File    : Reference.py

# 参考代码，使用cmd模块

import cmd

words_path = r'.\naive.txt'


class CLI(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Python敏感词检测:'
        with open(words_path, encoding='utf-8') as f:
            self.words = list(map(lambda i: i.strip('\n'), f.readlines()))
            self.prompt = ">>>"

    def default(self, line):
        if any([i in line for i in self.words]):
            print(line)
            print([i in line for i in self.words])
            print('Freedom')
        else:
            print(line)
            print([i in line for i in self.words])
            print('Human Rights')

    def do_quit(self, arg):
        exit()
        return True


if __name__ == '__main__':
    cli = CLI()
    cli.cmdloop()
