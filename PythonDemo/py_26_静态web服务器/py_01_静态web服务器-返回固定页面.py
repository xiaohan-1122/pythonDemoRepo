#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: pythonDemo2
# @File: py_01_静态web服务器-返回固定页面.py
# @Author: xiaohanzhang
# @Data: 2020/10/3

import socket

def main():
    # 创建TCP服务套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用，程序退出，端口号立即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    tcp_server_socket.bind(('', 8000))
    # 设置监听
    tcp_server_socket.listen(128)

    # 循环等待客户端的连接请求
    while True:
        new_socket, ip_port = tcp_server_socket.accept()
        # 接收客户端的请求信息
        recv_data = new_socket.recv(4096)
        print(recv_data)
        # 打开文件，读取文件数据
        with open('../static/index.html', 'r') as f:
            file_data = f.read()

        # 响应行
        response_line = 'HTTP/1.1 200 OK\r\n'
        # 相应头
        respones_header = 'Server: TWS/1.1\r\n'
        # 空行
        # 响应体
        response_body = file_data
        # 把数据封装成HTTP响应报文格式的数据
        response = response_line + respones_header + '\r\n' + response_body
        # 字符串编码成二进制
        response_data = response.encode('utf-8')
        # 发送给浏览器的响应报文数据
        new_socket.send(response_data)
        # 关闭与服务于客户端的套接字
        new_socket.close()


if __name__ == '__main__':
    main()