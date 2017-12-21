import socket, time, re, sys

class WSGIServer():
    """定义一个wsgi服务器的类"""

    def __init__(self, documents_root, port):
        # creat
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # reuse
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # BIND
        self.server_socket.bind(("", port))
        # listen
        self.server_socket.listen(128)

        # 非阻塞
        self.server_socket.setblocking(False)
        # 存放client_socket
        self.client_socket_list = []

        self.documents_root = documents_root

    def run_forever(self):
        """运行服务器"""

        while True:
            try:
                #time.sleep(0.5)
                new_socket, new_addr = self.server_socket.accept()
            except Exception as e:
                print("---------1---------",e)
            else:
                new_socket.setblocking(False)
                self.client_socket_list.append(new_socket)

            for client_socket in self.client_socket_list:
                try:
                    request = client_socket.recv(1024).decode()
                except Exception as e:
                    print("---------2---------", e)
                else:
                    if request:
                        self.deal_with_request(request, client_socket)
                    else:
                        client_socket.close()
                        self.client_socket_list.remove(client_socket)
            print(self.client_socket_list)

    def deal_with_request(self, request, client_socket):
        """为当前浏览器服务"""
        if not request:
            return

        request_lines = request.splitlines()
        for i, line in enumerate(request_lines):
            print(i, "\t", line)

        # 提取请求文件
        ret = re.match(r"[^/]*([^ ]+)", request_lines[0])
        if ret:
            print("提取数据>>>>[%s]" % ret.group(1))
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "index.html"
        else:
            return

        # 读文件
        try:
            f = open(self.documents_root + file_name, "rb")
        except:
            response_body = "file not found, 请输入正确的url"
            response_header = "HTTP/1.1 404 not found\r\n"
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += "Content-Length: %d\r\n" % (len(response_body))
            response_header += "\r\n"

            # 返回浏览器
            client_socket.send((response_header + response_body).encode())
        else:
            content = f.read()
            f.close()

            response_body = content
            response_header = "HTTP/1.1 200 0K\r\n"
            response_header += "Content-Length: %d\r\n" % (len(response_body))
            response_header += "\r\n"

            client_socket.send((response_header + response_body).encode())

def main():
    """控制web服务器整体"""

    if len(sys.argv) == 1:
        port = 8080
    elif len(sys.argv) == 2:
        port = sys.argv[1]
        if port.isdigit():
            port = int(port)
    else:
        print("运行方式如: python3 xxx.py 7890")

    http_server = WSGIServer(".", port)
    http_server.run_forever()

if __name__ == '__main__':
    main()
