import sys, re, socket, multiprocessing

# 设置静态资源访问路径
document_static = "./static"
# 设置动态资源访问路径
document_dynamic = "./dynamic"



class WSGIServer(object):
    """用来生成http服务器对象"""
    def __init__(self, port, app):
        # 1.创建套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("", port))
        self.server_socket.listen(128)

        self.document_static = document_static
        self.response_header = ""  # 用来存储动态请求的响应头
        self.app = app

    def run_forever(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()
            client_socket.settimeout(3)  # TODO what's this ??????
            client_process = multiprocessing.Process(target=self.handle_request, args=(client_socket, ))
            client_process.start()
            client_socket.close()

    def handle_request(self, client_socket):
        try:   # 不能用utf8解码,会报错(比如有emoji表情的utf8),也可以写成decode("utf-8",error=ignore)
            request_list = client_socket.recv(4096).decode("utf-8").splitlines()
        except Exception as e:
            print("==========>", e)
            client_socket.close()
            return
        # for line in request_list:   # 打印请求
        #     print(line)

        # 提取请求文件 GET /emoji HTTP/1.1
        ret = re.match(r"([^/]*)([^ ]+)", request_list[0])
        path_info = ret.group(2)
        if ret:
            # print("请求格式为:", ret.group(1))
            # print("请求路径为:", ret.group(2))
            if path_info == "/":
                path_info = "/index.html"
        # 不是以.py文件为结尾的路径,都认为是普通文件;
        # 反之,即为动态请求路径,移交小弟web框架处理
        if not re.search(r"\.html", path_info):
            response_header = ""  # 防止finally语法提醒
            try:  # 读取该路径文件
                f = open((self.document_static + path_info), "rb")
                print("静态请求路径路径:", (self.document_static + path_info))

            except FileNotFoundError or IOError as e:
                response_body = open("./static/super404/index.html", "rb").read()
                response_header = "HTTP/1.1 404 Not Found\r\n"
                response_header += "Content-Type: text/html; charset=utf-8\r\n"

            else:
                response_body = f.read()
                print("请求文件大小:", len(response_body))
                response_header = "HTTP/1.1 200 OK\r\n"
                f.close()

            finally:
                response_header += "Content-Length: %d\r\n" % len(response_body)
                response_header += "\r\n"
                response_data = response_header.encode() + response_body
                should_send_len = len(response_data)
                had_send_len = 0
                while had_send_len < should_send_len:  # send()函数会返回发送长度值
                    had_send_len += client_socket.send(response_data[had_send_len:])

                client_socket.close()

        else:   # 以.html结尾的动态路径请求
            env = {"file_name": path_info}
            print("动态请求路径", path_info)
            # 调用app对象call函数返回响应体
            response_body = self.app(env, self.handle_response_header)
            response_data = self.response_header.encode() + response_body
            client_socket.send(response_data)
            print("---------here1--------")
            client_socket.close()

    def handle_response_header(self, status, header_list):
        """将app对象传过来的(状态,头信息表)加工,合成响应头"""
        response_header = "HTTP/1.1 %s\r\n" % status
        for key, value in header_list:
            response_header += "%s: %s\r\n" % (key, value)
        self.response_header = response_header + "\r\n"


def main():
    """控制web服务器整体"""
    # python3 web_server.py 7878 web_app:app
    if len(sys.argv) == 3 and sys.argv[1].isdigit() and ":" in sys.argv[2]:
        # 1.获取 port,模块名,应用名
        port = int(sys.argv[1])
        ret = re.match(r"([^:]*):(.*)",sys.argv[2])
        web_frame_module = ret.group(1)
        app_name = ret.group(2)

        # 导入模块前,添加web_app对应路径
        print(sys.path)  # 打印系统模块导入的路径列表
        # 将路径添加到系统路径表
        sys.path.append(document_dynamic)
        print(sys.path)

        # 2.导入模块,应用
        frame_module = __import__(web_frame_module)
        app = getattr(frame_module, app_name)
        print(sys.argv)

        # 3.启动http服务器
        http_server = WSGIServer(port, app)
        http_server.run_forever()

    else:
        print("python3 web_server.py 7878 web_app:app")


if __name__ == '__main__':
    main()

