#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_15封装.py
# @Author: xiaohanzhang
# @Data: 2020/9/24

"""
需求：
1.小明体重75.0kg
2.小明每次跑步会减肥0.5kg
3.小明每次吃东西会增重1kg
"""


class Person(object):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return '%s的体重是%.1fkg' % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5
        print('%s爱跑步' % self.name)

    def eat(self):
        self.weight += 1
        print('%s吃了一顿饭' % self.name)


person = Person('小明', 75.0)
print(person)

person.run()
print(person)

person.eat()

print(person)


"""
需求：
1.士兵许三多有一把AK47
2.士兵可以开火
3.枪能够发射子弹
4.枪装填子弹 可增加子弹数量
"""
class Gun(object):
    def __init__(self, model):
        self.model = model
        self.buttet_count = 0

    def shoot(self):
        if self.buttet_count > 0:
            self.buttet_count -= 1
            print("射击")
        else:
            print("%s没子弹" % self.model)

    def add_bullet(self, count):
        print("装子弹")
        self.buttet_count += count


class Soldier(object):
    def __init__(self, name):
        self.name = name
        self.gun = None

    def add_gun(self, gun):
        self.gun = gun

    def add_bullet(self, count):
        if self.gun is None:
            print("没有枪")
        else:
            self.gun.add_bullet(count)

    def fire(self):
        if self.gun is None:
            print("士兵没有枪")
        else:
            print("开火")
            self.gun.shoot()


gun = Gun("AK47")
soldier = Soldier("许三多")
soldier.add_gun(gun)
soldier.add_bullet(20)
soldier.fire()
