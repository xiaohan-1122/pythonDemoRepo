#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo1
# @File: py_17多态.py
# @Author: xiaohanzhang
# @Data: 2020/9/24
"""
不同的子类对象调用相同的父类方法，产生不同的执行结果
1. 多态可以增加代码的灵活度
2. 以继承 和 重写父类方法 为前提
3. 是调用方法的技巧，不会影响到类内部设计
"""


class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s蹦蹦跳跳的玩耍~" % self.name)


class XiaoTianQuan(Dog):

    def game(self):
        print("%s飞到天上去玩耍" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))
        dog.game()


wangcai = Dog('旺财')
xiaolan = Person('小兰')
xiaolan.game_with_dog(wangcai)

xiaotianquan = XiaoTianQuan('哮天犬')
xiaohong = Person('小红')
xiaolan.game_with_dog(xiaotianquan)