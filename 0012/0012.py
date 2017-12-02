#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/1 17:33
# @Author  : WIX
# @File    : 0012.py

#  敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

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
        a = [i in line for i in self.words]
        if any(a):
            for index, element in enumerate(a):
                if element:
                    line = line.replace(self.words[index], '*'*len(self.words[index]))
            print(line)
            # print('Freedom')
        else:
            print(line)

    def do_quit(self, arg):
        exit()
        return True


if __name__ == '__main__':
    cli = CLI()
    cli.cmdloop()
