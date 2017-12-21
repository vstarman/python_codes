from socket import *

def handle_client(client_socket):
    "为一个客户端进行服务"
    recv_data = client_socket.recv(1024).decode()
    print(recv_data)
    request_header_lines = recv_data.splitlines()
    for line in request_header_lines:
        print(line)

    # 组织响应 头信息(header)
    response_headers = "HTTP/1.1 200 OK\r\n"  # 200表示找到这个资源
    response_headers += "\r\n"     # 用一个空的行与body进行隔开

    # 组织 内容(body)
    response_body = "hello world"

    response = response_headers + response_body
    client_socket.send(response.encode())
    client_socket.close()


if __name__ == '__main__':
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 设置当前服务器先close,即服务器端4次挥手后资源可以立即释放,这样就保证了下次程序运行,能立即绑定端口
    server_socket.bind(("", 8080))
    server_socket.listen(128)
    while True:
        client_socket, client_addr = server_socket.accept()
        # 处理客户请求
        handle_client(client_socket)