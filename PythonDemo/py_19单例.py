#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_19单例.py
# @Author: xiaohanzhang
# @Data: 2020/9/25
# ----------------------------------- __new__ 方法 ---------------------------------------
"""
使用类名创建对象时，会先调用__new__ 方法为对象分配内存空间
__new__是一个由object基类提供的内置的静态方法，主要作用有两个：
1.在内存中为对象分配内存空间
2.返回对象的引用
python解释器获得对象的引用后，将引用作为第一个参数传递给__init__方法
注：__new__ 是静态方法，需主动传递cls参数
"""


class MusicPlayer(object):

    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):

        if cls.instance is None:
            cls.instance = super().__new__(cls)
            print("创建对象，分配内存空间")
        return cls.instance

    def __init__(self):
        # 初始化只执行一次
        if MusicPlayer.init_flag:
            return

        MusicPlayer.init_flag = True
        print("播放器初始化")


player = MusicPlayer()
print(player)
player2 = MusicPlayer()
print(player2)