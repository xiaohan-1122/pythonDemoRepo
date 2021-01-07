# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: requests11_图片验证码识别.py
# @Author: xiaohanzhang
# @Date: 2021/1/6

# 使用百度文字识别 识别清晰验证码
import requests
import base64


def get_baidu_token():
    # grant_type： 必须参数，固定为client_credentials；
    # client_id： 必须参数，应用的API Key；
    # client_secret： 必须参数，应用的Secret Key；
    baidu_url = 'https://aip.baidubce.com/oauth/2.0/token'
    params = {
        'grant_type': 'client_credentials',
        'client_id': 't6z8GKlfi7RRmikGbGz8LKOo',
        'client_secret': 'TqVTlF7YnjhFlbEGx9ZZGPmCDy9FF89F'
    }
    response = requests.get(baidu_url, params=params)
    # access_token： 要获取的Access Token；
    # expires_in： Access Token的有效期(秒为单位，一般为1个月)；

    refresh_token = response.json()['access_token']
    return refresh_token


def main():
    refresh_token = get_baidu_token()
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic' + '?access_token=' + refresh_token
    print(url)

    # 二进制方式打开图片文件
    with open('./20210106141404.png', 'rb') as f:
        img = base64.b64encode(f.read())
        headers = {
            'content-type': 'application/x-www-form-urlencoded'
        }
        data = {
            'image': img
        }
        response = requests.post(url, data=data, headers=headers)
        print(response.json())
        words_list = response.json()['words_result']
        words = words_list[0]['words'] if len(words_list) > 0 else ''
        print(words)


if __name__ == '__main__':
    main()