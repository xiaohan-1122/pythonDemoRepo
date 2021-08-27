#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py19_高阶函数.py
# @Author: xiaohanzhang
# @Data: 2020/8/25

# 绝对值函数
print(abs(-10))     # 10

# 四舍五入
print(round(1.2))   # 1
print(round(1.8))   # 2
print(round(-1.2))  # -1

""" 高阶函数：一个函数可以作为参数传给另外一个函数 """


def sum_num(a, b, f):
    """ a,b经过f处理后 相加 """
    return f(a) + f(b)


sum = sum_num(4, -3, abs)
print(sum)
print(sum_num(1.2, 1.8, round))


"""
函数：map(func, lst)
将传入的func函数作用到列表lst中的每一个元素，并将结果组成新的序列返回
"""


# 计算list中没个元素的2次方
def f1(x):
    return x ** 2


list1 = [1, 2, 3]
result = map(f1, list1)
print(list(result))     # [1, 4, 9]


"""
函数：reduce(func, lst)
func必须有两个参数，每次func计算的结果必须和list的下一个元素做累积计算
"""

# 计算list中各个数字的累加和
import functools

list2 = [1, 2, 3, 4, 5]
def f2(a, b):
    return a + b


result = functools.reduce(f2, list2)
print(result)   # 15


"""
函数：filter(func, lst)
用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象。可以使用list()转换成列表
"""
# 筛选出list中的偶数
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def f3(x):
    return x % 2 == 0


result = filter(f3, list3)
print(list(result))     # [2, 4, 6, 8]

