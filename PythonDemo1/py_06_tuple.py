#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo1
# @File: py_06_tuple.py
# @Author: xiaohanzhang
# @Data: 2020/8/13

# 元组内数据不能修改
my_info_tuple = ("猪八戒", 17, "船长")
print(my_info_tuple)

print(my_info_tuple[1])

print(my_info_tuple.index("船长"))

# 某个元素在tuple中出现的次数
my_info_tuple.count("船长")

len(my_info_tuple)

for name in my_info_tuple:
    print(name)


# 元组和列表的转换
list1 = ["猪八戒", "孙悟空", "沙和尚"]
tuple1 = ("柯南", "路飞", "鸣人")

# 元组转列表
list2 = list(tuple1)
print(type(list2), list2)

# 列表转元组
tuple2 = tuple(list1)
print(type(tuple2), tuple2)

# 只有一个元素的元组
tuple = (1,)
print(tuple)

# 元组相加
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
tuple3 = tuple1 + tuple2
print(tuple3)

print(tuple3 * 2)

tuple4 = (1, 8, ['a', 'b', 'c'], 'iii')
tuple4[2][0] = 'aaa'
print(tuple4)