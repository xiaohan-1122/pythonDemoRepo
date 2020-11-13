#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: downloadDemo
# @File: download_img.py
# @Author: xiaohanzhang
# @Data: 2020/11/13
# 爬虫--王者荣耀皮肤图片
import requests
import json

# 获取数据
res = requests.get('https://pvp.qq.com/web201605/js/herolist.json')
# print(res.json())
# hero_list = res.json()
hero_list = json.loads(res.content)
# print(hero_list)

img_count = 0
# for i in range(len(hero_list))：
for dic in hero_list:
    # print(dic)
    ename = dic.get('ename')
    cname = dic.get('cname')
    skin_name = dic.get('skin_name')
    if skin_name is not None:
        skin_names = dic.get('skin_name').split('|')  # 皮肤名字
    else:
        skin_names = []
    # print(skin_names)
    # 计算每个英雄有多少个皮肤
    skin_count = len(skin_names)
    for i in range(len(skin_names)):
        img_count += 1
        img_url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i + 1}.jpg'
        # print(img_url)
        # img_list.append(img_url)
        response = requests.get(img_url)
        if response.status_code == 200:
            # 获取图片二进制数据
            img_data = response.content

            # 存储图片数据
            with open(cname + '-' + str(i) + '.jpg', 'wb') as f:
                f.write(img_data)
            print(f'正在下载第{img_count}张图片...')
        else:
            print('下载失败')
