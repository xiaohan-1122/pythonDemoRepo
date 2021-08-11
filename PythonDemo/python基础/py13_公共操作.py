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




""" 容器类型转换 """