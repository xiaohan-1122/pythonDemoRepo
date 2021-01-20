# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: crawler23_selenium模拟登录.py
# @Author: xiaohanzhang
# @Date: 2021/1/20
""" qq空间登录 """
from selenium import webdriver
import time


if __name__ == '__main__':
    brower = webdriver.Chrome(executable_path='./chromedriver.exe')
    brower.get('https://qzone.qq.com')
    # 切换到登录iframe中
    brower.switch_to.frame('login_frame')
    # 账号密码登录
    switch_login = brower.find_element_by_id('switcher_plogin')
    time.sleep(1)
    switch_login.click()

    time.sleep(2)

    username_input = brower.find_element_by_id('u')
    username_input.send_keys('')
    password_input = brower.find_element_by_id('p')
    password_input.send_keys('')

    time.sleep(1)
    brower.find_element_by_id('login_button').click()

    time.sleep(3)
    brower.quit()