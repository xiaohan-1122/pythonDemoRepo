# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: py03_数据类型转换.py
# @Author: xiaohanzhang
# @Date: 2021/7/23

"""
数据类型转换:
int(x[,base])   将x转换为一个整数
float(x)        将x转换为一个浮点数
str(x)          将对象x转换为字符串
eval(str)       将对象x转换为表达式字符串(真实类型)
tuple(s)        将序列s转换为一个元组
list(s)         将序列s转换为一个列表
"""

str1 = '12'
str2 = '10.1'
str3 = '("a", "b", "c")'
str4 = '[100, 200, 300]'
num = 13
l = [1, 'a', 8]

num1 = int(str1)
print(type(num1))   # <class 'int'>

f1 = float(str1)
print(type(f1))     # <class 'float'>

s1 = str(num)
s2 = str(l)
print(s1, type(s1))     # 13 <class 'str'>
print(s2, type(s2))     # [1, 'a', 8] <class 'str'>

t1 = tuple(l)
t2 = tuple(str3)
print(type(t1))     # <class 'tuple'>
print(type(t2))

l1 = list(str4)
print(type(l1))     # <class 'list'>

# eval(str) 将字符串转换为字符串内容的真实类型
print(type(eval(str1)))     # <class 'int'>
print(type(eval(str2)))     # <class 'float'>
print(type(eval(str3)))     # <class 'tuple'>
print(type(eval(str4)))     # <class 'list'>

"""
数字之间的逻辑
and: 只要有一个值为0，则结果0，否则结果为最后一个非0数字
or: 只有所有值都为0，结果才为0，否则结果为第一个非0数字
"""
