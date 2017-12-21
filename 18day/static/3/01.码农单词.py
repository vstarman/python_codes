from socket import *
import re, gevent, sys
from gevent import monkey
monkey.patch_all()


class WebServer(object):
    def __init__(self, port=8080):
        # 创建
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        # 收回端口
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 绑定
        self.server_socket.bind(("", port))
        # 监听
        self.server_socket.listen(128)

    def start(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()
            client_gevent = gevent.spawn(self.handle_client, client_socket)
            client_gevent.join()

    def handle_client(self, client_socket):
        """处理客户请求"""
        recv_data = client_socket.recv(4096).decode()
        request_list = recv_data.splitlines()
        #print(request_list)
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
        
        get_file_name = result.group(1)
        print("request path is %s" % get_file_name)
        if get_file_name == "/":
            get_file_name = "./index.html"
        else:
            get_file_name = "." + get_file_name
        print("request path is %s" % get_file_name)
        try:
            file_data = open(get_file_name, "rb")
        except IOError as e:
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
            had_send_len = 0    # 已經發送的數據
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
    if len(sys.argv) > 2:
        print("python3 web 8080")
        return

    elif len(sys.argv) == 1:
        web_server = WebServer()
        web_server.start()
    else:
        try:
            port = int(sys.argv[1])
            print(sys.argv)
            # 如果用户输入的不是正确的数字字符构成的字符串
            # 那么转化就会报错
        except ValueError as e:
            print("python3 web 8080",e)
            return
        web_server = WebServer(port)
        web_server.start()

if __name__ == '__main__':
    main()