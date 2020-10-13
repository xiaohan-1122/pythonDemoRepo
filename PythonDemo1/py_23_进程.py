#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo1
# @File: py_23_进程.py
# @Author: xiaohanzhang
# @Data: 2020/9/28

import multiprocessing
import time
'''
进程之间不共享全局变量
主进程会等待子进程执行结束再结束
'''

def sing():
    """ 唱歌5s """
    for i in range(5):
        print("------正在唱歌-------")
        print('thread %s is running...' % multiprocessing.current_process().name)
        time.sleep(1)


def dance():
    """ 跳舞5s """
    for i in range(5):
        print("---------正在跳舞-------")
        print('thread %s is running...' % multiprocessing.current_process().name)
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=sing)
    p2 = multiprocessing.Process(target=dance)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()