# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: crawler20_selenium初试.py
# @Author: xiaohanzhang
# @Date: 2021/1/19

from selenium import webdriver
from lxml import etree
import time

if __name__ == '__main__':
    # executable_path 驱动路径
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    # 配置环境变量后，可以省略驱动路径
    # driver = webdriver.Chrome()
    # driver.get('https://www.baidu.com')
    driver.get('http://scxk.nmpa.gov.cn:81/xk/')
    # 等待数据加载
    time.sleep(1)
    # 获取点前页面的页面源码数据
    tree = etree.HTML(driver.page_source)
    companies = tree.xpath('//ul[@id="gzlist"]/li/dl/@title')
    print(companies)

    driver.quit()