#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_16_继承.py
# @Author: xiaohanzhang
# @Data: 2020/9/24

"""
1.子类对象不能在自己的方法内部，直接访问父类的 私有方法 或 私有属性
2.子类对象可以通过父类的公有方法 间接 访问到 私有方法 和 私有属性
"""

# ----------------------------------------- 单继承 ------------------------------------------------
class Animal(object):

    def __init__(self, name):
        self.name = name
        self.__age = 2

    def eat(self):
        print("%s 吃" % self.name)

    def drink(self):
        print("%s 喝" % self.name)

    def run(self):
        print("%s 跑" % self.name)

    def sleep(self):
        print("%s 睡" % self.name)

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
        print(f'age = {self.__age}')


class Dog(Animal):

    def bark(self):
        print("%s 叫" % self.name)

    # 子类对象不能调用父类的私有方法
    def __test(self):
        print("Dog的私有方法")

    # 子类对象可以通过调用父类的公有方法,间接调用父类的私有方法
    def ttt(self):
        print("Dog的公有方法")
        self.__test()


class Cat(Animal):

    def catch(self):
        print("%s 抓老鼠" % self.name)


class RoaringDog(Dog):
    def fly(self):
        print("%s 会飞" % self.name)

    # 重写(override)父类方法
    def bark(self):
        super().bark()     # 同时执行父类中的方法
        print("%s叫的和神一样" % self.name)


dog = Dog("旺财")
dog.eat()
dog.bark()
dog.ttt()
print(dog.get_age())
dog.set_age(3)

cat = Cat("汤姆")
cat.drink()
cat.catch()

xtq = RoaringDog('哮天犬')
xtq.run()
xtq.fly()
xtq.bark()


''' 查看继承的层级关系 '''
print(Dog.__mro__)
print("=" * 50)

# ----------------------------------------- 多继承 ------------------------------------------------
"""
子类可以拥有多个父类，并且具有所有父类的属性和方法
注意：如果父类之间存在同名的属性或方法，应该避免使用多继承

语法：
class 类名(父类1,父类2...)
    pass
"""
class D1(object):
    def demo_1(self):
        print("D1的demo()方法")


class D2(object):
    def demo_2(self):
        print('D2的demo()方法')

class D3(D1, D2):
    pass


d = D3()
d.demo_1()
d.demo_2()


# ----------------------------------------- 单继承：子类调用父类同名方法和属性 ------------------------------------------------
class E1(object):
    def demo(self):
        print('E1')

class E2(E1):
    def demo(self):
        super().__init__()
        super().demo()

e = E2()
e.demo()

# ----------------------------------------- 多继承：子类调用父类同名方法和属性 ------------------------------------------------
class A(object):

    def __init__(self):
        self.name = 'A_name'

    def test(self):
        print(f'我是{self.name}')


class B(object):
    def __init__(self):
        self.name = 'B_name'

    def test(self):
        print(f'我是{self.name}')


class C(A, B):
    def __init__(self):
        self.name = 'C_name'

    def test(self):
        # 如果先调用了父类的属性和方法，父类属性会覆盖子类属性，故在调用属性前，先调用子类自己的初始化方法
        self.__init__()
        print(f'我是{self.name}')

    def test_A(self):
        # 调用父类方法，为了保证调用到的也是父类的属性，必须在调用父类方法前调用父类的初始化
        A.__init__(self)
        A.test(self)

    def test_B(self):
        B.__init__(self)
        B.test(self)


c = C()
c.test_A()
c.test_B()
c.test()

