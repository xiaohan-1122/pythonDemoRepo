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
    try:
        # 添加数据
        # sql = 'insert into students values(null, "小绿", 12, 129.32, "男", "2002-02-02", 0)'
        # 修改数据
        # sql = 'update students set name = "小王" where id = 5'
        # 删除数据
        sql = 'delete from students where id = 5'
        # 执行sql语句
        row_count = cursor.execute(sql)
        print(f'语句执行影响的行数:{row_count}')
        # 提交数据到数据库
        conn.commit()
    except Exception as e:
        # 回滚数据
        conn.rollback()

    # 查询数据
    sql = 'select * from students'
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