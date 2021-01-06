#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: requestsDemo
# @File: requests02_百度翻译.py
# @Author: xiaohanzhang
# @Date: 2020/12/5

# post请求
import requests
import json

def main():
    url = "https://fanyi.baidu.com/sug"
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15"
    }
    word = input('请输入：')
    data = {
        'kw': word
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print(response.json())
        dic_obj = response.json()
        # 写入json文件
        with open(f'./{word}.json', 'w', encoding='utf-8') as f:
            # json.dumps将一个Python数据结构转换为JSON
            # ensure_ascii=True：默认输出ASCLL码，如果把这个该成False,就可以输出中文
            f.write(json.dumps(dic_obj, ensure_ascii=False))
    else:
        print("请求失败")


if __name__ == '__main__':
    main()
