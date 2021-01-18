# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: requests15_进程池.py
# @Author: xiaohanzhang
# @Date: 2021/1/11
# 进程池
from multiprocessing.pool import Pool
import requests
import time
# 线程池、进程池
# 好处：降低系统对进程、线程创建和销毁的频率，降低系统开销
# 弊端：池中线程、进程有上限


def get_content(url, index):
    print(f'正在爬取第{index}个')
    res = requests.get(url)
    if res.status_code == 200:
        print('爬取成功！')


def test(name):
    print(f'正在下载{name}')
    time.sleep(3)
    print(f'下载成功{name}')


def main():
    name_list = ['111', '222', '333']
    start_time = time.time()
    # for name in name_list:
    #     test(name)

    # 创建进程池对象
    pool = Pool(3)
    # 将列表中每一个元素传递给test方法进行处理
    pool.map(test, name_list)

    end_time = time.time()
    print(f'耗时：{end_time - start_time}')


if __name__ == '__main__':
    main()