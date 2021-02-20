# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: s01_webdriver.py
# @Author: xiaohanzhang
# @Date: 2021/2/19

from selenium import webdriver
import time


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
