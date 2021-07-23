# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: getRandomMac.py
# @Author: xiaohanzhang
# @Date: 2021/4/25

import random


def getRandomMac():

    Maclist = []
    for i in range(1, 7):
        RANDSTR = "".join(random.sample("0123456789abcdef", 2))
        Maclist.append(RANDSTR)
        mac = ":".join(Maclist)
    print(mac)


def main():
    getRandomMac()


if __name__ == '__main__':
    main()
