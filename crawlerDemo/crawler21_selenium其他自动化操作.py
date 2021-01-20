# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: crawler21_selenium其他自动化操作.py
# @Author: xiaohanzhang
# @Date: 2021/1/20
""" 京东搜索某个商品 """
from selenium import webdriver
import time

if __name__ == '__main__':
    brower = webdriver.Chrome(executable_path='./chromedriver.exe')
    brower.get('https://www.taobao.com/')

    # 向下滚动1000像素
    # brower.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    brower.execute_script('window.scrollTo(0, 1000)')
    time.sleep(1)

    # 标签定位
    search_input = brower.find_element_by_id('q')
    # 输入要搜索的商品
    search_input.send_keys('switch')
    time.sleep(1)

    button_search = brower.find_element_by_class_name('btn-search')
    # 点击搜索按钮
    button_search.click()
    time.sleep(1)

    brower.get('https://www.baidu.com')
    time.sleep(1)
    # 后退
    brower.back()
    time.sleep(1)
    # 前进
    brower.forward()
    time.sleep(1)

    brower.quit()