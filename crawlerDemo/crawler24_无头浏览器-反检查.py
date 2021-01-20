# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: crawler24_无头浏览器-反检查.py
# @Author: xiaohanzhang
# @Date: 2021/1/20
""" 无可视化界面 """
from selenium import webdriver
from selenium.webdriver import ChromeOptions


if __name__ == '__main__':
    # 不显示浏览器界面
    options = ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    # selenium规避被网站识别的风险
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    brower = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
    brower.get('https://www.baidu.com')
    print(brower.page_source)
    brower.quit()
