#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: requestsDemo
# @File: requests05_爬取图片.py
# @Author: xiaohanzhang
# @Date: 2020/12/14

import requests


def main():
    url = 'https://pic.qiushibaike.com/system/pictures/12387/123875165/medium/Y12P1GEMKDR8IOAT.jpg'
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        img_data = response.content
        # 二进制方式写入文件
        with open('./qiutu.jpg', 'wb') as f:
            f.write(img_data)


if __name__ == '__main__':
    main()
