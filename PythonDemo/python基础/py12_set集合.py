#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py12_set集合.py
# @Author: xiaohanzhang
# @Data: 2020/8/14

# 集合中数据会自动去重，集合中数据没有顺序
# 创建集合
set1 = {1, 3, 5, 3}
print(set1)     # {1, 3, 5}
set2 = set('abc')
print(set2)     # {'a', 'c', 'b'}
# 创建空集合
set3 = set()

""" 添加数据 """
# add() 添加单个数据
set3.add('aaa')
set3.add('bbb')
print(set3)     # {'aaa', 'bbb'}

# update() 增加一个数据序列到原集合
set3.update([10, 20])
print(set3)     # {'bbb', 10, 20, 'aaa'}

""" 删除数据 """
# remove() 删除集合中指定数据，不存在报错
set5 = {'a', 'b', 'c', 'd'}
set5.remove('b')
print(set5)     # {'a', 'c', 'd'}

# discard() 删除集合中指定数据，不存在不会报错
set5.discard('dd')

# 随机删除集合中的某个数据，并返回这个数据
t = set5.pop()
print(t)    # a
print(set5)     # {'c', 'd'}

""" 查找 """
# 判断数据是否在集合中
set6 = {3, 5, 7, 9}
if 5 in set6:
    print('5在集合中')

if 1 not in set6:
    print('1不在集合中')


