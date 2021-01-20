# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: crawler19_aiohttp异步下载.py
# @Author: xiaohanzhang
# @Date: 2021/1/18

import aiohttp
import asyncio
import aiofiles


async def get_video(url, count):
    print(f'开始下载。。。{count}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # text()返回字符串形式的响应数据
            # read()返回二进制形式的响应数据
            # json()返回json对象
            if response.status == 200:
                async with aiofiles.open(f'./{count}.mp4', 'wb') as f:
                    data = await response.read()
                    await f.write(data)
                print(f'下载完成。。。{count}')
            else:
                print(f'下载视频失败{count}')


if __name__ == '__main__':
    urls = [
        'https://video.pearvideo.com/mp4/adshort/20210114/cont-1716345-15574909_adpkg-ad_hd.mp4',
        'https://vt1.doubanio.com/202101181411/e9102172c6d5c7300fe26bc9a14e5927/view/movie/M/402680884.mp4',
        'https://vt1.doubanio.com/202101181411/b6877081360b0d85f6243d9109fb6b2e/view/movie/M/402680750.mp4'
    ]
    tasks = [asyncio.ensure_future(get_video(urls[i], i)) for i in range(len(urls))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))