#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py05_条件语句if.py
# @Author: xiaohanzhang
# @Data: 2020/8/5

age = int(input('Please enter your age:'))
# if age >= 18:
#     print('ok')
# else:
#     print('no')

if 0 < age <= 120:
    if age >= 18:
        print('成年')
    else:
        print('未成年')
else:
    print('输入年龄不合法')

print('*' * 50)

a = int(input('Please enter first number:'))
b = int(input('Please enter second number:'))
if a > b:
    print('>>>>>>>>>')
elif a == b:
    print('=========')
else:
    print('<<<<<<<<<')

print('*' * 50)

python_score = float(input("请输入Python成绩："))
c_score = float(input("请输入c语言成绩："))
if python_score >= 60 or c_score >= 60:
    print("合格")
else:
    print("不合格")

print('*' * 50)

# is 判断两个标识符是否引用同一个对象，x is y 类似 id(x)==id(y)
# is not 判断两个标识符是否引用不同对象，x is not y 类似 id(x)!=id(y)
'''
is 和 == 区别：
is 判断两个标识符是否引用同一个对象
== 判断引用变量的值是否相等
针对None进行比较时，建议使用is
'''
# 三目运算符
# 条件成立表达式 if 条件 else 条件不成立执行表达式
a = 1
b = 2
c = a if a > b else b