import select, socket, time


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("", 8888))
    server_socket.listen(128)
    server_socket.setblocking(False)

    client_socket_list = list()
    while True:
        try:
            client_socket, client_addr = server_socket.accept()
        except Exception as e:
            print("暂时没有客户端链接，再等等...")
            time.sleep(2)
        else:
            client_socket.setblocking(False)
            client_socket_list.append((client_socket, client_addr))
            print("接收到来自%s的链接请求..." % str(client_addr))
        finally:
            for client_socket, client_addr in client_socket_list:
                try:
                    recv_data = client_socket.recv(1024)
                except Exception as e:
                    pass
                else:
                    if recv_data:
                        print("%s>>>>>>:" % str(client_addr), recv_data)
                    else:
                        print("%s已断开..." % str(client_addr))
                        client_socket.close()
                        client_socket_list.remove((client_socket, client_addr))


if __name__ == '__main__':
    main()