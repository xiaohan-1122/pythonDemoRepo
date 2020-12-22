#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: requestsDemo
# @File: request07_bs4解析基础.py
# @Author: xiaohanzhang
# @Date: 2020/12/22

from bs4 import BeautifulSoup

from bs4 import BeautifulSoup
import requests

# 需安装lxml
def test():
    response = requests.get('https://www.baidu.com')
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)


def main():
    # test()
    with open('./test.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')
        print(soup)


if __name__ == '__main__':
    main()