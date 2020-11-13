#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: downloadDemo
# @File: download_video.py
# @Author: xiaohanzhang
# @Data: 2020/11/13

# 视频解析网站：http://jx.618g.com/?url=

import requests
import re
import subprocess

def get_video_url(path):
    web_path = "http://jx.618g.com/?url=" + path
    response = requests.get(web_path)
    if response.status_code == 200:
        # print(respones.text)
        result = re.search(r"http.*m3u8", response.text)
        video_url = result.group()
        return video_url
    else:
        print("请求出错")


def download_video(url, name):
    # command = "D:/ffmpeg/ffmpeg-4.3-win64-static/bin/ffmpeg -i " + url + " -vcodec copy -acodec copy " + name + ".mp4"
    command = "ffmpeg -i " + url + " -c copy " + name + ".mp4"
    print(command)
    # 执行命令
    try:
        retcode = subprocess.call(command, shell=True)
        if retcode == 0:
            print("successed------")
        else:
            print("failed--------")
    except Exception as e:
        print("Error:", e)


def main():
    video_url = get_video_url("https://www.iqiyi.com/v_pa5rm8r7do.html")
    print(video_url)
    download_video(video_url, "test")


if __name__ == '__main__':
    main()

