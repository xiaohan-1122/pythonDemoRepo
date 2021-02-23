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
link_text   超链接文本
partial_link_text   超链接文本
xpath   元素路径
css     选择器
"""


def find_by_id(driver):
    """ 通过id元素 """
    # 找到搜索输入框
    search_text = driver.find_element_by_id('kw')
    # 输入搜索内容
    search_text.send_keys('北京')
    # 找到搜索按钮
    search_btn = driver.find_element_by_id('su')
    # 点击按钮
    search_btn.click()


def find_by_name(driver):
    """ 通过name属性定位元素 """
    # 找到搜索输入框
    search_text = driver.find_element_by_name('wd')
    search_text.send_keys('上海')


def find_by_class(driver):
    """ 通过class定位元素 """
    # 所有class为s_ipt的元素
    elements = driver.find_elements_by_class_name('s_ipt')
    search_text = elements[0]

    # 第一个class='s_ipt'的元素
    # search_text = driver.find_element_by_class_name('s_ipt')
    search_text.send_keys('杭州')


def find_by_tag(driver):
    """ 通过tag定位元素 """
    inputs = driver.find_elements_by_tag_name('input')
    print(inputs)
    # 如果页面中存在多个相同标签，默认返回第一个标签
    input = driver.find_element_by_tag_name('input')
    input.send_keys('重庆')


def main():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')

    # find_by_id(driver)
    # find_by_name(driver)
    # find_by_class(driver)
    find_by_tag(driver)

    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()
