# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: crawler08_bs4使用.py
# @Author: xiaohanzhang
# @Date: 2020/12/24

from bs4 import BeautifulSoup
import requests


# 爬取小说
def get_chapter_detail(url):
    """ 获取章节内容 """
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    response = requests.get(url, headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        h1_tag = soup.select('.bookmark-list h1')[0]
        title = h1_tag.text
        detail_text = soup.find('div', class_='chapter_content').text
        with open('./三国演义.txt', 'a', encoding='utf-8') as f:
            f.write(title)
            f.write(detail_text + '\n')


def get_book_chapter_urls(url):
    """ 获取书籍章节列表 """
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    response = requests.get(url, headers)
    chapter_urls = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        title_a_list = soup.select('.book-mulu a')
        for a in title_a_list:
            chapter_urls.append('http://www.shicimingju.com' + a['href'])

        return chapter_urls


def main():
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    chapter_urls = get_book_chapter_urls(url)
    for chapter_url in chapter_urls:
        get_chapter_detail(chapter_url)


if __name__ == '__main__':
    main()
