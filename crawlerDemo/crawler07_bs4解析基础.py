#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: crawlerDemo
# @File: crawler07_bs4解析基础.py
# @Author: xiaohanzhang
# @Date: 2020/12/22

from bs4 import BeautifulSoup
import requests


# 需安装lxml
def test():
    response = requests.get('https://www.baidu.com')
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)

# 获取标签：
# soup.tagName 根据标签名称获取对应的第一个标签
# soup.find('tagName')  根据标签名称获取对应的第一个标签
# 属性定位 soup.find('tagName', class_/id/attr='属性值') 返回符合条件的第一个标签
# soup.find_all('tagName')  返回符合条件的所有内容
# soup.find_all('tagName', class_/id/attr='属性值')
# soup.select('选择器') 返回符合条件的所有内容

# 拿到标签后，获取标签中的内容
# .text/ .string/ .get_text()
# .text / .get_text() 可以获取标签中的所有内容，包括子标签
# .string 只能获取标签中的直系文本，不能获取子标签内容

# 获取标签中属性值 [属性名称]


def main():
    # test()
    with open('./test.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')
        # print(soup)
        # soup.tagName 根据标签名称获取html内容
        print(soup.a)   # 返回页面中第一次出现的a标签
        print(soup.div)
        # soup.find('tagName') 同soup.tagName
        print(soup.find('a'))   # 返回页面中第一次出现的a标签
        # 根据属性获取标签(返回符合条件的第一个标签)
        print(soup.find('a', class_='test-a'))
        print(soup.find_all('a', class_='test-a'))  # 返回列表
        print(soup.find_all('a'))
        # select('选择器') 返回列表
        print(soup.select('.tang'))
        print(soup.select('.tang li a'))

        # 获取标签中的内容
        print(soup.find('a').text)
        print(soup.find('a').string)
        print(soup.find('a').get_text())

        print(soup.find('a')['href'])


if __name__ == '__main__':
    main()