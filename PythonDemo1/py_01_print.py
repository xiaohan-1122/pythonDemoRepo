#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo1
# @File: py_01_print.py
# @Author: xiaohanzhang
# @Data: 2020/8/3

print('100 + 200 = ', 100 + 200)

name = 'Luffy'
age = 17
score = 98.64

print('My name is:', name)
print('My name is: ' + name)    # 参数需要是string
print('My name is: %s' % name)
print('My age is:', age)
print('My age is: %d' % age)
# %03d,表示输出的整数显示位数，不足以0补全超出当前位数则原样输出
print('My age is %03d' % age)   # My age is 017
print('My score is %f' % score)
print('My score is %.1f' % score)

print('My name is', name, ', My age is', age)
print('My name is ' + name, ', My age is ' + str(age))
print('My name is %s, My age is %d' % (name, age))
print('My name is %s, My age is %s' % (name, age))

# f'{表达式}'比%s更高效，Python3.6之后增加的方法
print(f'My name is {name}, my age is {age}')
print(f'My name is {name}, my age is {age + 1}')

print('Hello, {0}, 你的成绩提升了 {1:.1f}%'.format(name, 15.21))

# 不换行输出
print(name, end=' ')
print(name)

# 转义
print("I'm \"OK\" !")
print('I\'m OK !')
print('hello\nhi')
print('hello\\hi')
print(r'hello\nhi')

num1 = input("Please enter one number:")
num2 = input("Please enter one number:")
print(num1, "+", num2, "=", int(num1) + int(num2))

# eval(str) 将字符串转换为字符串内容的真实类型
str1 = '12'
str2 = '10.1'
str3 = '("a", "b", "c")'
str4 = '[100, 200, 300]'
print(type(eval(str1)))     # <class 'int'>
print(type(eval(str2)))     # <class 'float'>
print(type(eval(str3)))     # <class 'tuple'>
print(type(eval(str4)))     # <class 'tuple'>

"""
数字之间的逻辑
and: 只要有一个值为0，则结果0，否则结果为最后一个非0数字
or: 只有所有值都为0，结果才为0，否则结果为第一个非0数字
"""