from socket import *
import threading,re
from multiprocessing import Process


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
            client_process = Process(target=self.handle_client, args=(client_socket,))
            client_process.start()
            client_socket.close()

    def handle_client(self, client_socket):
        """处理客户请求"""
        recv_data = client_socket.recv(4096).decode()
        request_list = recv_data.splitlines()
        print(request_list)
        '''for i in request_list:
            print(i)
        GET / HTTP / 1.1
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
            file_data = open(get_file_name,"rb")
        except IOError as e:
            # 构建响应报文 错误请求
            response_line = "HTTP/1.1 404 not found\r\n"
            response_body = "=====Sorry, file not found=====".encode()
            print("Request error:", e)
        else:
            response_line = "HTTP/1.1 200 OK\r\n"
            response_body = file_data.read()
            file_data.close()
        finally:
            response_headers = "Samuel: The Man Who From Sirius\r\n\r\n"
            send_response = (response_line + response_headers).encode() + response_body
            client_socket.send(send_response)
            client_socket.close()


def main():
    web_server = WebServer(8081)
    web_server.start()

if __name__ == '__main__':
    main()