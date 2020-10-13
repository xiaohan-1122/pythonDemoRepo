#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo1
# @File: py_21模块和包.py
# @Author: xiaohanzhang
# @Data: 2020/9/26

import py_21_test_module
import py_21_test_module as tm
from py_21_test_module import say_hello

import py_21_message

# ------------------------------- 模块 -------------------------------------
"""
模块的导入：
import 模块1
import 模块2

通过 模块名. 使用模块提供的全局变量、方法、类
模块导入时指定别名: import 模块1 as 模块别名

局部导入from...import：
如果希望从一个模块中导入部分工具，可以使用from...import 的方式
import 模块名是一次性将模块中所有工具全部导入，并且通过模块名/别名访问
from 模块名1 import 工具名
导入之后可以直接使用模块提供的工具--全局变量、函数、类
注：如果两个模块，存在同名的函数，后导入模块的函数会覆盖先导入模块的函数

从模块中导入所有工具(知道)
from...import *
"""

py_21_test_module.say_hello()
tm.say_hi()
say_hello()

# 模块路径
print(py_21_test_module.__file__)

"""
在导入模块文件时，文件中所有没有缩进的代码都会被执行一遍
__name__ 属性可以做到，测试模块的代码只在测试情况下被运行，而在被导入时不会执行
__name__是python的内置属性，记录着一个字符串
如果是被其它文件导入的，__name__就是文件名
"""
print(py_21_test_module.__name__)  # py_17_testModule
print(__name__)  # __main__

"""
# 导入模块
# 定义全局变量
# 定义类
# 定义函数

# 在代码最下方
def main():
    pass

# 根据__name__判断 是否执行下面的方法
if __name__ == "__main__":
    main()
"""

# ------------------------------- 模块 all列表 -------------------------------------
"""
如果一个模块中有__all__变量，当使用from xxx import *导入时，只能导入这个列表中的元素。
test_module模块中代码：
__all__ = ['testA']
def testA():
    print('testA')

def testB():
    print('testB')
使用from test_module import *导入时，只能导入testA(),而无法导入testB().
"""


# ------------------------------- 包 -------------------------------------
"""
包是一个包含了多个模块的特殊目录
目录下有一个特殊文件 __init__.py
包名的命名方式与变量名一致，小写字母+_
使用 import 包名 可以一次性导入包中的所有模块

__init_.py
要在外界使用包中的模块，需要在__init_.py中指定对外界提供的模块列表
from py_21_message import py_17_send_message
from py_21_message import py_17_receive_message
"""
py_21_message.py_21_send_message.send("你是🐷吗")
txt = py_21_message.py_21_receive_message.receive()
print(txt)

# ------------------------------- 发布模块(知道) -------------------------------------
"""
步骤：
1.创建setup.py文件
from distutils.core import setup

setup(name="xh_message",    # 包名
      version="1.0.0",      # 版本号
      description="发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块", # 完整的描述信息
      author="xiaohan",     # 作者
      author_email="xiaohan@gamil.com",  # 作者邮箱
      url="www.xiaohan.com",    # 主页
      py_21_message=["py_21_message.py_17_send_message", "py_21_message.py_17_receive_message"]) # 模块中包含的文件名称

2.构建模块
终端：$ python3 setup.py build

3.生成发布压缩包
终端：$ python3 setup.py sdist


安装模块
$ tar -zxvf py_21_message-1.0.0.tar.gz
$ sudo python3 setup.py install

卸载模块
直接从安装目录将模块目录删除即可
$ cd /usr/local/lib/python3/dist-packages/
$ sudo rm -r py_21_message*
可以通过__file__内置属性获取模块所在路径
$ ipython3
$ import py_21_message
$ py_21_message.__file__
"""