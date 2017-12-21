from gevent import monkey

monkey.patch_all()
import gevent
import socket
import re
import time


class HTTPServer(object):
    """这是一个处理HTTP请求和响应报文的类"""

    def __init__(self, port=8080, app=None):
        # 创建服务器套接字 server_socket listen_socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 当程序重启时  报 地址已经被使用
        # 1 Pycharm后台还有进程存活
        # 2 TCP 等待2MSL时间才能继续被下一次重新使用
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('', port))

        self.server_socket.listen(128)

        # 保存一个应用程序的引用
        self.app = app
        # client_socket client_address
        self.response_data = ""

    def start(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()

            # 创建一个协程
            gevent.spawn(self.client_handler, client_socket)
            # pro = multiprocessing.Process(target=self.client_handler, args=(client_socket,))

    def client_handler(self, client_socket):
        """这是处理客户端请求的函数"""
        request_data = client_socket.recv(4096)

        """ GET /index.html?k=v&k2=v2 HTTP/1.1
            GET 资源名 HTTP/1.1  """
        request_str_data = request_data.decode()  # 字节->字符串
        data_list = request_str_data.split("\r\n")
        request_line = data_list[0]
        result = re.search(r"\w+\s+([^ ]+)", request_line)
        # result.group(0)表示正则整体匹配的结果
        if not result:
            # 说明不是一个合法的HTTP请求
            client_socket.close()
            return

        path_info = result.group(1)
        print("path info :", path_info)  # ./
        response_line = "HTTP/1.1 200 OK\r\n"  # 响应行

        # web服务器的 默认规则 / == /index.php /index.html
        if path_info == '/':
            path_info = '/index.html'

        env = {
            "FILE_NAME": path_info
        }
        # 处理动态资源请求
        if path_info.endswith(".py"):
            # 响应体就是返回数据
            response_body = self.app(env, self.start_response)

            # WSGI建议 响应体使用字节类型的数据
            data = self.response_data.encode() + response_body
            client_socket.send(data)
            client_socket.close()
        else:
            # 处理静态资源请求的代码
            try:
                data_file = open("." + path_info, "rb")
            except FileNotFoundError as e:
                # 错误
                response_line = "HTTP/1.1 404 Not Found\r\n"  # 响应行
                response_body = str(e).encode()
            else:
                # 如果文件过大 不适合全部读取  可以考虑边读取边发送

                file_data = data_file.read()
                # 关闭文件 资源
                data_file.close()
                response_body = file_data
            finally:
                response_header = "Server: PythonWebServer1.0\r\n"  # 响应头
                response_data = (response_line + response_header + "\r\n").encode() + response_body

                # 需要发送的响应数据大小
                need_send_len = len(response_data)
                had_send_len = 0  # 已经发送的数据大小
                """ data = '*' * 4097
                    len = send(data)  # len =1024
                    # 0-len-1 send(data[len:])
                """
                while had_send_len < need_send_len:
                    had_send_len += client_socket.send(response_data[had_send_len:])  # str->bytes
                    # time.sleep(0.01)
                client_socket.close()

    def start_response(self, status, header_list):
        response_line = "HTTP/1.1 %s\r\n" % status

        response_headers = ""
        for header_name, header_value in header_list:
            response_headers += ("%s: %s\r\n" % (header_name, header_value))

        self.response_data = response_line + response_headers + "\r\n"


def main():
    # 狗吃草
    # 吃(狗，草)
    # 狗.吃(草)

    import sys
    if len(sys.argv) != 3:
        print("python3 web.py 8080 应用模块名:可调用方法名")
        return
    # python3 web.py aaaa
    try:
        port = int(sys.argv[1])
    # 如果用户输入的不是正确的数字字符构成的字符串 那么转化的时候就会报错
    except ValueError as e:
        print("python3 web.py 8080", e)
        return
    else:

        # 切割出应用模块名和可调用方法名
        # application:app
        # print(sys.argv[2])
        moudle_name_app_name = sys.argv[2]
        data_list = moudle_name_app_name.split(":")

        print(data_list)
        # 模块名
        moudle_name = data_list[0]
        # 可执行函数的名称
        app_name = data_list[1]

        applicaton = __import__(moudle_name)
        app = getattr(applicaton, app_name)

        # 80是著名端口 在MAC LINUX平台上如果需要绑定 需要root权限
        http_server = HTTPServer(port, app)
        http_server.start()


if __name__ == '__main__':
    main()
