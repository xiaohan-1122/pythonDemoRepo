# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: requests16_协程.py
# @Author: xiaohanzhang
# @Date: 2021/1/14

"""
单线程+异步协程
event_loop: 事件循环，相当于一个无限循环，可以把一些函数注册到这个事件循环上，当满足某些条件时，函数就会被循环执行
coroutine: 协程对象，可以将协程对象注册到事件循环中，它会被事件循环调用
            可以使用async关键字定义一个方法，这个方法在调用时不会立即被执行，而是返回一个协程对象
task: 任务，它是对协程对象的进一步封装，包含了任务的各个状态
future: 代表将来执行或还没执行的任务，实际上和task没有本质区别
async: 定义一个协程
await: 用来挂起阻塞方法的执行

"""
