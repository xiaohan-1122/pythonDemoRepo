#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_11_lambda.py
# @Author: xiaohanzhang
# @Data: 2020/8/24

# 如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化。
"""
语法：lambda 参数列表: 表达式
"""
def fn1():
    return 100


print(fn1)  # <function fn1 at 0x1057fb268>
print(fn1())

fn2 = lambda: 100
print(fn2)  # <function <lambda> at 0x10589c0d0>
print(fn2())


# 两个数的和
add = lambda a, b: a + b
print(add(2, 5))

# ----------- 无参数 --------------
fn1 = lambda: 100

# ----------- 有参数 -------------
fn2 = lambda a, b: a + b

# ----------- 默认参数 -------------
fn3 = lambda a, b = 2: a * b
print(fn3(4))

# ----------- 可变参数*args -------------
fn4 = lambda *args: args
print(fn4('a', 'b'))

# ----------- 可变参数 *kwargs ----------
fn5 = lambda **kwargs: kwargs
print(fn5(name='Tom', age=12))


# lambda应用
# 1. 带判断的lambda
fn6 = lambda a, b: a if a > b else b
print(fn6(2, 9))

# 2. 列表数据按某个key的值排序
students = [{'name': 'Tom', 'age': 12}, {'name': 'Jack', 'age': 10}, {'name': 'Rose', 'age': 15}]
students.sort(key=lambda x: x['name'])
print(students)
students.sort(key=lambda x: x['name'], reverse=True)
print(students)
