#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: requestsDemo
# @File: requests03_豆瓣电影.py
# @Author: xiaohanzhang
# @Date: 2020/12/6

import requests
import json

def main():
    url = 'https://movie.douban.com/j/chart/top_list'
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

    }
    # word = input('请输入：')
    params = {
        'type': 17,
        'interval_id': '100:90',
        'action': '',
        'start': 0,
        'limit': 20
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        # print(response.json())
        list_data = response.json()
        with open('./douban.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(list_data, ensure_ascii=False))
    else:
        print('请求失败')


if __name__ == '__main__':
    main()