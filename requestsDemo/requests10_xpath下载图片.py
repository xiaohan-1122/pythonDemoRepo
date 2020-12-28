#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: requestsDemo
# @File: requests10_xpath下载图片.py
# @Author: xiaohanzhang
# @Date: 2020/12/26

import requests
from lxml import etree
import os
from bs4 import BeautifulSoup

def save_img(data, name):
    if not os.path.exists('./images'):
        os.mkdir('./images')
    with open('./images/' + name + '.jpg', 'wb') as f:
        f.write(data)


def get_img(url, name):
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    response = requests.get(url, headers)
    if response.status_code == 200:
        save_img(response.content, name)
    else:
        print('图片请求失败')


def xpath_test(text):
    html_tree = etree.HTML(text)
    li_tags = html_tree.xpath('//div[@id="main"]/div[@class="slist"]//li')
    for li_tag in li_tags:
        img_url = 'http://pic.netbian.com' + li_tag.xpath('./a/img/@src')[0]
        # title = img_url.split('/')[-1]
        # 通用处理中文乱码解决方案
        title = title.encode('iso-8859-1').decode('gbk')
        print(f'url = {img_url}, title = {title}')
        get_img(img_url, title)


def bs4_test(text):
    soup = BeautifulSoup(text, 'lxml')
    img_tags = soup.select('#main .slist img')
    for img_tag in img_tags:
        img_url = 'http://pic.netbian.com' + img_tag['src']
        # title = img_url.split('/')[-1]
        title = img_tag['alt']
        # 通用处理中文乱码解决方案
        title = title.encode('iso-8859-1').decode('gbk')
        print(f'url = {img_url}, title = {title}')
        get_img(img_url, title)


def main():
    url = 'http://pic.netbian.com/4kmeishi/'
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    response = requests.get(url, headers)
    if response.status_code == 200:
        # 可以对response重新编码
        # response.encoding = 'utf-8'

        # xpath_test(response.text)
        bs4_test(response.text)
    else:
        print('请求失败')


if __name__ == '__main__':
    main()