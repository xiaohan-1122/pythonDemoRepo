#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo1
# @File: test_01.py
# @Author: xiaohanzhang
# @Data: 2020/8/19
""" 学员管理系统 """
gl_info = []

def add_info():
    """ 添加学员 """
    id = input('请输入学号:')
    name = input('请输入名字:')
    age = input('请输入年龄:')
    for dict in gl_info:
        if id == dict['id']:
            print('该用户已经存在')
            return
    gl_info.append({'id': id, 'name': name, 'age': age})
    print(gl_info)


def del_info():
    """ 删除学员 """
    id = input('请输入要删除的学员id:')
    for dict in gl_info:
        if id == dict['id']:
            gl_info.remove(dict)
            print('删除成功')
            break
    else:
        print('该学员不存在')

    print(gl_info)


def update_info():
    """ 修改学员信息 """
    id = input('请输入要修改的学员id:')
    for dict in gl_info:
        if id == dict['id']:
            dict['name'] = input(f'请输入id为{id}的学员名字:')
            dict['age'] = input(f'请输入id为{id}的学员年龄:')
            break
    else:
        print('该学员不存在')

    print(gl_info)


def search_info():
    """ 查找学员信息 """
    id = input('请输入要查找的学员id:')
    for dict in gl_info:
        if id == dict['id']:
            print(dict)
            break
    else:
        print('该学员不存在')


def print_all():
    """ 显示所有学员信息 """
    for dict in gl_info:
        print(f'学号:{dict["id"]}\t姓名:{dict["name"]}\t年龄:{dict["age"]}')


def info_print():
    """功能界面"""
    print('请选择功能-----------')
    print('1. 添加学员')
    print('2. 删除学员')
    print('3. 修改学员')
    print('4. 查询学员')
    print('5. 显示所有学员')
    print('6. 退出系统')
    print('*' * 30)


while True:
    # 1. 显示功能界面
    info_print()
    # 2. 用户输入功能序号
    user_num = int(input('请输入功能序号：'))
    # 3. 根据用户输入的功能序号，执行不同的功能
    if user_num == 1:
        add_info()
    elif user_num == 2:
        del_info()
    elif user_num == 3:
        update_info()
    elif user_num == 4:
        search_info()
    elif user_num == 5:
        print_all()
    elif user_num == 6:
        exit_flag = input('确定要退出吗? y or n\n')
        if exit_flag == 'y':
            print('退出系统')
            break
    else:
        print('输入有误')

