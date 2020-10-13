#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo1
# @File: py_07_dictionary.py
# @Author: xiaohanzhang
# @Data: 2020/8/13

# 创建字典
# 有数据字典
student_dic = {"name": "小明", "age": 10, "score": 67.2}
# 空字典
dic1 = {}
dic2 = dict()

# 取值
# key不存在返回None
student_dic.get("nnn")

# key不存在返回指定value
student_dic.get("nnn", -1)

# student_dic["key"],key不存在会报错,in判断的是key
if "nnn" in student_dic:
    print(student_dic["nnn"])
else:
    print("key不存在")


# 删除元素
del student_dic['score']

student_dic.pop("age")
print(student_dic)

# 增加、修改元素
student_dic["height"] = 155
print(student_dic)

# 统计键值对数量
len(student_dic)

# 合并字典, 如果被合并的字典中包含已经存在的键值对，会覆盖原有键值对
dic1 = {"key1": "value1"}
dic2 = {"key2": "value2", "key1": "value3"}
dic1.update(dic2)
print(dic1)

# 清空字典
dic1.clear()
print(dic1)

print("-" * 50)


# 循环遍历
for key in student_dic.keys():
    print("key =", key)

print("-" * 50)

for value in student_dic.values():
    print("value =", value)

print("-" * 50)

for key, value in student_dic.items():
    print("key =", key, ", value =", value)

print("-" * 50)