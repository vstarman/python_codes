#!/usr/bin/python3
from socket import *
import re, gevent, sys
from gevent import monkey
monkey.patch_all()


class WebServer(object):
    def __init__(self, port=8080, app=None):
        # 创建
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        # 收回端口
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 绑定
        self.server_socket.bind(("", port))
        # 监听
        self.server_socket.listen(128)
        # 保存一个应用程序的引用
        self.app = app
        # client_socket  client_address
        self.response_data = ""

    def start(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()
            client_gevent = gevent.spawn(self.handle_client, client_socket)
            client_gevent.join()


    def handle_client(self, client_socket):
        """处理客户请求"""
        recv_data = client_socket.recv(4096).decode()
        request_list = recv_data.splitlines()
        # print(request_list)
        for i in request_list:
            print(i)
        '''GET / HTTP / 1.1
        Host: 192.168.93.123: 8080
        Connection: keep - alive
        Cache - Control: max - age = 0
        Accept: text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8
        Upgrade - Insecure - Requests: 1
        User - Agent: Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 50.0.2661.102Safari / 537.36
        Accept - Encoding: gzip, deflate, sdch
        Accept - Language: zh - CN, zh;q = 0.8'''
        
        # 正则切割请求行路径
        result = re.search(r"\w+\s+([^ ]+)", request_list[0])
        if not result:
            client_socket.close()
            return

        path_info = result.group(1)
        print("request path is %s" % path_info)
        if path_info == "/":
            path_info = "./index.html"
        
        # 定义字典environ
        environ = {
            "file_name": path_info
        }
        # 处理动态资源请求
        if path_info.endswith(".py"):
            # 响应体就是返回数据
            response_body = self.app(environ, self.start_response)
            data = self.response_data + response_body
            client_socket.send(data.encode())
            client_socket.close()

        else:
            path_info = "." + path_info
        print("request path is %s" % path_info)
        try:
            file_data = open(path_info, "rb")
        except (IOError, FileNotFoundError) as e:
            # 构建响应报文 错误请求
            response_line = "HTTP/1.1 404 not found\r\n"
            response_body = open("./super404/index.html", "rb").read()
            print("Request error:", e)
        else:
            response_line = "HTTP/1.1 200 OK\r\n"
            response_body = file_data.read()
            file_data.close()
        finally:
            response_headers = "Samuel: The Man Who From Sirius\r\n"
            response_data = (response_line + response_headers + "\r\n").encode() + response_body

            # 需要发送的响应数据大小
            need_send_len = len(response_data)
            had_send_len = 0  # 已經發送的數據
            '''
            data = "*" * 4097
            len = send(data) # len = 1024
            # 0-len-1 send(data[len:])
            '''
            while had_send_len < need_send_len:
                had_send_len += client_socket.send(response_data[had_send_len:])
            client_socket.close()


def main():
    # 获取终端输入
    if len(sys.argv) != 3:
        print("python3 01.miniweb.py 8080 application:app")
        return
    try:
        port = int(sys.argv[1])
        print(sys.argv)
        # 如果用户输入的不是正确的数字字符构成的字符串
        # 那么转化就会报错
    except ValueError as e:
        print("python3 web.py 8080 应用模块名:可调用方法", e)
        return
    else:
        # 切割调用的数据库模块和函数名
        # application:app
        data_list = sys.argv[1].split(":")
        module_name = data_list[0]
        app_name = data_list[1]

        # 用__import__导入字符串的py文件,返回一个模块对象
        # getattr(对象,属性名) 返回对象的属性
        application = __import__(module_name, app_name)
        app = getattr(application, app_name)

        web_server = WebServer(port, app)
        web_server.start()


if __name__ == '__main__':
    main()
