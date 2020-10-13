#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_08_set.py
# @Author: xiaohanzhang
# @Data: 2020/8/14

# 集合中数据会自动去重
# 创建集合
set1 = {1, 3, 5, 3}
print(set1)     # {1, 3, 5}
set2 = set('abc')
print(set2)     # {'a', 'c', 'b'}
# 创建空集合
set3 = set()

# 添加数据
set3.add('aaa')
set3.add('bbb')
print(set3)

# 追加数据序列
set4 = {1, 2}
set4.update([10, 20])
print(set4)     # {1, 2, 10, 20}

# 删除集合中指定数据，不存在报错
set5 = {'a', 'b', 'c'}
set5.remove('b')
print(set5)

# 删除集合中指定数据，不存在不会报错
set5.discard('dd')

# 随机删除集合中的某个数据，并返回这个数据
t = set5.pop()
print(t)
print(set5)

# 判断数据是否在集合中
set6 = {3, 5, 7, 9}
if 5 in set6:
    print('5在集合中')

if 1 not in set6:
    print('1不在集合中')


