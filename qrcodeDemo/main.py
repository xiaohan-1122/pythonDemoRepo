# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: main.py
# @Author: xiaohanzhang
# @Date: 2020/12/16
# 需要安装Pillow模块
import qrcode
from PIL import Image


def get_qrcode(data_str, name):
    """ 生成普通二维码 """
    img = qrcode.make(data=data_str)
    with open(name, 'wb') as f:
        img.save(f)


def get_qrcode_with_color(data_str, name):
    """ 生成带颜色二维码 """
    # 创建QRCode对象
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )

    # 添加信息，data_str为拟创建二维码中的信息字符串
    qr.add_data(data_str)
    # 生成二维码
    qr.make(fit=True)
    # 获取二维码图像并设置颜色
    # img = qr.make_image()
    img = qr.make_image(fill_color="red", back_color="blue")
    with open(name, 'wb') as f:
        img.save(f)


def get_qrcode_with_logo(data_str, logo_path, name):
    """ 生成带logo的二维码"""
    # 创建QRCode对象
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )

    # 添加信息，data_str为拟创建二维码中的信息字符串
    qr.add_data(data_str)
    # 生成二维码
    qr.make(fit=True)
    # 获取二维码图像
    img = qr.make_image()
    # 转换图像格式
    img = img.convert("RGBA")
    # 获取图像宽、高
    img_w, img_h = img.size
    # 打开logo图像，logo_path为logo的文件名和路径
    logo = Image.open(logo_path)
    # 比例因子，即logo宽度为二维码图像的1/3左右
    factor = 3
    # 生产二维码中logo宽高
    logo_w = int(img_w / factor)
    logo_h = int(img_h / factor)
    logo = logo.resize((logo_w, logo_h), Image.ANTIALIAS)
    # 转换logo格式
    logo = logo.convert("RGBA")
    # 计算粘贴位置
    w = int((img_w - logo_w) / 2)
    h = int((img_h - logo_h) / 2)
    # 将logo粘贴到二维码图像
    img.paste(logo, (w, h))

    with open(name, 'wb') as f:
        img.save(f)


def main():
    # get_qrcode('https://baidu.com', 'baidu.png')
    # get_qrcode_with_color('https://baidu.com', 'baidu-color.png')
    get_qrcode_with_logo('谁扫谁是傻瓜！！！', 'ee.jpg', 'baidu-logo.png')


if __name__ == '__main__':
    main()

