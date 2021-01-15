# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: requests14_线程池.py
# @Author: xiaohanzhang
# @Date: 2021/1/15
import random
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

# 原则：线程池处理额的是阻塞且耗时的操作


def make_thread_pool(num, urls):
    with ThreadPoolExecutor(max_workers=num) as t:  # 创建一个最大容纳数量为5的线程池
        tasks = []
        for i in range(num):
            # 通过submit提交执行的函数到线程池中
            t.submit(get_video, urls[i])


def save_video(video_url, id):
    response = requests.get(video_url)
    with open('./' + id + '.mp4', 'wb') as f:
        f.write(response.content)


def handle_video_url(video_url, video_id):
    """ 请求到的url需要处理一下才可以播放 """
    # 'https://video.pearvideo.com/mp4/adshort/20210114/1610606530104-15574909_adpkg-ad_hd.mp4' 将1610606530104替换为id,拼接cont-,'https://video.pearvideo.com/mp4/adshort/20210114/cont-1716345-15574909_adpkg - ad_hd.mp4
    str = video_url.split('/')[-1]
    str = str.split('-')[0]
    url = video_url.replace(str, 'cont-' + video_id)
    # print(url)
    return url


def get_video(detail_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Referer': detail_url,
    }

    url = 'https://www.pearvideo.com/videoStatus.jsp'
    mrd = random.random()
    contId = detail_url.split('_')[1]
    # print(contId)
    params = {
        'contId': contId,
        'mrd': mrd
    }
    print(f'正在下载{contId}.....')
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            video_url = data.get('videoInfo').get('videos').get('srcUrl')
            video_url = handle_video_url(video_url, contId)
            save_video(video_url, contId)
            print(f'{contId}下载完成。。')
            # return video_url
        else:
            print(f'{contId}下载失败！！！')
    except Exception as error:
        print(f'{contId}下载失败, {error}')


def get_detail_url():
    detail_urls = []
    # 解析获得视频详情页url和视频名称
    classification_url = 'https://www.pearvideo.com/category_8'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    try:
        response = requests.get(classification_url, headers=headers)
        if response.status_code == 200:
            tree = etree.HTML(response.text)
            video_detail_urls = tree.xpath('//li[@class="categoryem"]//a[@class="vervideo-lilink actplay"]/@href')
            for video_detail_url in video_detail_urls:
                video_detail_url = 'https://www.pearvideo.com/' + video_detail_url
                detail_urls.append(video_detail_url)
            return detail_urls
        else:
            print(f"获取视频详情页失败。。。。{response.text}")
    except Exception as error:
        print(f'获取视频详情页失败,{error}')


def main():
    video_urls = []
    # 获取视频详情页地址
    urls = get_detail_url()
    # print(urls)
    # 获取视频地址
    # for url in urls:
    #     get_video_url(url)

    make_thread_pool(len(urls), urls)


if __name__ == '__main__':
    main()