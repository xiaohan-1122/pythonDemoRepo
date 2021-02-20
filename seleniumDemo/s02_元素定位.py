# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: s02_元素定位.py
# @Author: xiaohanzhang
# @Date: 2021/2/20

from selenium import webdriver
import time

"""
元素定位方式：
id
name属性
class_name 类名
tag_name 标签名
link_text
partial_link_text
"""


def find_by_id(driver):
    """ 通过id元素 """


def main():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')

    find_by_id(driver)

    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()
