#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_04_string.py
# @Author: xiaohanzhang
# @Data: 2020/8/5

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

str = 'python'
print(str[0:-1])    # 下标为0的字符到倒数第二个字符
print(str[0])       # 下标为0的字符
print(str[2:4])     # 下标为2的字符到下标为4之前的字符
print(str[2:])      # 下标2开始的后的所有字符
print(str * 2)      # 输出字符串两次
print(str + "TEST") # 连接字符串
print(str[-1:])     # -1表示最后一个字符
print('*' * 50)
# 使用反斜杠()转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串
print('aa\nbb')
print(r'aa\bb')
print('*' * 50)


# 字符串的切片，切片同样适用于list和tuple
# str[索引:索引:步长] 步长是选取间隔，正负数均可，负数表示从右边开始选取
str = "0123456789"
str1 = str[0:5]
print(str1)         # 01234
str2 = str[0:8:3]   # 从下标为0的字符开始，到下标为8的字符之前（左闭右开）,每隔三个字符取一个
print(str2)         # 036
# -1表示从右向左切
print(str[-1::-1])  # 9876543210
print(str[::-1])    # 9876543210


string = "abcdefgocdoe"
# 字符串string长度
print(len(string))

# string中字符串"o"的个数
print(string.count("o"))

# 字符串string中是否包含字符串“a”,返回string中第一个“a”所在下标,不存在返回-1
print(string.find("a"))
print(string.rfind("a"))    # 从右往左查找

# 返回字符串string中字符串“a“所在下标，不存在报异常
print(string.index("a"))
print(string.rindex("a"))  # 从右往左查找

# 将string中的"old"用"new"替换,原字符串不会改变，返回新的字符串
string.replace("old", "new")
string.replace("old", "new", 1)  # 只替换第一个"old"字符串

# 判断字符串string是否以"a"开头
print(string.startswith("a"))

# 判断字符串string是否以"s"结尾
print(string.endswith("s"))

# 将字符串string转为小写
print(string.lower())

# 将字符串string转为大写
print(string.upper())

# 去掉字符串左边空格
string.lstrip()

# 去掉字符串右边空格
string.rstrip()

# 去掉字符串两边空格
string.strip()

width = 20
# 返回原字符串左对齐，并且使用空格填充至长度的width的新字符串
string.ljust(width)

# 返回原字符串右对齐，并且使用空格填充至长度的width的新字符串
string.rjust(width)

# 返回原字符串居中，并且使用空格填充至长度的width的新字符串
string.center(width)

# 将字符串按照某个字符串进行分割,split()方法不传任何参数时,则按照任意空白字符分割
string = "er ewe dsdsf fdsfs"
print(string.split(" "))    # ['er', 'ewe', 'dsdsf', 'fdsfs']

# 将字符串string以"str"分割为三部分，str前、str、str后，以第一个"str"为准
string.partition("str")
string.rpartition("str")  # 从右边起

# 字符串按 “\n”切割
string.splitlines()

# 字符串中是否都是数字,都不能判断小数
string.isdecimal()  # 全角数字,尽量使用这个方法
string.isdigit()    # 全角数字、"(1)"、\u00b2(unicode字符串)
string.isnumeric()  # 全角数字、汉字数字

# 字符串中是否都是字母
string.isalpha()

# 字符串中是否只有数字和字母
string.isalnum()

# 字符串中只包含空格
string.isspace()

# string每一个字符后插入字符串sss,构造新的字符串
sss = "xxx"
print(sss.join(string))  # axxxbxxxcxxx1xxx2xxx3

# 去掉字符串中的空格和\t
string = "sd hs\tj  fgdh \tsfg\tdshf gdshj f gs"
print("".join(string.split()))

print('*' * 50)


# 练习
'''需求：
    1、将字符串中的空白字符去掉
    2、使用" "作为分隔符，拼接成一个整齐的字符串
'''
poem_str = "关关雎鸠\t 在河之洲 窈窕淑女 \t 君子好逑"
print(poem_str)     # 关关雎鸠	 在河之洲 窈窕淑女 	 君子好逑
poem_list = poem_str.split()
print(poem_list)    # ['关关雎鸠', '在河之洲', '窈窕淑女', '君子好逑']
poem_str = " ".join(poem_list)
print(poem_str)     # 关关雎鸠 在河之洲 窈窕淑女 君子好逑

