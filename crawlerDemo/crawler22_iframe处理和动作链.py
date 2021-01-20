# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: crawler22_iframe处理和动作链.py
# @Author: xiaohanzhang
# @Date: 2021/1/20

from selenium import webdriver
# 导入动作链对应的类
from selenium.webdriver import ActionChains
import time

if __name__ == '__main__':
    brower = webdriver.Chrome(executable_path='./chromedriver.exe')
    brower.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

    # 如果定位标签是存在于iframe标签中的，必须通过如下操作进行标签定位
    brower.switch_to.frame('iframeResult')
    div = brower.find_element_by_id('draggable')
    time.sleep(2)
    # 动作链
    action = ActionChains(brower)
    # 点击并长按指定的标签
    action.click_and_hold(div)
    for i in range(5):
        # .perform()动作链立即执行
        action.move_by_offset(17, 0).perform()
        time.sleep(0.3)

    # 释放动作链
    action.release()
    time.sleep(2)
    brower.quit()