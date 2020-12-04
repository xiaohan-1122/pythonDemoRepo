# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: main.py
# @Author: xiaohanzhang
# @Date: 2020/12/4

import re

import chardet
import requests
from pprint import pprint

# 爬取B站弹幕数据的API：https://api.bilibili.com/x/v1/dm/list.so?oid=XXX
# 获取oid的接口：https://api.bilibili.com/x/player/pagelist?bvid=BV1PK4y1b7dt&jsonp=jsonp
# bvid在视频原始网页地址中获取，如：https://www.bilibili.com/video/BV1PK4y1b7dt?t=1


def get_bvid(url):
    # 分割字符串
    bvid_str = re.split(r'/', url)[-1]
    bvid = re.split(r'\?', bvid_str)[0]
    return bvid if bvid is not None else ''


def get_cid(bvid):
    """ 根据bvid请求得到cid """
    cid = ''
    url = f'https://api.bilibili.com/x/player/pagelist'
    params = {
        'bvid': bvid,
        'jsonp': 'jsonp'
    }
    responts = requests.get(url, params=params)
    if responts.status_code == 200:
        # print(responts.json())
        data = responts.json()['data']
        if len(data) >= 1:
            cid = data[0]['cid']
    else:
        print("获取cid失败")

    return cid


# bilibili的网页现在已经换了，list.so接口找不到了，但是记住这个接口就行了。
def get_data(cid):
    """ 获取弹幕 """
    final_url = 'https://api.bilibili.com/x/v1/dm/list.so'
    params = {
        'oid': cid
    }
    final_res = requests.get(final_url, params=params)
    # 检测编码格式
    # print(chardet.detect(final_res.content)['encoding'])    # utf-8
    final_res.encoding = chardet.detect(final_res.content)['encoding']
    # final_res.encoding = 'utf-8'
    final_res = final_res.text
    # pprint()模块打印出来的数据结构更加完整，每行为一个数据结构，更加方便阅读打印输出结果
    # pprint(final_res)

    # 以列表的形式返回能匹配的子串
    # data = re.findall(r'<d.*?>(.*?)</d>', final_res)
    # re.compile() 是用来优化正则的，它将正则表达式转化为对象
    pattern = re.compile('<d.*?>(.*?)</d>')
    data = pattern.findall(final_res)
    # print(data)
    return data


def save_to_file(data):
    """ 保存弹幕列表 """
    with open("dan_mu.txt", "w", encoding="utf-8") as f:
        for i in data:
            f.write(i)
            f.write("\n")


def main():
    # 要爬取字幕的视频页面
    video_url = "https://www.bilibili.com/video/BV1tD4y1X7Ru?t=345"
    bvid = get_bvid(video_url)
    cid = get_cid(bvid)
    dm_list = get_data(cid)
    # print(dm_list)
    save_to_file(dm_list)


if __name__ == '__main__':
    main()
