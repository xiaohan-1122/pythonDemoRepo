#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo1
# @File: py_14_class.py
# @Author: xiaohanzhang
# @Data: 2020/8/30
"""
class后面紧接着是类名，类名命名规则大驼峰，紧接着是(object)，表示该类是从哪个类继承下来的
定义类格式:

class 类名:

    def 方法名(self, 参数):
        pass


创建对象格式:

对象变量 = 类名()
"""


class Student(object):

    def study(self):
        print("学习")


student1 = Student()
student1.study()

# ------------------------------ 在类的外部给对象增加属性（不推荐）---------------------------------
student1.gender = "男"
print(student1.gender)


# ---------------------------------------- 初始化方法 ------------------------------------------
class Person(object):

    def __init__(self):
        print("初始化方法")
        self.name = "Naruto"


# 使用类名()创建对象时，会自动调用__init__方法
# __init__方法用来定义一个类具有哪些属性
person = Person()
print(person.name)


class Cat(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s爱吃鱼' % self.name)


cat = Cat('Tom', 2)
print(cat.name)
cat.eat()


# ---------------------------------------- 内置方法__del__ ------------------------------------------
# 对象从内存中被销毁前，会自动调用__del__
class Dog(object):

    def __init__(self, name):
        self.name = name
        print('%s 来喽' % self.name)

    def __del__(self):
        print("%s 走了" % self.name)

    def __str__(self):

        return '我是小狗%s' % self.name


dog = Dog('xiaohei')
# ---------------------------------------- 内置方法__str__ ------------------------------------------
# 必须返回一个字符串
# 如果在开发中，使用print输出一个对象时，希望打印自定义内容，可以使用__str__方法
print(dog)


# ---------------------------------------- 访问限制 ------------------------------------------
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Students(object):

    def __init__(self, name, score):
        # 无法从外部访问实例变量.__name和实例变量.__score
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            # raise ValueError('bad score')
            self.__score = 0


student = Students('Naruto', 60)
print('%s: %s' % (student.get_name(), student.get_score()))

