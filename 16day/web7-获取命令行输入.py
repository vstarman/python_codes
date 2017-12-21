import socket, re, sys, gevent, multiprocessing, threading
from gevent import monkey
monkey.patch_all()


class HTTPServer(object):
    def __init__(self, port, app):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 允许在7788端⼝资源没有彻底释放完毕时，可以重复绑定7788端⼝
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("", port))
        self.server_socket.listen(128)
        self.app = app
        self.response_data = ""

    def server_forever(self):
        """循环运行web服务器，等到客户端链接，并为客户端服务"""
        while True:
            client_socket, client_addr = self.server_socket.accept()
            print(client_addr)
            gevent.spawn(self.deal_request, client_socket)
            # gevent不用start方法
            # client_process.start()
            # 线程共享套接字，不能关闭！
            # client_socket.close()

    def deal_request(self, client_socket):
        """以长链接方式,为浏览器服务器"""
        while True:
            recv_data = client_socket.recv(1024).decode()
            if not recv_data:
                client_socket.close()
                return
            # print("-" * 80)
            # for line in recv_data.splitlines():
            #     print(line)
            # print("-" * 80)

            """b'GET / HTTP/1.1\r\n
            Host: 127.0.0.1:7788\r\n
            Connection: keep-alive\r\n
            Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n
            Upgrade-Insecure-Requests: 1\r\n
            User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36\r\n
            Accept-Encoding: gzip, deflate, sdch\r\n
            Accept-Language: zh-CN,zh;q=0.8\r\n\r\n'"""
            request_header_lines = recv_data.splitlines()
            path_info = re.match(r"\w+\s+([^ ]+)", request_header_lines[0]).group(1)
            print(path_info)

            if path_info == "/":
                path_info = g_static_document_root + "/index.html"
            elif path_info.endswith(".py"):
                env = {
                    "file_name": path_info
                }
                print("请求动态路径:", path_info)
                response_body = self.app(env, self.set_response_header)
                client_socket.send(self.response_data.encode() + response_body)
                client_socket.close()
                return

            try:
                f = open(path_info, "rb")
            except IOError or FileNotFoundError as e:
                response_headers = "HTTP/1.1 404 not found\r\n"
                response_headers += "Content-Type: text/html; charset=utf-8\r\n"
                response_headers += "\r\n"
                response_boody = ">>>>>>>>Sorry, file not found, 请输入正确url>>>>>>>>>".encode()
                print(e)
            else:
                # 组织响应头
                response_headers = "HTTP/1.1 200 OK\r\n\r\n"  # 200 找到资源
                # 组织响应体
                response_boody = f.read()
            finally:
                response = response_headers.encode() + response_boody
                # 遇到大文件时会接收不完全
                should_send_length = len(response_boody)
                had_send_length = 0
                while had_send_length < should_send_length:
                    had_send_length += client_socket.send(response[had_send_length:])
                    print("发送文件大小:", had_send_length)
                client_socket.close()

    def set_response_header(self, status, headers_list):
        """用来拼接响应行和体,此方法会在web框架中被默认调用"""
        response_line = "HTTP/1.1 %s\r\n" % status
        response_headers = ""
        for header_name, header_value in headers_list:
            response_headers += ("%s: %s\r\n" % (header_name, header_value))
        self.response_data = response_line + response_headers + "\r\n"


# 配置静态服务器资源
g_static_document_root = "./html"
# 配置动态服务器资源
g_dynamic_document_root = "./web"


def main():
    """python3 web.py 8080"""
    if len(sys.argv) != 3 or not sys.argv[1].isdigit() or ":" not in sys.argv[2]:
        print("请输入正确命令格式：python3 web.py 8080 webApp:app")
        return
    else:
        port = int(sys.argv[1])
        str_list = sys.argv[2].split(":")
        # 切割模块名和对象名
        module_name = str_list[0]
        app_name = str_list[1]
        # 导入web框架主模块
        web_frame_module = __import__(module_name)
        # 获取可直接使用的函数或对象
        app = getattr(web_frame_module, app_name)

        web = HTTPServer(port, app)
        print(sys.argv)
        web.server_forever()


if __name__ == '__main__':
    main()
