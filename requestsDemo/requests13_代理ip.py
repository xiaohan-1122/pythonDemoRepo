# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: requests13_代理ip.py
# @Author: xiaohanzhang
# @Date: 2021/1/8

# http://www.xiladaili.com/
# 代理ip匿名度:
# 透明: 服务器知道该次请求使用了代理，也知道请求对应的真实ip
# 匿名: 知道使用了代理，不知道真实ip
# 高匿: 不知道使用了代理，更不知道真实ip

import requests
import re


def main():
    url = 'https://www.baidu.com/s?wd=ip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    # 使用代理
    response = requests.get(url, headers=headers, proxies={"https": '219.131.240.38:9797'})
    page_text = response.text
    ip = re.findall(r'本机IP:&nbsp;(.*)</span>', page_text)[0]
    print(ip)


if __name__ == '__main__':
    main()