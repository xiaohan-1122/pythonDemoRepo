# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: ciyuntu.py
# @Author: xiaohanzhang
# @Date: 2020/12/4

import jieba
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from imageio import imread

# 使用python实现一个文本的词频统计，并进行词云绘制。
# 1.使用jieba对文本进行分词
# 2.比对stoplist.txt停用词文件，删除停用词，无关符号。
# 3.使用collections.Counter（）函数对词频进行统计，输出统计结果。
# 4.使用wordcloud 绘制词云，保存图片。


def get_word_list():
    with open("dan_mu.txt", encoding="utf-8") as f:
        word = f.read()
    word_list = word.split()

    # 使用lcut()方法进行分词
    data_cut = [jieba.lcut(x) for x in word_list]
    # data_cut
    print(data_cut)

    # 3 读取停用词
    with open(r"cn_stopwords.txt", encoding="utf-8") as f:
        stop = f.read()
    stop = stop.split()
    stop = [" ", "道", "说道", "说"] + stop
    # 4 去掉停用词之后的最终词
    s_data_cut = pd.Series(data_cut)
    all_words_after = s_data_cut.apply(lambda x: [i for i in x if i not in stop])
    # 5 词频统计
    all_words = []
    for i in all_words_after:
        all_words.extend(i)
    word_count = pd.Series(all_words).value_counts()

    # 6 词云图的绘制
    # 1）读取背景图片
    back_picture = imread(r"G:\6Tipdm\wordcloud\jay1.jpg")

    # 2）设置词云参数
    wc = WordCloud(font_path="G:\\6Tipdm\\wordcloud\\simhei.ttf",
                   background_color="white",
                   max_words=2000,
                   mask=back_picture,
                   max_font_size=200,
                   random_state=42
                   )
    wc2 = wc.fit_words(word_count)

    # 3）绘制词云图
    plt.figure(figsize=(16, 8))
    plt.imshow(wc2)
    plt.axis("off")
    plt.show()
    wc.to_file("ciyun.png")


def main():
    get_word_list()


if __name__ == '__main__':
    main()
