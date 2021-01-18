# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: requests18_协程应用.py
# @Author: xiaohanzhang
# @Date: 2021/1/18

import requests
import asyncio


async def get_video(url, count):
    print(f'正在下载。。。{count}')
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'./{count}.mp4', 'wb') as f:
            f.write(response.content)
        print(f'下载完成。。。{count}')
    else:
        print('下载视频失败')


if __name__ == '__main__':
    urls = [
        'https://video.pearvideo.com/mp4/adshort/20210114/cont-1716345-15574909_adpkg-ad_hd.mp4',
        'https://vt1.doubanio.com/202101181411/e9102172c6d5c7300fe26bc9a14e5927/view/movie/M/402680884.mp4',
        'https://vt1.doubanio.com/202101181411/b6877081360b0d85f6243d9109fb6b2e/view/movie/M/402680750.mp4'
    ]
    tasks = [asyncio.ensure_future(get_video(urls[i], i)) for i in range(len(urls))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))