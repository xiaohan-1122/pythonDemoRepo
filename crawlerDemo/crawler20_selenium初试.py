# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: crawler20_selenium初试.py
# @Author: xiaohanzhang
# @Date: 2021/1/19

from selenium import webdriver
import time


if __name__ == '__main__':
    # executable_path 驱动路径
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    # 配置环境变量后，可以省略驱动路径
    # driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    time.sleep(3)
    driver.quit()