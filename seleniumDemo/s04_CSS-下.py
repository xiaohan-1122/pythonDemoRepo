# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: s04_CSS-下.py
# @Author: xiaohanzhang
# @Date: 2021/3/3
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

"""选择器可以组合使用"""


def css_test(wd):
    # 同时满足标签和class，即class为title-content-title的span
    elements = wd.find_elements_by_css_selector('span.title-content-title')
    # , 表示或  选择器中不能加括号  紧挨着写是与
    elements = wd.find_elements_by_css_selector('.s-hotsearch-content > [data-index="0"] , .s-hotsearch-content > .even')
    print(len(elements))
    for e in elements:
        print(e.text)


def css_nth(wd):
    """按次序选择子元素"""
    # li标签的第二个
    element = wd.find_element_by_css_selector('.s-hotsearch-content>li:nth-child(2)')
    # li标签类型的第二个
    element = wd.find_element_by_css_selector('.s-hotsearch-content li:nth-of-type(2)')
    # print(element.text)

    # 偶数节点
    elements = wd.find_elements_by_css_selector('.s-hotsearch-content li:nth-child(even)')
    # 奇数节点
    elements = wd.find_elements_by_css_selector('.s-hotsearch-content li:nth-of-type(odd)')
    for e in elements:
        print(e.text)


def css_test3(wd):
    # 兄弟节点 .top-0后面紧跟的span
    element = wd.find_element_by_css_selector('.top-0 + span')
    print(element.text)

    # 兄弟节点 .top-0后面所有的span
    elements = wd.find_elements_by_css_selector('.top-0 ~ span')
    print(len(elements))


def main():
    if __name__ == '__main__':
        wd = webdriver.Chrome()
        wd.get('https://www.baidu.com')
        wd.implicitly_wait(5)

        # css_test(wd)
        # css_nth(wd)
        css_test3(wd)

        wd.quit()


if __name__ == '__main__':
    main()