#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: requestsDemo
# @File: requests11_xpath爬取城市名称.py
# @Author: xiaohanzhang
# @Date: 2020/12/28

import requests
from lxml import etree

def main():
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    response = requests.get(url, headers)
    if response.status_code == 200:
        tree = etree.HTML(response.text)
        names = tree.xpath('//div[@class="bottom"]/ul[@class="unstyled"]//li/a/text()')
        print(names)
    else:
        print('请求失败')


if __name__ == '__main__':
    main()