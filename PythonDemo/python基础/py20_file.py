#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py20_file.py
# @Author: xiaohanzhang
# @Data: 2020/8/27
# ----------------------------------- 文件的基本操作 -----------------------------------------
"""
open() 打开文件 并且返回文件操作对象
read() 将文件内容读取到内存
write() 将指定内容写入文件
close() 关闭文件

open 函数默认以只读方式打开文件
    如果文件存在，返回文件操作对象
    如果文件不存在，会抛出异常
read 方法可以一次性读入并返回文件的所有内容
close 方法负责关闭文件
"""
try:
    file = open("../text")     # 打开文件(默认只读方式)
    text = file.read()      # 读取文件
    text2 = file.read()     # 已经读取过来，文件指针在末尾，读取不到任何内容
    file.close()            # 关闭文件

    print(text)
    print(len(text2))
    print("-" * 50)
except FileNotFoundError:
    print("文件不存在")
except Exception as e:
    print("未知错误 %s" % e)

"""
open方法参数：
1.第一个参数是要打开的文件名
2.第二个参数是访问方式
r: 以只读方式打开。文件指针会放在文件开头，如果文件不存在会抛出异常
w: 以只写方式打开。如果文件存在会被覆盖，如果文件不存在，创建新文件
a: 以追加方式打开。如果文件已存在，文件指针会放在文件结尾；如果文件不存在，会创建文件
r+:以读写方式打开。文件指针会放在文件开头，如果文件不存在会抛出异常
w+:以读写方式打开。如果文件存在会被覆盖，如果文件不存在，创建新文件
a+:以读写方式打开。如果文件已存在，文件指针会放在文件结尾；如果文件不存在，会创建文件
"""

file = open("../text", "a")
file.write("hello")
file.close()
print("-" * 50)

file = open("../text")
print(file.read())
file.close()
print("-" * 50)

# ----------------------------------- 按行读取文件内容 -----------------------------------------
"""
readline 方法可以一次读取一行内容
方法执行后，会把文件指针移动到下一行，准备再次读取
"""
# 读取大文件
file = open("../text")
while True:
    text = file.readline()
    if not text:
        break
    print(text, end="")

file.close()
print("\n")
print("-" * 50)

"""
readlines() 按行读取,读取全部内容
返回一个列表，每一行数据为一个元素
"""
file = open("../text")
text = file.readlines()
print(text)     # ['hello\n', '2222\n', '3333\n', '4444hellohello']
file.close()

# ----------------------------------- 文件指针 -----------------------------------------
"""
文件指针 标记从哪个位置开始读取数据
第一次打开文件时，通常文件指针会指向文件的开始位置
当执行了read方法后，文件指针会移动到文件内容的末尾
seek() 用来移动文件指针
文件对象.seek(偏移量, 起始位置) 起始位置: 0-文件开头  1-当前位置  2-文件结尾
"""

# ----------------------------------- 复制文件 -----------------------------------------
# 小文件复制
# file_read = open("text")
# file_write = open("text[副本]", "w")
#
# text = file_read.read()
# file_write.write(text)
#
# file_read.close()
# file_write.close()

# 大文件复制
file_read = open("../text")
file_write = open("text[副本]", "w")

while True:
    text = file_read.readline()
    if not text:
        break

    file_write.write(text)

file_read.close()
file_write.close()

# ----------------------------------- 文件\目录的常用管理操作 -----------------------------------------
# 需要导入os模块
import os
"""
文件操作：
rename      重命名文件       os.rename(源文件名, 目标文件名)
remove      删除文件         os.remove(文件名)
path.isfile 判断是否是文件    os.path.isfile(路径)

目录操作：
listdir     目录列表        os.listdir(目录名)
mkdir       创建目录        os.mkdir(目录名)
rmdir       删除目录        os.rmdir(目录名)
getcwd      获取当前目录     os.getcwd()
chdir       修改工作目录     os.chdir(目标目录)
path.isdir  判断是否是目录   os.path.isdir(路径)
"""
# os.rename('text.txt', 'new_text.txt')
print(os.getcwd())
# os.mkdir("测试")
os.remove(os.getcwd() + "/text[副本]")