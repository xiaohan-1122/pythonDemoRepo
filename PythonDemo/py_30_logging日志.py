#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_30_logging日志.py
# @Author: xiaohanzhang
# @Data: 2020/10/23
import logging

# 设置logging日志的配置信息
# level     级别 默认warning
# %(asctime)s   当前时间
# %(filename)s  文件名
# %(lineno)d    行号
# %(levelname)s 日志级别
# %(message)s   日志信息
# filename      将日志保存到文件中
# filemode      文件写入方式 a追加 重写
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s-%(filename)s[lineno:%(lineno)d-%(levelname)s-%(message)s]", filename="log.txt", filemode="a")
# 2020-10-23 22:22:23,137-py_30_logging日志.py[lineno:14-INFO-这是一个info日志]

logging.debug("这是一个debug日志")
logging.info("这是一个info日志")
logging.warning("这是一个warning日志")
logging.error("这是一个error日志")
logging.critical("这是一个critical日志")
