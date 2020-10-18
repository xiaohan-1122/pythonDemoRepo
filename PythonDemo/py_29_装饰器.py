#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_29_装饰器.py
# @Author: xiaohanzhang
# @Data: 2020/10/17
import time
"""
- 装饰器
给已有函数增加额外功能的函数，本质就是一个闭包函数。
- 装饰器(decorator)功能
1. 不修改已有函数的源代码
2. 不修改已有函数的调用方式
3. 给已有函数增加额外功能
- 装饰器执行时机
当前模块加载完成时，装饰器会立即执行，对已有函数进行装饰

- 装饰器的语法
def decorator(func):    # func被装饰的目标函数
    def inner():
        '''执行函数之前'''
        func()      # 执行被装饰的目标函数
        '''执行函数之后'''
    return inner
# 装饰器语法糖用法：
@装饰器名称 修饰被装饰函数
"""
# 如果闭包函数有且只有一个参数，并且是函数类型，那么这个闭包函数称为装饰器
def outter(func):
    def inner():
        print("登录验证")
        func()
    return inner

# 装饰器语法糖写法 等价于comment = outter(comment)
@outter
def comment():
    print("发表评论")


comment()
# 调用装饰器对已有函数进行装饰
# comment = outter(comment)
# comment()


# ------------- 利用装饰器统计函数执行时间 无参数装饰器-------------------
def work_time(func):

    def inner():
        begin_time = time.time()
        func()
        end_time = time.time()
        print(end_time - begin_time)
    return inner

@work_time
def work():
    for i in range(1000):
        print(i)


work()

# ------------- 带参数装饰器 ------------------
def decorator_add(func):
    def inner(num1, num2):
        print('正在努力执行加法运算....')
        func(num1, num2)
    return inner


@decorator_add
def add_num(num1, num2):
    result = num1 + num2
    print(f'结果为：{result}')


add_num(1, 4)
"""
正在努力执行加法运算....
结果为：5
"""
# ------------- 有返回值装饰器 ------------------
def decorator_add2(func):
    def inner(num1, num2):
        print('2正在努力执行加法运算....')
        return func(num1, num2)
    return inner

@decorator_add2
def add_num2(num1, num2):
    return num1 + num2


result = add_num2(1, 2)
print(f'有返回值函数：result = {result}')
'''
正在努力执行加法运算....
有返回值函数：result = 3
'''
# ------------- 不定长参数装饰器 ------------------
def decorator_add3(func):
    def inner(*args, **kwargs):
        print('3正在努力执行加法运算....')
        return func(*args, **kwargs)    # 拆包
    return inner

@decorator_add3
def add_num3(*args, **kwargs):
    print("-----call_func:args =", args, ",kwargs =", kwargs)
    result = 0
    for value in args:
        result += value
    for value in kwargs.values():
        result += value
    return result


result = add_num3(1, 3)
print(f'不定长参数函数：result = {result}')
result = add_num3(1, 3, num=4)
print(f'不定长参数函数：result = {result}')
'''
3正在努力执行加法运算....
-----call_func:args = (1, 3) ,kwargs = {}
不定长参数函数：result = 4
3正在努力执行加法运算....
-----call_func:args = (1, 3) ,kwargs = {'num': 4}
不定长参数函数：result = 8
'''

# ------------- 通用装饰器 ------------------
def decorator(func):
    def inner(*arg, **kwargs):
        print('通用装饰器')
        res = func(*arg, **kwargs)
        return res
    return inner


@decorator
def show():
    print('哈哈哈哈哈哈')


show()