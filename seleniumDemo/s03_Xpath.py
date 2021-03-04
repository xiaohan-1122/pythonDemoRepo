# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: s03_Xpath.py
# @Author: xiaohanzhang
# @Date: 2021/3/1

from selenium import webdriver
import time

'''
知道元素名 尽量不要用 *
尽量使用相对路径，不要使用绝对路径
'''


def find_by_absolute_path(wd):
    """ 绝对路径定位元素 """
    elements = wd.find_elements_by_xpath('/html/body/div/div[1]/div[3]/a')
    for element in elements:
        print(element.text)

    # 获取文字 “百度热榜”
    e = wd.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/a/div')
    print(e.text)


def find_relative_path_test(wd):
    """相对路径定位元素"""
    # 直接子节点
    titles = wd.find_elements_by_xpath('//div/ul/li/a/span[2]')
    for title in titles:
        print(title.text)
    print('*' * 30)

    # 子节点
    titles = wd.find_elements_by_xpath('.//div//li//span[2]')
    for title in titles:
        print(title.text)
    # 通配符 ul中所有直接子节点
    eles = wd.find_elements_by_xpath('//ul/*')
    print(len(eles))


def find_by_attribute(wd):
    """按属性定位"""
    btn = wd.find_element_by_xpath('//input[@value="百度一下"]')
    print('value:' + btn.get_attribute('value'))
    btn = wd.find_element_by_xpath('//*[@id="su"]')
    print('id:' + btn.get_attribute('value'))
    # class不能只写一个，要全写上
    btn = wd.find_element_by_xpath('//*[@class="bg s_btn"]')
    print('class:' + btn.get_attribute('value'))
    elements = wd.find_elements_by_xpath('//li[@class="hotsearch-item even"]')
    print(len(elements))

    # 有value属性的元素
    elements = wd.find_elements_by_xpath('//*[@value]')
    print(len(elements))


def find_by_sequence(wd):
    """按次序定位"""
    # ul中第一个li标签中的第二个span
    span = wd.find_element_by_xpath('//ul/li[1]//span[2]')
    print(span.text)
    # 最后一个span
    last_span = wd.find_element_by_xpath('//ul/li[1]//span[last()]')
    print(last_span)
    # 倒数第二个span
    span = wd.find_element_by_xpath('//ul/li[1]//span[last() - 1]')
    print(span.text)
    # 前两个
    span_list = wd.find_elements_by_xpath('//ul/li[1]//span[position()<=2]')
    # 选取class属性为hotsearch-item odd的第一个li标签中的前两个span
    # e_list = wd.find_elements_by_xpath('//*[@class="hotsearch-item odd"][1]//span[position()<=2]')


def find_by_logical(wd):
    """路径与逻辑结合"""
    # ul中第一个li标签中的第二个span
    span = wd.find_element_by_xpath('//li[@class="hotsearch-item odd" and @data-index="0"]//span[2]')
    print(span.text)
    li_list = wd.find_elements_by_xpath('//li[@class="hotsearch-item odd" or @class="hotsearch-item even"]')
    print(len(li_list))


def find_by_other(wd):
    """其它常用方法"""
    # 文本内容是xxxx的元素 //*[text() = "xxxx"]
    element = wd.find_element_by_xpath('//*[text() = "百度热榜"]')
    print(element.text)

    # 属性中含有xxxx的元素 //*[contains(@attribute, "xxxx")]  移动端自动化测试用的比较多
    element = wd.find_element_by_xpath('//*[contains(@href, "login")]')
    print(element.get_attribute('href'))

    # 属性以xxxx开头的元素
    element = wd.find_element_by_xpath('//*[starts-with(@href, "https://passport.baidu.com")]')
    print(element.get_attribute('href'))


def main():
    wd = webdriver.Chrome()
    wd.get('https://www.baidu.com')
    wd.implicitly_wait(5)

    # find_by_absolute_path(wd)
    # find_relative_path_test(wd)
    find_by_attribute(wd)
    # find_by_sequence(wd)
    # find_by_logical(wd)
    # find_by_other(wd)

    time.sleep(2)
    wd.quit()


if __name__ == '__main__':
    main()