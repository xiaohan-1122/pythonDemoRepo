#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py_30_miniWeb框架-Ajax.py
# @Author: xiaohanzhang
# @Data: 2020/10/31
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse
from urllib.parse import parse_qs
from os import path

host = ('localhost', 8888)


class Resquest(BaseHTTPRequestHandler):

    def do_GET(self):
        querypath = urlparse(self.path)
        print(querypath)
        filepath, query = querypath.path, querypath.query
        args = parse_qs(query)
        try:
            print("name = ", args['name'])
            print("age = ", args['age'])
        except KeyError as e:
            print('KeyError = ', e, 'is exist')

        if filepath == '/' or filepath == '/?':
            filepath = "/getAndPost.html"

        try:
            f = open("./html" + filepath, "rb")  # 读取的是二进制
        except:
            response = "HTTP/1.1 404 NOT FOUND\r\n"
            response += "\r\n"
            response += "---------file not found-------"
            self.wfile.write(response.encode("utf-8"))
        else:
            html_content = f.read()
            f.close()
            # 返回HTTP格式的数据给浏览器
            # 将response header发送给浏览器
            self.send_response(200, 'OK')
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # 将response body发送给浏览器
            if len(args) > 0:
                self.wfile.write(json.dumps(args).encode())
                return
            self.wfile.write(html_content)

        # self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = parse_qs(self.rfile.read(length).decode('utf-8'))
        print('postdata = ', post_data)
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        if len(post_data) > 0:
            self.wfile.write(json.dumps(post_data).encode())
            return
        self.wfile.write("nothing".encode("utf-8"))


def main():
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()


if __name__ == '__main__':
    main()