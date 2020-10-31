#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_33_生成器.py
# @Author: xiaohanzhang
# @Data: 2020/10/29
"""
生成器：
    根据设定的规则循环生成数据，当条件不成立时，生成数据结束。
    数据不是一次性全部生成处理，而是使用一个再生成一个，可以节约大量的内存。
创建生成器方式：
    1.生成器推导式
    2.yield关键字
"""
# ------------- 生成器推导式------------
# 创建生成器
my_generator = (value * 2 for value in range(3))
# 生成器取值 通过next()方法
print(next(my_generator))

# for循环内部循环调用next函数获取生成器中的下一个值，当出现异常，for循环内部自动进行了异常捕获
for value in my_generator:
    print(value)

# ------------- yield关键字------------
# 这个函数就是一个生成器 当程序执行到yield关键字时，代码暂停并把结果返回，再次启动生成器时，会在暂停的位置继续往下执行
def my_generator():
    for i in range(3):
        print('开始生成数据...')
        yield i
        print('上一个数据生成完了...')


for value in my_generator():
    print(value)


# 生成器的使用 生成斐波拉契数列
def fibonacci(num):
    # 初始化前两个数
    a = 0
    b = 1
    # 记录每次生成数列个数的索引
    current_index = 0

    while current_index < num:
        result = a
        # 条件成立交换两个变量的值
        a, b = b, a + b
        current_index += 1
        yield result


for value in fibonacci(10):
    print(value)