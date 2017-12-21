import sys, socket, re, multiprocessing

g_static_document_root = "./static"
g_dynamic_document_root = "./dynamic"


class WSGIServer(object):
    """WSGI服务的类"""
    def __init__(self, port, app):
        self.app = app
        self.web_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.web_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.web_server_socket.bind(("", port))
        self.web_server_socket.listen(128)

        self.response_header = ""  # 保存动态请求处理后的响应头

    def run_forever(self):
        while True:
            client_socket, client_addr = self.web_server_socket.accept()
            self.handle_request(client_socket)
            client_socket.close()

    def handle_request(self, client_socket):
        """处理请求信息,并作出响应"""
        request_list = client_socket.recv(4096).decode("utf-8").splitlines()

        path_info = re.match(r"([^/]*)([^ ]+)", request_list[0]).group(2)
        if path_info == "/":
            path_info = "/test.html"

        if re.search(r"\.html", path_info):
            env = {"file_name": path_info}
            print('动态请求路径:', path_info)
            response_body = self.app(env, self.handle_dynamic_request)
            send_data = self.response_header.encode() + response_body
            should_send_len = len(send_data)
            had_send_len = 0
            while had_send_len < should_send_len:
                had_send_len += client_socket.send(send_data)
            print("发送data:", send_data)
            print("动态页面发送完成,发送大小:", had_send_len)
            client_socket.close()

        else:
            try:
                f = open(g_static_document_root + path_info, "rb")
                print('静态请求路径:', g_static_document_root + path_info)
            except FileNotFoundError or OSError as e:
                print("请求的静态文件本地没有...", e)
                response_header = "HTTP/1.1 404 not found\r\n"
                response_header += "\r\n"
                response_body = "404 Not Found".encode()
            else:
                response_header = "HTTP/1.1 200 OK\r\n"
                response_header += "\r\n"
                response_body = f.read()
                f.close()
            finally:
                send_data = response_header.encode() + response_body
                should_send_len = len(send_data)
                had_send_len = 0
                while had_send_len < should_send_len:
                    had_send_len += client_socket.send(send_data)
                print("静态页面发送完成,发送大小:", had_send_len)
                client_socket.close()

    def handle_dynamic_request(self, state, header_list):
        self.response_header = "HTTP/1.1 %s\r\n" % state
        for key, value in header_list:
            self.response_header += "%s: %s\r\n" % (key, value)
        self.response_header += "\r\n"





def main():
    """控制web服务器整体"""
    # python3 mini_web.py 7878 App:app
    if len(sys.argv) == 3 and sys.argv[1].isdigit() and ":" in sys.argv[2]:
        port = int(sys.argv[1])
        module_name, app_name = sys.argv[2].split(":")
        print(sys.argv)
    else:
        print("输入方式: python3 mini_web.py 7878 App:app")
        return

    # 导入模块,创建对象
    web_fram_module = __import__(module_name)
    app = getattr(web_fram_module, app_name)

    http_server = WSGIServer(port, app)
    http_server.run_forever()

if __name__ == '__main__':
    main()