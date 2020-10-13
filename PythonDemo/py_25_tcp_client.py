#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_25_tcp_client.py
# @Author: xiaohanzhang
import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(("192.168.1.105", 7890))
    tcp_socket.send("啦啦啦啦啦".encode("utf-8"))
    recv_data = tcp_socket.recv(1024)
    print(recv_data.decode("utf-8"))
    tcp_socket.send("第二条".encode("utf-8"))
    recv_data = tcp_socket.recv(1024)
    print(recv_data.decode("utf-8"))
    tcp_socket.close()


if __name__ == "__main__":
    main()