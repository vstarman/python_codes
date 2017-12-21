#coding=utf-8
from socket import *
import time


# Save newClientInfo
g_socket_list = list()


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(("", 8080))
    # 将套接字设置位非阻塞
    # 非阻塞状态,accept时无客户connect,会报错
    server_socket.setblocking(False)

    while True:
        time.sleep(0.5)   # for test
        try:
            newClientInfo = server_socket.accept()
        except Exception as e:
            print("Error is :", e)
        else:
            print("One client is coming :%s" % str(newClientInfo))
            newClientInfo[0].setblocking(False)  # 将单客户服务端设为非阻塞
            g_socket_list.append(newClientInfo)

        for client_socket, client_addr in g_socket_list:
            try:
                recvData = client_socket.recv(1024)
                if recvData:
                    print("Recv [%s] :%s" % (str(client_addr), recvData))
                else:
                    print("[%s] socket was closed." % str(client_addr))
                    client_socket.close()
                    g_socket_list.remove((client_socket, client_addr))
            except Exception as result:
                print("Error2 is:",result)
        print(g_socket_list)

if __name__ == '__main__':
    main()



