# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: py16_函数参数.py
# @Author: xiaohanzhang
# @Date: 2021/8/18

# 可变类型可作为实参
# -------------------------------------- 位置参数 --------------------------------------
# 调用函数时，根据参数的定义位置来传递参数，传递和定义参数的顺序和个数必须是一致的
def user_info(name, age, gender):
    print(f'名字是{name}, 年龄是{age}, 性别是{gender}')


user_info('小黑', 13, '男')


# -------------------------------------- 关键字参数 --------------------------------------
# 函数调用时，根据“键=值”的形式加以指定，如果有位置参数，位置参数必须在关键字参数前面，关键字参数之间没有顺序
def user_info1(name, age=10, gender='女'):
    print(f'名字是{name}, 年龄是{age}, 性别是{gender}')


user_info1('小白', gender='男', age=15)


# -------------------------------------- 缺省参数 --------------------------------------
# 函数调用时，如果传递缺省参数，则修改缺省参数默认值，否则使用默认值
def user_info2(name, age, gender='男'):
    print(f'名字是{name}, 年龄是{age}, 性别是{gender}')


user_info2('小蓝', 20)


# def add_end(L=[]): # []是可变的
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# -------------------------------------- 不定长参数之位置参数 --------------------------------------
# 不确定调用函数时会传多少个参数
def user_info3(*args):
    print(args)


user_info3('小红')        # ('小红',)
user_info3('小绿', 44)    # ('小绿', 44)


# -------------------------------------- 不定长参数之关键字参数 --------------------------------------
def user_info4(**kwargs):
    print(kwargs)


user_info4(name='小紫', age=22, gender='女')      # {'name': '小紫', 'age': 22, 'gender': '女'}


# ------------------------------------- 私有函数 ---------------------------------------
# _xxx和__xxx这样的函数或变量就是非公开的（private）,不应该被直接引用
def __privateFun__(name):
    return 'Hello, %s' % name


print(__privateFun__("xiaoli"))


print('===================================================================')

L = ['Hello', 'World', 'IBM', 'Apple']
list = [s.lower() for s in L]
print(list)     # ['hello', 'world', 'ibm', 'apple']

# 查看对象内的所有属性和方法
print(list.__dir__())