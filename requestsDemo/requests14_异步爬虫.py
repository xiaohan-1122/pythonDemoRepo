# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: requests14_异步爬虫.py
# @Author: xiaohanzhang
# @Date: 2021/1/11
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
    urls = ['https://90-cucc-dd.tv002.com/down/389600e516857fb87f760505c6ade3ee/Hookshot_1.16.3_%2832%29_%28%E6%9C%80%E4%BD%8E10.12%29__macwk.com.dmg?cts=wt-f-D39A88A109A215F62fce&ctp=39A88A109A215&ctt=1610372004&limit=1&spd=550000&ctk=389600e516857fb87f760505c6ade3ee&chk=72db8a525c65f1a91a5b0742d63e289d-18748254&mtd=1',
        'https://90-cucc-dd.tv002.com/down/cc097c59483b29bd904a37c618c46a2c/OpenCore_Configurator_2.22.2.0_%28%E6%9C%80%E4%BD%8E10.11%29__macwk.com.dmg?cts=wt-f-D39A88A109A215F62fce&ctp=39A88A109A215&ctt=1610371889&limit=1&spd=550000&ctk=cc097c59483b29bd904a37c618c46a2c&chk=4a645f880f16b50a1271cc4a03b24548-13350678&mtd=1',
        'https://90-cucc-dd.tv002.com/down/ee12982a1b3ef0c6f0080144cd4975cd/Progressive_Downloader_4.7.21_%284.7.10658%29_%28%E6%9C%80%E4%BD%8E10.10%29__macwk.com.dmg?cts=wt-f-D39A88A109A215F62fce&ctp=39A88A109A215&ctt=1610371973&limit=1&spd=550000&ctk=ee12982a1b3ef0c6f0080144cd4975cd&chk=c1c30047d5e7f948edd8029666c3da9a-20608476&mtd=1']
    name_list = ['111', '222', '333']
    start_time = time.time()
    # for name in name_list:
    #     test(name)

    # 创建线程池对象
    pool = Pool(3)
    # 将列表中每一个元素传递给test方法进行处理
    pool.map(test, name_list)
    end_time = time.time()
    print(f'耗时：{end_time - start_time}')


if __name__ == '__main__':
    main()