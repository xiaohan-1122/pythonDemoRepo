#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py06_循环语句while.py
# @Author: xiaohanzhang
# @Data: 2020/8/5

# 打印5次啊啊啊啊
i = 0
while i < 5:
    print('啊啊啊啊')
    i += 1

print('=' * 50)

# 1-100累加
result = 0
i = 1
while i <= 100:
    result += i
    i += 1
print(f"1-100累加的值是 {result}")
print('=' * 50)

# 1-100偶数累加
result = 0
i = 0
while i <= 100:
    result += i
    i += 2
print(f'1-100偶数累加的值是 {result}')

result = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1
print(f'1-100偶数累加的值是 {result}')

# break和continue
"""
break   终止循环
continue    退出当前一次循环，继续下一次循环
"""
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
print('*' * 50)

i = 0
while i < 10:
    if i == 5:
        i += 1
        continue    # continue之前要修改计数器，否则会陷入死循环
    print(i)
    i += 1
print('*' * 50)

row = 1
while row < 5:
    col = 1
    while col <= row:
        print('*', end=' ')
        col += 1
    row += 1
    print('')
print('*' * 50)

# 九九乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print(col, "*", row, "=", col * row, end="\t")
        col += 1
    print("")
    row += 1

# else 循环正常结束之后要执行的代码,break不会执行else中代码，continue会执行else代码
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print('正常结束了')  # 会执行

i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
else:
    print('正常结束了')  # 不会执行
print('*' * 50)

i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
else:
    print('正常结束了')  # 会执行

