#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py15_函数.py
# @Author: xiaohanzhang
# @Data: 2020/8/17
"""
可变类型:
列表、字典、集合
不可变类型:
字符串、整型、浮点型、元组

"""
# 变量
# 注意：在开发时，应该把模块中的全局变量定义在所有函数的上方
# 全局变量名应加 g_ 或 gl_ 前缀
gl_a = 10
gl_name = "唐僧"


# ----------------------------------- 定义函数 -------------------------------------------
def f1():
    print('无参数，无返回值函数')


f1()


# a,b是形参 有参数无返回值函数
def add(a, b):
    result = a + b
    print(result)


add(1, 9)


# 无参数有返回值函数
def get_name():
    return 'xiaobai'


print(get_name())


# 有参数有返回值函数
def add2(a, b):
    result = a + b
    return result


print(add2(3, 4))
print('*' * 50)


# ----------------------------------- 函数说明文档 -------------------------------------------
def test(num):
    """ 函数的说明文档 """
    result = "result"
    return result


# 查看函数说明文档
help(test)


def add3(a, b):
    """
    函数说明文档的高级写法（写完函数内容后，输入\"""点击回车\"""）
    :param a: 第一个数字
    :param b: 第二个数字
    :return: 返回值
    """
    return a + b


# ----------------------------------- 函数嵌套 -------------------------------------------
def testA():
    print('testA start---')
    print('testA end---')


def testB():
    print('testB start...')
    testA()
    print('testB end...')


testB()


# 函数嵌套应用
def sum_nums(a, b, c):
    sum = a + b + c
    return sum


def avg_nums(a, b, c):
    avg = sum_nums(a, b, c) / 3
    return avg

print(f'平均值是{avg_nums(3, 4, 8)}')


# ----------------------------------- 变量作用域 -------------------------------------------
# 函数内部修改全局变量
def demo1():

    # global关键字声明变量为全局变量
    global gl_name
    gl_name = "悟空"
    print(gl_name)


demo1()
print(gl_name)
