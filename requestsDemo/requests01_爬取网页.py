#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: requestsDemo
# @File: requests01_爬取网页.py
# @Author: xiaohanzhang
# @Data: 2020/12/3

import requests

if __name__ == '__main__':
    url = "https://www.sogou.com/web"
    kw = input("请输入搜索内容:")
    params = {
        'query': kw
    }
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        # print(response.text)
        page_text = response.text
        file_name = kw + '.html'
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(page_text)
        print('保存成功')
    else:
        print("请求失败")