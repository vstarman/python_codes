from socket import *
import threading,re


def handle_client(client_socket, client_addr):
    request_str = client_socket.recv(4096).decode()
    # 以行切割为列表
    request_list = request_str.split("\r\n")
    # print(request_list)  # 测试

    # 客户端请求报文分解
    '''GET /index.html?k=v&ks=v2 HTTP/1.1
    ['GET / HTTP/1.1', 'Host: 192.168.93.95:8080', 'Connection: keep-alive', 'Cache-Control: max-age=0', 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Upgrade-Insecure-Requests: 1', 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 'Accept-Encoding: gzip, deflate, sdch', 'Accept-Language: zh-CN,zh;q=0.8', '', '']
    '''
    request_line = request_list[0]
    # 正则切割获取请求资源路径
    result = re.search(r"\w+\s+([^ ]+)", request_line)
    # 如果匹配不成功,说明不是一个合法的http请求
    if not result:  # 如果为空
        client_socket.close()
        return

    # result.geoup(0)表示正则整体匹配
    path_info = result.group(1)
    print(path_info)   # ./index.html
    response_line = "HTTP/1.1 200 OK\r\n"  # 响应行

    # web服务器的默认规则 / == /index.html
    if path_info == "/":
        path_info = "/index.html"

    # 拼接响应报文
    '''
    HTTP/1.1 200 OK\r\n
    '''
    try:
        data_file = open("." + path_info, "rb")
    except FileNotFoundError or IOError as e:
        response_line = "HTTP/1.1 404 NOT FOUND\r\n"
        response_body = str(e).encode()
    else:
        file_data = data_file.read()
        data_file.close()
        response_body = file_data

    finally:
        response_header = "Server: Python ,I'm Flying...\r\n"
        #
        response_data = (response_line + response_header + "\r\n").encode() + response_body
        client_socket.send(response_data)
        client_socket.close()


def main():
    # 创建套接字
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 回收端口,允许立即使用上次绑定的端口
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(("", 8080))


    server_socket.listen(128)

    while True:
        client_socket, client_addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client,args=(client_socket,client_addr))
        # run()也能运行,但不会创建线程,start()可以创建线程和运行
        client_thread.setDaemon(1)
        client_thread.start()

if __name__ == '__main__':
    main()