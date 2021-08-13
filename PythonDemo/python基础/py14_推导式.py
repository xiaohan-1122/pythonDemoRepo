#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py14_推导式.py
# @Author: xiaohanzhang
# @Data: 2020/8/15

"""
推导式格式
列表推导式格式: [xxx for xxx in range()]
字典推导式格式: {key: value for ... in ...}
集合推导式格式: {xxx for xxx in ...}
"""

"""
列表推导式：
用一个表达式，创建一个有规律的列表或控制一个有规律的列表。
格式: [xxx for xxx in range()]
"""
# 创建一个0-9的列表

# 方式一 while
list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)

# 方式二 for
list2 = []
for i in range(10):
    list2.append(i)
print(list2)

# 方式三 列表推导式
list3 = [i for i in range(10)]
print(list3)

""" 创建0-10的偶数列表"""
# 方式一
list4 = [i for i in range(0, 11, 2)]
print(list4)
# 方式二
list5 = [i for i in range(11) if i % 2 == 0]
print(list5)

""" 创建列表[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]"""
list6 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list6)


"""
字典推导式：
格式: {key: value for ... in ...}
"""
# 将两个list合并为一个字典
keys_list = ['name', 'age', 'gender']
values_list = ['Tom', 15, 'man']
dict1 = {keys_list[i]: values_list[i] for i in range(len(keys_list))}
print(dict1)

# 提取字典中目标数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# 提取电脑数量大于等于200的数据
count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1)


""" 
集合推导式
格式: {xxx for xxx in ...}
"""
# 创建一个集合，数据为下方列表的2次方
# list = [1, 1, 2]
list7 = [1, 1, 2]
set1 = {i ** 2 for i in list7}
print(set1)
# 注意集合有去重功能

