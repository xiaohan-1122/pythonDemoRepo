# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: py01_数据类型.py
# @Author: xiaohanzhang
# @Date: 2021/7/23

"""
python数据类型分为：
数值型：
    int(整型)
    float(浮点型)
布尔型(bool)：
    True
    False
字符串(str)
列表(list)
元组(tuple)
集合(set)
字典(dict)
"""
num1 = 2
num2 = 2.1
num3 = 2.229
print(type(num1))   # <class 'int'>
print(type(num2))   # <class 'float'>
print(type(num3))   # <class 'float'>

bool1 = True
print(type(bool1))  # <class 'bool'>

str = "hello world"
print(type(str))    # <class 'str'>

list1 = [1, 'a', '3']
print(type(list1))  # <class 'list'>

tuple1 = (1, 2, 'a')
print(type(tuple1)) # <class 'tuple'>

set1 = {1, 2, 'a'}
print(type(set1))   # <class 'set'>

dict1 = {'key1': 'value1', 'key2': 2}
print(type(dict1))  # <class 'dict'>

disct = {'bb', 'fansile', 0, 'exit', 'exit()'}