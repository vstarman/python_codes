from socket import *
import threading,re


def handle_client(client_socket):
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
    get_file_name = (re.search(r"\w+\s+([^ ]+)", request_list[0])).group(1)
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
        response_data = (response_line + response_headers).encode() + response_body
        client_socket.send(response_data)
        client_socket.close()

def main():
    # 创建
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 收回端口
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定
    server_socket.bind(("", 8080))
    # 监听
    server_socket.listen(128)

    while True:
        client_socket, client_addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.setDaemon(1)
        client_thread.start()

if __name__ == '__main__':
    main()

