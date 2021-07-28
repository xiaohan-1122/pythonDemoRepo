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


names = ['小红', '小蓝', '小黄']

index = 0
while index < len(names):
    print(names[index])
    index += 1
print('=' * 50)

index = 0
while index < len(names):
    print(names[index])
    index += 1
else:
    print('white循环正常结束后，会执行的代码')
print('=' * 50)


for name in names:
    print(name)
else:
    print("for循环正常结束后，会执行的代码")
print('=' * 50)


# range()函数，可以生成一个整数序列,比如range(5)生成的序列是从0开始小于5的整数[0,1,2,3,4]
sum = 0
for num in list(range(101)):
    sum += num
print(f'1-100的和是：{sum}')


i = 0
while i < len(names):
    if i == 1:
        break
    print(names[i])
    i += 1

print('=' * 50)


# 10以内奇数
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
print('=' * 50)


row1 = 1
while row1 <= 5:
    col1 = 1
    while col1 <= row1:
        print("*", end="")
        col1 += 1
    print("")
    row1 += 1

print('=' * 100)

# 九九乘法表
row2 = 1
while row2 <= 9:
    col2 = 1
    while col2 <= row2:
        print(col2, "*", row2, "=", col2 * row2, end="\t")
        col2 += 1
    print("")
    row2 += 1

print('=' * 100)

