import socket, re


def handle_client(client_socket):
    recv_data = client_socket.recv(1024).decode()
    #print(recv_data)  # test
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

    if path_info == "/":
        path_info = g_document_root + "/index.html"
    else:
        path_info = g_document_root + path_info
    print(path_info)

    try:
        f = open(path_info, "rb")
    except IOError or FileNotFoundError as e:
        response_headers = "HTTP/1.1 404 not found\r\n\r\n"  # 200 找到资源
        response_boody = ">>>>>>>>Sorry, file not found>>>>>>>>>".encode()
        print(e)
    else:
        # 组织响应头
        response_headers = "HTTP/1.1 200 OK\r\n\r\n"  # 200 找到资源
        # 组织响应体
        response_boody = f.read()
    finally:

        response = response_headers.encode() + response_boody
        client_socket.send(response)
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 允许在7788端⼝资源没有彻底释放完毕时，可以重复绑定7788端⼝
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("", 7788))
    server_socket.listen(128)
    while True:
        client_socket, client_addr = server_socket.accept()
        handle_client(client_socket)

# 配置服务器资源
g_document_root = "./html"

if __name__ == '__main__':
    main()
