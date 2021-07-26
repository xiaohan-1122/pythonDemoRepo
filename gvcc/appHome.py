# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: appHome.py
# @Author: xiaohanzhang
# @Date: 2021/4/25
import requests
import time
import hashlib

domain = '192.168.1.37:8093'
protocol = 'http'

# def md5_test(apiKey, time, userId, access_Token):
def md5_test(str):
    m = hashlib.md5()
    m.update(str.encode(encoding='utf-8'))
    # print(m.hexdigest())
    return m.hexdigest()


def meeting_list(token, secret):
    url = protocol + '://' + domain + '/api/app/gvcc/meeting-list'
    now_time = str(int(time.time() * 1000))
    print(url)
    print(now_time)
    params = {
        'access_token': token,
        'lang': 'zh',
        'secret': secret,
        'time': now_time
    }
    response = requests.get(url, params=params)
    print(response.json())


def main():
    meeting_list(f"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", '181180fa563bebf367b51c58f77235d5')


if __name__ == '__main__':
    main()