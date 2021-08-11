#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py10_tuple元组.py
# @Author: xiaohanzhang
# @Data: 2020/8/13

"""
元组内数据不能修改
"""

my_info_tuple = ("猪八戒", 17, "船长")
print(my_info_tuple)

# 只有一个元素的元组
t = (1,)
print(t)    # (1,)

tuple1 = ('小白', '小红', '小鹅', '小黑', '小白')
# 按下标查找数据
print(tuple1[1])

# 1. index() 获取元素下标,如果元素不在列表中，会抛异常
index1 = tuple1.index('小红')
print(index1)   # 1

# 2.count() 统计指定数据在当前列表中出现的次数
count = tuple1.count('小白')
print(count)    # 2

# 3.len() 列表的长度,即列表中数据的个数
count = len(tuple1)
print(count)    # 5

# 元组遍历 while
i = 0
while i < len(tuple1):
    print(tuple1[i])
    i += 1

# 元组遍历 for
for name in tuple1:
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



# 元组相加
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
tuple3 = tuple1 + tuple2
print(tuple3)

print(tuple3 * 2)

tuple4 = (1, 8, ['a', 'b', 'c'], 'iii')
tuple4[2][0] = 'aaa'
print(tuple4)