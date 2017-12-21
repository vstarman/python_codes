import socket
import threading
import re

# 定义相对目录初始格式
WWW_ROOT_PATH = "."

def handle_client(client_socket, client_addr):
    # 解析http请求报文格式,解析用户请求数据
    print("开始为%s服务>>>>>" % str(client_addr))
    response_data = client_socket.recv(4096).decode()
    print(response_data)
    '''
    GET URL HTTP/1.1\r\n
    header1_name: header1_value\r\n
    \r\n
    '''
    # 正则切割response_data
    data_list = response_data.split("\r\n")
    print(data_list)
    # 第0行就是请求行数据
    result = re.search(r"^\w+\s+([^ ]+)", data_list[0])
    print(result)
    if not result:
        # 报文格式解析出错
        client_socket.close()
        return
    # 报文匹配成功
    print("find index: %s" % result.group(1))
    # /favicon.ico 是一个网站的缩略图 是一个网站高识别度的标识
    # 用户请求的url资源名称 ./index.html
    file_name = result.group(1)
    if file_name == "/":
        file_name = "/index.html"
    response_header = "Server:PythonWebServer2.0\r\n"
    try:
        data_file = open(WWW_ROOT_PATH + file_name, "rb")
    except (FileNotFoundError, IOError) as e:
        response_line = "HTTP/1.1 404 Not Found\r\n"
        response_body = str(e).encode()
    else:
        # 构造响应行数据
        response_line = "HTTP/1.1 200 OK\r\n"
        # 响应头数据 隐患 文件大 响应慢
        # 当使用rb读取文件时 read返回数据就是bytes
        response_body = data_file.read()
    finally:
        response_data = (response_line + response_header + "\r\n").encode() + response_body
        # 把响应数据回复给客户端
        client_socket.send(response_data)
        # 关闭套接字
        client_socket.close()


if __name__ == '__main__':
    # 创建socket服务器
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 快速收回端口
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server_socket.bind(("",8080))
    # 返回客户端套接字服务接收客户端请求
    server_socket.listen(128)
    while True:
        client_socket, client_addr = server_socket.accept()

        # 创建子线程为每个客户单独负责
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_addr))
        client_thread.start()

