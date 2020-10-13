#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_25_socket.py
# @Author: xiaohanzhang
# @Data: 2020/9/28

import socket

"""
套接字使用流程：
1. 创建套接字
2. 使用套接字收/发数据
3. 关闭套接字
"""
# ---------------------------------------------- 创建一个TCP socket ----------------------------------------

# 创建socket套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ...使用套接字的功能...
print("tcp_socket------")

# 不使用时，关闭套接字
tcp_socket.close()


# ---------------------------------------------- 创建一个UDP socket ----------------------------------------
# 发送数据
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ...使用套接字的功能...
udp_socket.sendto(('哈哈哈哈哈哈'.encode('utf-8')), ("192.168.31.254", 8080))

print("udp_socket------")

# 不使用时，关闭套接字
udp_socket.close()

# 接收数据
# 创建一个UDP socket
udp_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定一个本地信息
localaddr = ("", 7788)
udp_recv_socket.bind(localaddr)

# 模拟发送数据
udp_sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_sender_socket.sendto(('哈哈哈哈哈哈'.encode('utf-8')), ("192.168.31.254", 7788))
udp_sender_socket.close()

# 接收数据
recv_data = udp_recv_socket.recvfrom(1024)
recv_msg = str(recv_data[0], 'utf-8')
sender_addr = recv_data[1]
print('msg = %s addr = %s' % (recv_msg, sender_addr))
udp_recv_socket.close()

