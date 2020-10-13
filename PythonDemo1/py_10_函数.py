#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo1
# @File: py_10_函数.py
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


def test(num):
    """ 函数的说明文档 """
    print("函数内部参数num的内存地址 %d" % id(num))

    result = "result"
    print("result的内存地址 %d" % id(result))

    return result


print("a的内存地址 %d" % id(gl_a))
# 查看函数说明文档
help(test)

r = test(gl_a)

print("函数返回值r的内存地址%d" % id(r))


# 函数内部修改全局变量
def demo1():

    # global关键字声明变量为全局变量
    global gl_name
    gl_name = "悟空"
    print(gl_name)


demo1()
print(gl_name)


# 位置参数
def user_info(name, age, gender):
    print(f'名字是{name}, 年龄是{age}, 性别是{gender}')


user_info('小黑', 13, '男')

# 关键字参数
user_info('小白', gender='男', age=15)


# 缺省参数
def user_info2(name, age, gender='男'):
    print(f'名字是{name}, 年龄是{age}, 性别是{gender}')


user_info2('小蓝', 20)


# def add_end(L=[]): # []是可变的
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 不定长参数
def user_info3(*args):
    print(args)


user_info3('小红')        # ('小红',)
user_info3('小绿', 44)    # ('小绿', 44)


# 不定长参数之关键字参数
def user_info4(**kwargs):
    print(kwargs)


user_info4(name='小紫', age=22, gender='女')      # {'name': '小紫', 'age': 22, 'gender': '女'}

# ------------------------------------- 递归函数 ---------------------------------------
# n! = 1 x 2 x 3 x ... x n
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))


# 尾递归
'''
尾递归是指，在函数返回的时候，调用函数本身，并且，return语句不能包含表达式。
编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
'''
def fact_iter(num, result=1):
    if num == 1:
        return result
    return fact_iter(num - 1, num * result)


fact_iter(5)


# ------------------------------------- 私有函数 ---------------------------------------
# _xxx和__xxx这样的函数或变量就是非公开的（private）,不应该被直接引用
def __private__(name):
    return 'Hello, %s' % name


print(__private__("xiaoli"))


print('===================================================================')

L = ['Hello', 'World', 'IBM', 'Apple']
list = [s.lower() for s in L]
print(list)     # ['hello', 'world', 'ibm', 'apple']

# 查看对象内的所有属性和方法
print(list.__dir__())