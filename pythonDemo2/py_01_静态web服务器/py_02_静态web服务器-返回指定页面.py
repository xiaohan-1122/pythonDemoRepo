#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: pythonDemo2
# @File: py_02_静态web服务器-返回指定页面.py
# @Author: xiaohanzhang
# @Data: 2020/10/3
import os
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
        # 判断接收的数据是否为空
        if len(recv_data) == 0:
            new_socket.close()
            return
        # print(recv_data)
        # 对收到的二进制数据进行解码
        recv_content = recv_data.decode('utf-8')
        # 对数据按空格进行分割，maxsplit=2分割两次
        request_list = recv_content.split(' ', maxsplit=2)
        # 获取请求资源路径
        request_path = request_list[1]
        print(request_path)     # 如：/index.html
        # 打开文件，读取文件数据
        request_path = '/index.html' if request_path == '/' else request_path
        # 判断文件是否存在,下面方式或者异常
        # os.path.exists('../static' + request_path)
        try:
            # 使用rb(二进制)模式打开，兼容打开图片
            with open('../static' + request_path, 'rb') as f:
                file_data = f.read()
        except Exception as error:
            response_line = 'HTTP/1.1 404 Not Found\r\n'
            with open('../static/404.html', 'rb') as f:
                file_data = f.read()
        else:
            # 响应行
            response_line = 'HTTP/1.1 200 OK\r\n'
        finally:
            # 响应头
            respones_header = 'Server: TEST/1.1\r\n'
            # 响应体
            response_body = file_data
            # 把数据封装成HTTP响应报文格式的数据
            response = (response_line + respones_header + '\r\n').encode('utf-8') + response_body
            # 发送给浏览器的响应报文数据
            new_socket.send(response)
            # 关闭与服务于客户端的套接字
            new_socket.close()


if __name__ == '__main__':
    main()