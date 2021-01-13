# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: requests15_异步爬虫应用.py
# @Author: xiaohanzhang
# @Date: 2021/1/11
""" 爬取梨视频 """
import requests
from lxml import etree
# 原则：线程池处理额的是阻塞且耗时的操作


def main():
    # 解析获得视频详情页url和视频名称
    classification_url = 'https://www.pearvideo.com/category_8'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response = requests.get(classification_url, headers=headers)
    tree = etree.HTML(response.text)
    video_detail_urls = tree.xpath('//li[@class="categoryem"]//a[@class="vervideo-lilink actplay"]/@href')
    for video_detail_url in video_detail_urls:
        video_detail_url = 'https://www.pearvideo.com/' + video_detail_url
        print(video_detail_url)


if __name__ == '__main__':
    main()