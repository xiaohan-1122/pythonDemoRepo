#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: requestsDemo
# @File: crawler04_药监局.py
# @Author: xiaohanzhang
# @Date: 2020/12/8

import requests
import json

# 药监局网址
# http://scxk.nmpa.gov.cn:81/xk/


def get_ids():
    id_list = []
    list_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    page = 1
    while True:
        data = {
            'on': 'true',
            'page': page,
            'pageSize': 15,
            'conditionType': 1
        }
        response = requests.post(list_url, headers=headers, data=data)
        if response.status_code == 200:
            # print(response.json())
            list = response.json()['list']
            for item in list:
                id_list.append(item['ID'])
        else:
            print(f'第{page}页请求失败')
        page += 1
        if page > 3:
            return id_list


def main():
    all_details = []
    ids = get_ids()
    # 公司详情url
    detail_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    for id in ids:
        data = {
            'id': id
        }
        # 获取公司详情
        response = requests.post(detail_url, headers=headers, data=data)
        if response.status_code == 200:
            # print(response.json())
            all_details.append(response.json())

    print(len(all_details))
    with open('./yaojianju.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(all_details, ensure_ascii=False))


if __name__ == '__main__':
    main()
