#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_24_进程池.py
# @Author: xiaohanzhang
# @Data: 2020/9/28

from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d" % (msg, os.getpid()))
    # random.random()随机生成0-1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print("%s执行完毕，耗时%0.2f" % (msg, t_stop - t_start))


po = Pool(3)
for i in range(0, 10):
    # Pool().apply_async(要调用的目标,(传递给目标的参数元组,))
    # 每次循环将用空闲出来的子线程来调用目标
    po.apply_async(worker, (i, ))

print("---------- start -----------")
# 关闭进程池，关闭后，po不再接收新的请求
po.close()
# 等待po中所有子进程执行完成，必须放在close()语句之后
po.join()
print("---------- end -------------")


def main():
    pass


if __name__ == "__main__":
    main()