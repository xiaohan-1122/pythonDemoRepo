#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: requestsDemo
# @File: crawler09_xpath解析基础.py
# @Author: xiaohanzhang
# @Date: 2020/12/24
import requests
from lxml import etree

def main():
    tree = etree.parse('test.html')
    # 解析title标签中的信息
    tag_list = tree.xpath('/html/head/title')
    print(tag_list)
    # / 表示直接子元素
    li_list = tree.xpath('/html/body/div/ul/li')
    # 中间的 // 表示子元素
    li_list = tree.xpath('/html//li')
    # 以//开头表示从任意位置定位元素
    li_list = tree.xpath('//li')
    print(len(li_list))

#     属性定位
    res_list = tree.xpath('//div[@class="song"]')
    print(res_list)

    res_list = tree.xpath('//div[@class="song"]/a')
    print(res_list)

#     索引定位,索引从1开始
    p = tree.xpath('//div/p[3]')       # 获取第三个p标签
    print(p)

#     获取文本
    text = tree.xpath('//li[5]/a/text()')[0]    # /text()返回标签中的文本，标签本身的文本，是一个列表
    text = tree.xpath('//li[7]//text()')        # //text()返回标签中的文本，包含子标签中的文本，是一个列表
    print(text)
#     获取属性  /@属性名
    img_src = tree.xpath('//div[@class="song"]/img/@src')[0]
    print(img_src)


if __name__ == '__main__':
    main()
