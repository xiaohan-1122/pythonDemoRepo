#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: requestsDemo
# @File: requests06_正则解析案例.py
# @Author: xiaohanzhang
# @Date: 2020/12/15
import requests
import re
import os


def main():
    # 创建文件夹 保存图片
    if not os.path.exists('./qiutu'):
        os.mkdir('./qiutu')
    img_src_list = []
    # 爬取前3页
    for i in range(1, 4):
        url = f'https://www.qiushibaike.com/imgrank/page/{i}'
        headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        # 1.爬取糗事百科热图页面
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            page_text = response.text
            """
            <div class="thumb">
                <a href="/article/123881207" target="_blank">
                <img src="//pic.qiushibaike.com/system/pictures/12388/123881207/medium/TRXVUU1YOCGTQVPI.jpg" alt="糗事#123881207" class="illustration" width="100%" height="auto">
                </a>
                </div>
            """
            # 2.提取页面中的图片地址
            # .* 单个字符匹配任意次，即贪婪匹配。
            # .*? 满足条件的情况只匹配一次，即懒惰匹配
            ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
            # re.S 使 . 匹配包括换行在内的所有字符
            img_src_list.extend(re.findall(ex, page_text, re.S))
    # 3.爬取页面中的图片
    for img_src in img_src_list:
        response = requests.get('https:' + img_src, headers=headers)
        img_data = response.content
        img_name = img_src.split('/')[-1]
        with open('./qiutu/' + img_name, 'wb') as f:
            f.write(img_data)
            print(f'{img_name}下载成功！')


if __name__ == '__main__':
    main()
