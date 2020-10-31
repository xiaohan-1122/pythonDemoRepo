#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_31_property属性.py
# @Author: xiaohanzhang
# @Data: 2020/10/28
"""
property属性就是负责把一个方法当做属性进行使用，这样做可以简化代码。
两种方式：
1.装饰器方式
    该方式的property属性，方法名要保持一致
2.类属性方式
"""
# -------------- 装饰器方式 ------------------
class Person(object):
    def __init__(self):
        self._age = 0

    # 装饰器方式的propety，把age方法当做属性使用，表示获取属性时，会执行下面的方法
    @property
    def age(self):
        return self._age

    # 把age方法当做属性使用，表示当设置属性是会执行下面的方法
    @age.setter
    def age(self, new_age):
        if new_age >= 130:
            print('成精了')
        elif new_age <= 0:
            print('不能为负数')
        else:
            self._age = new_age


p = Person()
print(p.age)
p.age = 12
print(p.age)

# --------------- 类属性方式 --------------------
class Student(object):
    def __init__(self):
        self._name = ''

    def get_name(self):
        """当获取name属性时，会执行该方法"""
        return self._name

    def set_name(self, new_name):
        """当设置name属性时，会执行该方法"""
        if new_name is not None:
            self._name = new_name

    # 类属性方式的property属性
    name = property(get_name, set_name)


s = Student()
print(s.name)
s.name = 'xiaolan'
print(s.name)