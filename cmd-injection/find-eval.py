#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/6 21:25
# @Author  : lockcy
# @File    : find-eval.py


# 寻找含有 eval 的内建模块
num = 0
for item in ''.__class__.__mro__[-1].__subclasses__():
    try:
        if 'eval' in item.__init__.__globals__['__builtins__']:
            print(num, item)
            print(item.__init__.__globals__['__builtins__']['eval']("2+2"))
        num += 1
    except:
        num += 1