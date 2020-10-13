#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_20异常.py
# @Author: xiaohanzhang
# @Data: 2020/9/25
# --------------------------------- 捕获异常 -------------------------------------
try:
    # 不能确定正确执行的代码
    num = int(input("请输入一个数字:"))
except:
    # 错误的处理代码
    print("请输入正确数字")

print('-' * 50)

# --------------------------------- 根据错误类型捕获异常 -------------------------------------
try:
    num = int(input("请输入一个整数:"))
    result = 8 / num
except ValueError as e:
    print('except:', e)
except ZeroDivisionError as e:
    print('except:', e)
except Exception as e:
    print("未知错误 %s" % e)
else:
    #  没有异常才会执行的代码
    print(result)
finally:
    # 无论是否有异常 都会执行的代码
    print("-" * 50)

# --------------------------------- 异常的传递 -------------------------------------
"""
当方法的执行出现异常，会将异常传递给调用方法的一方
如果传递到主程序，仍然没有异常处理，程序才会被终止
提示：
在开发中，可以在主函数中增加异常捕获，在主函数中调用的其它函数，只要出现异常，就会传递到主函数的异常捕获中
这样就不需要在代码中增加大量的异常捕获，能够保证代码的整洁
"""


def demo1():
    return int(input("请输入一个整数："))


def demo2():
    return demo1()


try:
    demo2()
except ValueError as e:
    print("请输入正确整数")
except Exception as e:
    print('未知错误 %s' % e)


print("-" * 50)


# --------------------------------- 抛出raise异常 -------------------------------------
"""
在开发中，除了代码执行出错会抛出异常之外，还可以根据应用程序特有的业务需求主动抛出异常
步骤：
1.创建一个Exception 异常类
2.使用raise关键字抛出异常对象
"""


def input_password():
    password = input("请输入密码：")
    if len(password) >= 8:
        return password

    raise Exception("密码长度不够")


try:
    print(input_password())
except Exception as e:
    print(e)

# --------------------------------- 自定义异常 -------------------------------------
class ShortInputError(Exception):
    def __init__(self, lenght, min_len):
        self.lenght = lenght
        self.min_len = min_len

#     设置抛出异常的描述信息
    def __str__(self):
        return f'输入的长度是{self.lenght}, 不能少于{self.min_len}个字符'


def input_pwd():
    try:
        pwd = input('请输入密码:')
        if len(pwd) < 3:
            raise ShortInputError(len(pwd), 3)
    except Exception as e:
        print(e)
    else:
        print('密码输入完成')
