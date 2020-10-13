#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo1
# @File: py_21_test_module.py
# @Author: xiaohanzhang
# @Data: 2020/9/26

def say_hello():
    print("hello!!!")


def say_hi():
    print("hi???")


# 被其它文件导入时，不会被执行
if __name__ == "__main__":
    print("小米开发的模块")
