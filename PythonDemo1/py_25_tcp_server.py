#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo1
# @File: py_25_tcp_server.py
# @Author: xiaohanzhang
import socket


def main():
    # 创建一个UDP socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定本地信息
    tcp_socket.bind(("", 7890))
    # 让默认套接字由主动变为被动
    tcp_socket.listen(128)
    # 循环目的：多次调用accept 从而为多个客户端服务
    while True:
        print("等待一个新客户端到来......")
        # 等待客户端连接
        new_client_socket, client_addr = tcp_socket.accept()
        print("一个新客户端连接%s" % str(client_addr))

        # 循环目的：为同一个客户端服务多次
        while True:
            # 接收客户端发过来的数据
            recv_data = new_client_socket.recv(1024)
            print("客户端发过来的数据：%s" % recv_data.decode("utf-8"))
            # 如果recv解堵塞，有2中方式：
            # 1.客户端发送数据过来
            # 2.客户端调用close 导致结束
            if recv_data:
                # 回送数据给客户端
                new_client_socket.send("收到了".encode("utf-8"))
            else:
                break

        # 关闭套接字 意味着不会再为这个客户端服务
        new_client_socket.close()
        print("服务完毕........")

    # 关闭服务器套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()

