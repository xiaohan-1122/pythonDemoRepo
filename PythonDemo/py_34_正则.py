#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_34_正则.py
# @Author: xiaohanzhang
# @Data: 2020/10/31
import re

# 使用match方法进行匹配操作
result = re.match("hello", 'hello xiaobai')
# 如果匹配到数据，通过group方法提取数据
info = result.group()
print(info)
"""
匹配单个字符
.   匹配任意1个字符(除了\n)
[]  匹配[]中列举的字符串
\d  匹配数字，即0-9
\D  匹配非数字，即不是数字
\s  匹配空白字符，即空格、tab键
\S  匹配非空白字符
\w  匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
\W  匹配特殊字符，即非字母、非数字、非_、非汉字

匹配多个字符
*   匹配前一个字符出现0次或无限次，即可有可无
+   匹配前一个字符出现1次或无限次，即至少有1次
?   匹配前一个字符出现0次或1次，即至多1次
{m}  匹配前一个字符出现m次
{m,n}   匹配前一个字符出现 m 到 n 次
[^指定字符] 除了指定字符都匹配
匹配开头和结尾
^   匹配字符串开头
$   匹配字符串结尾


匹配分组
|   匹配左右任意一个表达式
(ab)    将括号中字符串作为一个分组
\num    引用分组num匹配到的字符串
(?P<name>)  分组起别名
(?P=name)   引用别名为name分组匹配到的字符串
"""
# -------------- 匹配单个字符 ------------------
# .表示任意一个字符
match_obj = re.match("t.o", "two")
if match_obj:
    print(match_obj.group())    # two
else:
    # 匹配失败，match_obj是None
    print('匹配失败')

# []  匹配[]中列举的字符串
match_obj = re.match("葫芦娃[12]", "葫芦娃1 爷爷")
print(match_obj.group())    # 葫芦娃1
match_obj = re.match('[0-9]', '8')

# 匹配数字
match_obj = re.match('\d', '7')
# 匹配非数字
re.match('\D', 'a')
# 匹配空白字符
match_obj = re.match('葫芦娃\s[12]', '葫芦娃 1')
print(match_obj.group())
# 匹配非空白字符
match_obj = re.match('葫芦娃[\S]', '葫芦娃3')
print(match_obj.group())    # 葫芦娃3
# 匹配非特殊字符
match_obj = re.match('\w', 'd')
# 匹配特殊字符
match_obj = re.match('\W', '&')


# -------------- 匹配多个字符 ------------------
# w出现0次或多次
match_obj = re.match("tw*o", "twwwwwo")
print(match_obj.group())
# 中间任意字符出现0次或多次
match_obj = re.match("t.*o", "tdaso")
# w至少出现一次
match_obj = re.match("tw+o", "two")
# t出现2次
match_obj = re.match("ht{2}p", "http")
# t出现2-4次
match_obj = re.match("ht{2,4}p", "htttp")
# t至少出现2次
match_obj = re.match("ht{2,}p", "htttp")


# -------------- 匹配开头和结尾 ------------------
# 匹配数字开头
match_obj = re.match("^\d.*", "12dss")
# 匹配数字结尾
match_obj = re.match(".*\d$", "dsds2")

# 中间除了abc都匹配
match_obj = re.match("a[^abc]f", "agf")
print(match_obj.group())



