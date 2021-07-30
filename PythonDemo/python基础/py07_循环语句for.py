# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: py07_循环语句for.py
# @Author: xiaohanzhang
# @Date: 2021/7/30

str = 'hello'
for i in str:
    print(i)
print('*' * 50)

# 输出10以内数字
for i in range(10):
    print(i)
print('*' * 50)

# break 输出5以内数字
for i in range(10):
    if i == 5:
        break
    print(i)
print('*' * 50)

# continue 输出除5以外数字
for i in range(10):
    if i == 5:
        continue
    print(i)
print('*' * 50)


# else 循环正常结束之后要执行的代码,break不会执行else中代码，continue会执行else代码
for i in range(5):
    print(i)
else:
    print('循环正常结束')     # 会执行
print('*' * 50)

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print('循环正常结束')     # 不会执行
print('*' * 50)

for i in range(5):
    if i == 3:
        continue
    print(i)
print('循环正常结束')     # 会执行
print('*' * 50)