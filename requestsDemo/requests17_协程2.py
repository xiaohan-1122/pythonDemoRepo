# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: requests17_协程2.py
# @Author: xiaohanzhang
# @Date: 2021/1/15

import asyncio
import time


async def test(num):
    print(f'正在处理。。。。{num}')
    # 在异步协程中出现同步模块相关代码，将无法实现异步
    # time.sleep(2)
    # 当在asynicio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print(f'处理完毕。。。{num}')


if __name__ == '__main__':

    start_time = time.time()

    # 任务列表存放多个任务对象
    tasks = [asyncio.ensure_future(test(i)) for i in range(3)]
    # tasks = []
    # for i in range(3):
    #     task= asyncio.ensure_future(test(i))
    #     tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    ens_time = time.time()
    print(ens_time - start_time)

