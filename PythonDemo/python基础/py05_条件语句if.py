#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py05_条件语句if.py
# @Author: xiaohanzhang
# @Data: 2020/8/5
import random

age = int(input('Please enter your age:'))
if age >= 18:
    print('OK')
else:
    print('NO')

print('*' * 50)

if age > 60:
    print('退休')
elif age >= 18:
    print('打工')
elif age >= 6:
    print('上学')
else:
    print('玩儿')

print('*' * 50)

if 0 < age <= 120:
    if age >= 18:
        print('成年')
    else:
        print('未成年')
else:
    print('输入年龄不合法')

print('*' * 50)

# 随机数
a = random.randint(0, 100)
b = random.randint(0, 100)
if a > b:
    print(f'a={a} > b={b}')
elif a == b:
    print('a = b')
else:
    print(f'a={a} < b={b}')

print('*' * 50)

""" 三目运算符 """
# 条件成立的表达式 if 条件 else 条件不成立执行的表达式
str1 = '成年人' if age >= 18 else '未成年人'
print(str1)
a = 1
b = 2
c = a if a > b else b

# is 判断两个标识符是否引用同一个对象，x is y 类似 id(x)==id(y)
# is not 判断两个标识符是否引用不同对象，x is not y 类似 id(x)!=id(y)
'''
is 和 == 区别：
is 判断两个标识符是否引用同一个对象
== 判断引用变量的值是否相等
针对None进行比较时，建议使用is
'''

