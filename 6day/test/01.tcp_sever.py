import socket, threading


def recv_data(server_client_socket):
    while True:
        # 5.收发消息
        recv_data = server_client_socket.recv(1024)
        if recv_data:
            print("接受客户端的数据:", recv_data.decode("gbk"))
            server_client_socket.send("你的请求已收到,正在处理中...".encode("gbk"))
            # 终止对链接客户服务
        else:
            print("结束对客户服务")
            server_client_socket.close()
            break

if __name__ == '__main__':
    # 1.创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 立刻收回端口
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # "",表示绑定本机任一ip地址,6789端口号
    # 2.绑定端口
    tcp_server_socket.bind(("", 6789))

    # 3.设置响铃模式,监听模式
    # 128:等待服务端接收的最大连接数
    # tcp_sever_socket主动套接字,变成被动,也就是不能等待被接收用户的连接
    tcp_server_socket.listen(128)

    while True:
        # 4.等待客户端的链接,来一个客户找一个客服服务这个客户,10086客服
        server_client_socket, ip_port = tcp_server_socket.accept()
        print(server_client_socket)

        # 开辟线程
        recv_thread = threading.Thread(target=recv_data, args=(server_client_socket,))
        recv_thread.setDaemon(True)
        recv_thread.start()


    # 6.关闭socket(可选)
    # 好比机构关门,不接受新连接,已建立链接的客户还要服务
    tcp_server_socket.close()


