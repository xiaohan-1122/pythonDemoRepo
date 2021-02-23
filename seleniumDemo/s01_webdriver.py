# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: s01_webdriver.py
# @Author: xiaohanzhang
# @Date: 2021/2/19

from selenium import webdriver
import time

"""
自动化测试
概念：让程序或工具代替人为对应用程序进行验证的过程
误区：1.一定比手工厉害 2.能发现更多bug 3.完全替代手工测试 4.所有功能都能自动化
适合自动化的项目：1.项目周期长 2.需求变动不频繁 3.需要回归测试
优点：1.提高效率 2.减少人为错误 3.可重复运行
缺点：
"""


def main():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    time.sleep(2)

    input_text = driver.find_element_by_id('kw')
    search_btn = driver.find_element_by_id('su')
    input_text.send_keys('哈尔滨')
    search_btn.click()

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    main()
