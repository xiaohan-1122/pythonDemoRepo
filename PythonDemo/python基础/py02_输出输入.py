#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py02_输出输入.py
# @Author: xiaohanzhang
# @Data: 2020/8/3

print('100 + 200 = ', 100 + 200)

name = 'Luffy'
age = 17
score = 98.64


"""
格式化输出:
%s  字符串
%d  有符号十进制整数
%f  浮点数
%u  无符号十进制整数
"""
# f'{表达式}'比%s更高效，Python3.6之后增加的方法
print(f'My name is: {name}')
print('My name is:', name)
print('My age is:', age)
print('My name is:' + name)     # 参数需要是string
print('My name is:%s' % name)
print('My age is: %d' % age)
print('My age is: %03d' % age)  # %03d表示输出的整数显示位数，不足以0补全，超出则按原样输出
print('My score is %f' % score)
print('My score is %.1f' % score)   # 保留1位小数

print(f'My name is {name}, my age is {age}')
print(f'My name is {name}, my age is {age + 1}')
print('My name is', name, ', My age is', age)
print('My name is ' + name, ', My age is ' + str(age))
print('My name is %s, My age is %d' % (name, age))
print('My name is %s, 明年%d岁' % (name, age + 1))

print('Hello, {0}, 你的成绩提升了 {1:.1f}%'.format(name, 15.21))

# 转义
print("I'm \"OK\" !")
print('I\'m OK !')
print('hello\nhi')
print('hello\\hi')
print(r'hello\nhi') # r表示不转义

# 不换行输出
print(name, end=' ')
print(name)

# 输入
num1 = input("Please enter one number:")
num2 = input("Please enter one number:")
print(num1, "+", num2, "=", int(num1) + int(num2))
