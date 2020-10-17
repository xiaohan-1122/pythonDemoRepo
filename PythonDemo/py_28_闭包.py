#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_28_闭包.py
# @Author: xiaohanzhang
# @Data: 2020/10/17
"""
在函数嵌套的前提下，内部函数使用了外部函数的变量，把这个内部函数成为闭包。
- 闭包构成条件
1.1 函数嵌套（函数里面再定义函数）
1.2 内部函数使用外部函数的变量
1.3 外部函数返回了内部函数
"""
def func_out1():
    num1 = 10
    def func_inner(num2):
        result = num1 + num2
        print(f'result = {result}')
    return func_inner


# 闭包保存了外部函数的变量num1，执行闭包都是在num1 = 10的基础上进行计算。
func_out1()(2)  # result = 13
f = func_out1()
f(3)    # result = 14


def func_out2(num1):
    def func_inner(num2):
        result = num1 + num2
        print(f'result = {result}')
    return func_inner


f = func_out2(1)
f(1)    # result = 2


# ------------------ 闭包修改外部函数变量 ------------------------
def func_out3(num1):
    def func_inner():
        # 在闭包内修改外部函数变量，需要使用nonlocal关键字修饰
        nonlocal num1
        num1 += 1

    print(f'修改前:num1 = {num1}')
    func_inner()
    print(f'修改后:num1 = {num1}')
    return func_inner


func_out3(1)()


def func_out4(num1):
    def func_inner():
        nonlocal num1
        num1 += 1
        return num1

    return func_inner


f = func_out4(10)
print(f())
