# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: main.py
# @Author: xiaohanzhang
# @Date: 2021/1/7

import requests
import re
import time
import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud

g_is_login = False


def write_comments(path, comments):
    if comments is not None and len(comments) > 0:
        with open(path, 'a+', encoding='utf-8') as f:
            f.write('\n'.join(comments))
    else:
        print('评论为空!!!!')


def cut_word():
    with open('./source/comments.txt', 'r', encoding='utf-8') as f:
        comment_text = f.read()
        word_list = jieba.cut(comment_text, cut_all=True)
        words = ' '.join(word_list)
        # print(words)
        return words


def create_word_cloud(words):
    # 设置词云形状，若设置了词云的形状，生成的词云与图片保持一致，后面设置的宽度和高度将默认无效
    mask = np.array(Image.open("./source/pikaqiu.jpg"))
    with open(r"source/cn_stopwords.txt", encoding="utf-8") as f:
        stop_words = f.read()
    stop_words = stop_words.split()
    # 自定义词云
    wc = WordCloud(
        # 遮罩层,除白色背景外,其余图层全部绘制（之前设置的宽高无效）
        mask=mask,
        # 默认黑色背景,更改为白色
        background_color='#FFFFFF',
        # 若想生成中文字体,需添加中文字体路径
        font_path="./source/FZNiNSJW.TTF",
        stopwords=stop_words,
        max_words=2000,
        max_font_size=150,
    )
    wc.generate(cut_word())
    # 返回对象
    image_produce = wc.to_image()
    # 显示图像
    image_produce.show()
    wc.to_file("./source/ciyun.png")


def login(username, password, session):
    url = 'https://accounts.douban.com/j/mobile/login/basic'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
    }
    data = {
        'remember': 'false',
        'name': username,
        'password': password
    }
    response = session.post(url, headers=headers, data=data)
    if response.status_code == 200:
        if response.json()['status'] == 'success':
            global g_is_login
            g_is_login = True
        else:
            print(response.json())
    else:
        print(f'登录失败: {response.text}')


def get_comment(session, start=0):
    limit = 20
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }

    params = {
        'percent_type': '',
        'start': start,
        'limit': limit,
        'status': 'P',
        'sort': 'new_score',
        'comments_only': 1
    }
    url = 'https://movie.douban.com/subject/24733428/comments'
    try:
        response = session.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f'获取评论失败,start：{start}')
            return
        # print(response.json())
    except:
        print(f'获取评论失败，start:{start}')
    content = response.json()['html']
    comments = re.findall('<span class="short">(.*)</span>', content)

    print(comments)
    if len(comments) > 0:
        write_comments('./source/comments.txt', comments)
        start += limit
        time.sleep(3)
        get_comment(session, start)
    else:
        print('爬取完毕！！！')
        return


def main():

    # requests的session对象每次请求会自动带上Cookie,requests.Session对象只是一个用于保存Cookie的对象而已
    session = requests.Session()
    login('18205322783', 'A262408*', session)
    if g_is_login:
        get_comment(session)
    create_word_cloud(cut_word())


if __name__ == '__main__':
    main()
