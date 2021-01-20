# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: crawler11_图片验证码识别pytesseract.py
# @Author: xiaohanzhang
# @Date: 2021/1/7

import cv2 as cv
from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字


def recognize_text(image):
    # 边缘保留滤波  去噪
    blur = cv.pyrMeanShiftFiltering(image, sp=8, sr=60)
    cv.imshow('dst', blur)
    # 灰度图像
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    # 二值化  设置阈值  自适应阈值的话 黄色的4会提取不出来
    ret, binary = cv.threshold(gray, 185, 255, cv.THRESH_BINARY_INV)
    print(f'二值化设置的阈值：{ret}')
    cv.imshow('binary', binary)
    # 逻辑运算  让背景为白色  字体为黑  便于识别
    cv.bitwise_not(binary, binary)
    cv.imshow('bg_image', binary)
    # 识别
    test_message = Image.fromarray(binary)
    text = pytesseract.image_to_string(test_message)
    print(f'识别结果：{text}')


def main():
    src = cv.imread(r'./yanzhengma.png')
    cv.imshow('input image', src)
    recognize_text(src)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()