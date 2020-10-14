#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_27_pymysql.py
# @Author: xiaohanzhang
# @Data: 2020/10/13

import pymysql

def main():
    # 创建连接对象
    conn = pymysql.connect(host='47.92.123.248',
                           port=3306,
                           user='root',
                           password='A262408_a',
                           database='test_database',
                           charset='utf8')
    # 获取游标
    cursor = conn.cursor()
    # sql语句
    sql = 'select * from students'
    # 执行sql语句
    cursor.execute(sql)
    # 获取查询结果
    # row = cursor.fetchone()
    # print(row)
    data_tuple = cursor.fetchall()
    for row in data_tuple:
        print(row)
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


if __name__ == '__main__':
    main()