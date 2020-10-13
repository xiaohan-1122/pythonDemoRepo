#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_22_线程.py
# @Author: xiaohanzhang
# @Data: 2020/9/28
import threading
import time

'''
线程之间执行是无序的
主线程会等待所有子线程结束再结束
线程之间共享全局变量
将子线程设置为主线程的守护线程，主线程结束，子线程之间销毁
'''
def sing():
    """ 唱歌5s """
    for i in range(5):
        print("------正在唱歌-------")
        print('thread %s is running...' % threading.current_thread().name)
        time.sleep(1)


def dance():
    """ 跳舞5s """
    for i in range(5):
        print("---------正在跳舞-------")
        print('thread %s is running...' % threading.current_thread().name)
        time.sleep(1)


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print("I'm " + self.name + ' @ ' + str(i))


def test1(temp):
    temp.append(33)
    print("-------- in test1 temp = %s" % str(temp))


def test2(temp):
    print("-------- in test2 temp = %s" % str(temp))


gl_num = 0
# 创建互斥锁 默认是没有上锁的
mutex = threading.Lock()


def test3(count):
    global gl_num
    # 上锁
    # 如果之前没有被上锁，则上锁成功
    # 如果已经被上锁，则会堵塞在这里，直到锁被解开
    mutex.acquire()

    for i in range(count):
        gl_num += 1

    # 解锁
    mutex.release()
    print("-------in test3 gl_num = %d" % gl_num)


def test4(count):
    global gl_num
    mutex.acquire()
    for i in range(count):
        gl_num += 1
    mutex.release()
    print("-------in test4 gl_num = %d" % gl_num)


def main():
    print("---- 开始 ----:%s" % time.ctime())
    # 方式一
    t1 = threading.Thread(target=sing)  # 没有()
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

    # 方式二
    t3 = MyThread()
    t3.start()

    # target指定这个线程执行哪个函数
    # args指定 调用函数时，传递什么参数
    t4 = threading.Thread(target=test3, args=(100000,))
    t5 = threading.Thread(target=test4, args=(100000,))
    t4.start()
    t5.start()

    print("------- in main thread g_nums = %s" % str(gl_num))

    while True:
        length = len(threading.enumerate())
        print("当前运行的线程数为: %d", length)

        if length <= 1:
            break
        time.sleep(0.5)


if __name__ == "__main__":
    main()