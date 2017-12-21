import socket, gevent, re


class HTTPServer(object):
    """This class is use to deal http request & response"""
    # 传入port号, app名
    def __init__(self, port=8080, app=None):
        # 创建服务器套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # reuse port
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind
        self.server_socket.bind(("", port))
        # listen
        self.server_socket.listen(128)

        # save quote(引用)
        self.app = app

        self.response_data = ""

    # define running method
    def start(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()
            print(client_socket,client_addr)
            # creat gevent
            gevent.spawn(self.client_handler, client_socket)
            # pro = multiprocessing.Process(target=self.client_handler, args=(client_socket,))

    # define client_socket handel receive data
    def client_handler(self, client_socket):
        """This method use to handel receive data"""
        # transform data to utf-8
        request_data = client_socket.recv(4096).decode()
        # split data
        data_list = request_data.split("\r\n")
        print(data_list)
        # regex matching path 正则匹配路径
        """ GET /index.html?k=v&k2=v2 HTTP/1.1
                    GET 资源名 HTTP/1.1  """
        result = re.search(r"\w+\s+([^ ]+)", data_list[0])
        if not result:
            # prove this path is illegal
            client_socket.close()
            return

        path_info = result.group(1)
        print("Path info:", path_info)
        respose_line = "HTTP/1.1 200 OK\r\n"

        # web server default(默认) rule ( / == /index.html or /index.php)
        if path_info == "/":
            path_info = "/index.html"

        try:
            data_file = open("." + path_info, "rb")
        except FileNotFoundError or IOError as e:
            respose_line = "HTTP/1.1 404 Not Found\r\n"
            response_body = str(e).encode()
        else:
            # 如果文件过大,可以边读取边发送
            file_data = data_file.read()
            data_file.close()
            response_body = file_data
        finally:
            response_header = "Server: PythonWebServer1.0\r\n"
            respose_data = (respose_line + response_header + "\r\n").encode() + response_body

            # send file
            need_send_len = len(respose_data)
            had_send_len = 0  # 已经发送的大小
            """ data = '*' * 4097
                len = send(data)  # len =1024
                # 0-len-1 send(data[len:])
            """
            while had_send_len < need_send_len:
                had_send_len += client_socket.send(respose_data[had_send_len:])
                # time.sleep(0.01)
            client_socket.close()


def main():
    # 获取命令行输入
    import sys
    if len(sys.argv) != 3:
        print("python3  web.py  PortNumber  ModuleName:Instance(application:app)")
        return
    # 防止参数格式错误(端口号为字符串)
    try:
        port = int(sys.argv[1])
    except ValueError as e:
        print("python3  web.py  PortNumber  ModuleName:Instance", e)
        return
    else:
        # 切割出应用模块名和方法名
        moduleName_appName = sys.argv[2]
        element_list = moduleName_appName.split(":")

        print(element_list)
        # 取出模块名和方法名
        moduleName = element_list[0]
        appName = element_list[1]
        # 导入字符串的模块名和方法名
        application = __import__(moduleName)
        # getattr() 第一个参数为模块名,第二个参数为字符串的方法名
        app = getattr(application, appName)

        http_sever = HTTPServer(port, app)
        http_sever.start()


if __name__ == '__main__':
    main()