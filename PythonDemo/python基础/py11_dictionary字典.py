#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py11_dictionary字典.py
# @Author: xiaohanzhang
# @Data: 2020/8/13

# 创建字典
# 有数据字典
student_dict = {'name': '小明', 'age': 10, 'score': 67.2, 'gender': '男'}
# 空字典
dict1 = {}
dict2 = dict()

# 增加或修改 key不存在则新增，key存在则修改
dict1['name'] = 'xiaobai'
print(dict1)    # {'name': 'xiaobai'}
dict1['name'] = '路飞'
print(dict1)    # {'name': '路飞'}


# 取值
# get() key不存在返回None
a = student_dict.get('name')
print(a)    # 小明
# key不存在返回指定value
a = student_dict.get("nnn", -1)
print(a)    # -1

dict1['name']
# dict["key"],key不存在会报错,in判断的是key
if "nnn" in dict1:
    print(dict1["nnn"])
else:
    print("key不存在")


# 删除元素
del student_dict['score']
print(student_dict)     # {'name': '小明', 'age': 10, 'gender': '男'}

age = student_dict.pop("age")     # {'name': '小明', 'gender': '男'}
print(age)      # 10
print(student_dict)
# 清空字典
dict1.clear()
print(dict1)    # {}


# 统计键值对数量
l = len(student_dict)
print(l)    # 2

# 合并字典, 如果被合并的字典中包含已经存在的键值对，会覆盖原有键值对
dic1 = {"key1": "value1"}
dic2 = {"key2": "value2", "key1": "value3"}
dic1.update(dic2)
print(dic1)     # {'key1': 'value3', 'key2': 'value2'}

print("-" * 50)


# 循环遍历
for key in student_dict.keys():
    print("key =", key)

print("-" * 50)

for value in student_dict.values():
    print("value =", value)

print("-" * 50)

for key, value in student_dict.items():
    print("key =", key, ", value =", value)

print("-" * 50)