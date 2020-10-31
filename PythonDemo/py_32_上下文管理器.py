#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_32_上下文管理器.py
# @Author: xiaohanzhang
# @Data: 2020/10/29
"""
上下文管理器：
一个类只要实现了__enter__()和__exit__()两个方法，通过该类创建的对象，我们就称为上下文管理器。
"""

# -------------------- 上下文管理器----类方式实现
class File(object):
    def __init__(self, file_name, file_model):
        self.file_name = file_name
        self.file_model = file_model

    def __enter__(self):
        # 上文方法，负责返回操作对象资源，比如：文件对象，数据库连接对象
        self.file = open(self.file_name, self.file_model)
        return self.file

    # with语句执行完成以后自动执行__exit__()方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 下文方法，负责释放对象资源，如：关闭文件，关闭数据库连接
        self.file.close()
        print('over')


with File("log.txt", "r") as f:
    file_data = f.read()

# -------------------- 上下文管理器----装饰器方式实现
# 通过yield将函数分割成两部分，yield上面的语句在__enter__*(方法中执行，yield下面的语句在__exit__()方法中执行，紧跟在yield后面的参数是函数的返回值
from contextlib import contextmanager

@contextmanager
def my_open(file_name, file_model):
    try:
        file = open(file_name, file_model)
        # yield之前的代码可以认为是上文方法，负责返回操作对象的资源
        yield file
    except Exception as e:
        print(e)
    finally:
        # yield之后的代码可以认为是下文方法，负责释放操作对象的资源
        file.close()


with my_open("log.txt", "r") as f:
    file_data = f.read()






