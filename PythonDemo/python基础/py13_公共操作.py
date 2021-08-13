#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py13_公共操作.py
# @Author: xiaohanzhang
# @Date: 2021/8/11

""" 运算符 """
'''
运算符         描述          支持的容器类型
+             合并         字符串、列表、元组
*             复制         字符串、列表、元组
in         元素是否存在     字符串、列表、元组、字典
not in     元素是否不存在   字符串、列表、元组、字典
'''
str1 = 'aa'
str2 = 'bb'

list1 = [1, 2]
list2 = [8, 9]

tuple1 = (22, 33)
tuple2 = (88, 99)

# +
str3 = str1 + str2
print(str3)     # aabb
list3 = list1 + list2
print(list3)    # [1, 2, 8, 9]
tuple3 = tuple1 + tuple2
print(tuple3)   # (22, 33, 88, 99)

# *
str4 = 'a'
str5 = str4 * 2
print(str5)     # aa

list4 = [1, 2]
list5 = list4 * 3
print(list5)    # [1, 2, 1, 2, 1, 2]

tuple4 = ('a', 'b')
tuple5 = tuple4 * 2
print(tuple5)   # ('a', 'b', 'a', 'b')

# in 和 not in
str6 = 'abcd'
print('a' in str6)
print('a' not in str6)


list6 = [1, 2, 3]
print(3 in list6)
print(3 not in list6)

tuple6 = (11, 22, 33)
print(22 in tuple6)
print(22 not in tuple6)

dict1 = {'name': 'xiaobai'}
print('name' in dict1)  # True
print('name' in dict1.keys())   # True
print('name' not in dict1.values()) # True


""" 公共方法 """
'''
函数                          描述
len()                   计算容器中元素个数
del                     删除
max()                   返回容器中元素最大值
min()                   返回容器中元素最小值
range(start, end, step) 生成从start到end的数字，步长是step，供for循环使用
enumerate()             用于将一个可遍历的数据对象（如列表、字符串）组合为一个索引序列，同时列出数字和下标，一般用在for循环中
'''
# len()
str6 = 'abcd'
print(len(str6))     # 4
list6 = [1, 2, 3]
print(len(list6))   # 3
dict2 = {'name': 'xiaolan', 'age': 10}
print(len(dict2))   # 2
set1 = {10, 20, 30, 40}
print(len(set1))    # 4

# del
del str1
# print(str1)     # NameError: name 'str1' is not defined
del list6[0]
print(list6)    # [2, 3]
del list6
# print(list6)    # NameError: name 'list6' is not defined

# max()和 min()
list6 = [3, 8, 2, 9]
print(max(list6))   # 9
print(min(list6))   # 2

str7 = 'rygska'
print(max(str7))    # y
print(min(str7))    # a

# range() 左闭右开 默认步长为1，不写start默认从0开始
for i in range(1, 5):
    print(i)    # 1, 2, 3, 4

for i in range(1, 5, 2):
    print(i)    # 1, 3

for i in range(5):
    print(i)    # 0, 1, 2, 3, 4


# enumerate(可遍历对象, start=0)，start参数用来设置遍历数据的下标的起始值，默认为0
list7 = ['a', 'b', 'c']
for index, value in enumerate(list7):
    print(f'index = {index}, value = {value}')
'''
index = 0, value = a
index = 1, value = b
index = 2, value = c
'''
for index, value in enumerate(list7, start=2):
    print(f'index = {index}, value = {value}')
'''
index = 2, value = a
index = 3, value = b
index = 4, value = c
'''


""" 容器类型转换 """
list8 = [1, 2, 3]
set2 = {'a', 'b', 'c'}
tuple7 = (11, 22, 33)

# 转为元组
tuple8 = tuple(list8)
print(tuple8)   # (1, 2, 3)
tuple9 = tuple(set2)
print(tuple9)   # ('c', 'b', 'a')

# 转为列表
list9 = list(set2)
print(list9)    # ['a', 'c', 'b']
list10 = list(tuple7)
print(list10)   # [11, 22, 33]

# 转为集合
set3 = set(list8)
print(set3)     # {1, 2, 3}
set4 = set(tuple7)
print(set4)     # {33, 11, 22}