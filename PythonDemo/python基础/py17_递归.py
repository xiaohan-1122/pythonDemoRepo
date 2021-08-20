# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: py17_递归.py
# @Author: xiaohanzhang
# @Date: 2021/8/20

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
