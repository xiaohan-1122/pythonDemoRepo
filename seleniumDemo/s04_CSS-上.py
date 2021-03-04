# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: s04_CSS-上.py
# @Author: xiaohanzhang
# @Date: 2021/3/3
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

""" 
css选择器查找效率比xpath高，有时候xpath写法也会比css简单
查找元素比较简单，用css，查找元素复杂，用xpath
 """
"""验证选择器是否正确，可以直接在Chrome中搜索该选择器，查看是否定位到要找的元素 cmd + f"""


def find_by_css_id(wd):
    """id选择器"""
    element = wd.find_element_by_css_selector('#su')
    print(element.get_attribute('value'))


def find_by_css_class(wd):
    """class选择器"""
    elements = wd.find_elements_by_css_selector('.title-content-title')
    for element in elements:
        print(element.text)


def find_by_css_tag(wd):
    """标签选择器"""
    elements = wd.find_elements_by_css_selector('a')
    for e in elements:
        print(e.text)


def find_by_css_attribute(wd):
    """通过属性定位元素"""
    element = wd.find_element_by_css_selector('[name="tj_settingicon"]')
    print(element.get_attribute('href'))


def find_by_css_sequence(wd):
    """子元素选择器 后代元素选择器"""
    # 子元素
    element = wd.find_element_by_css_selector('ul>[data-index="0"]>.title-content')
    print(element.get_attribute('href'))

    # 后代元素
    element = wd.find_element_by_css_selector('ul>[data-index="0"] .title-content-title')
    print(element.text)


def find_by_css_other(wd):
    """其它常用方法"""
    # 属性以xxxx开头的元素
    elements = wd.find_elements_by_css_selector('span[class^="title"]')

    # 属性以xxxx结尾
    elements = wd.find_elements_by_css_selector('span[class$="title"]')

    # 属性包含xxxx
    elements = wd.find_elements_by_css_selector('span[class*="content"]')

    for element in elements:
        print(element.text)


def main():
    if __name__ == '__main__':
        wd = webdriver.Chrome()
        wd.get('https://www.baidu.com')
        wd.implicitly_wait(5)

        # find_by_css_id(wd)
        # find_by_css_class(wd)
        # find_by_css_tag(wd)
        # find_by_css_attribute(wd)
        # find_by_css_sequence(wd)
        find_by_css_other(wd)

        wd.quit()


if __name__ == '__main__':
    main()