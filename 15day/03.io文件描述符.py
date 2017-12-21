# 文件描述符
#       只是本进程内部对 文件资源 描述的一个符号
#       获取socket的文件描述符 socket_obj.fileno()
# 向操作系统中添加自己感兴趣的　socketd的fd(文件描述符) 和事件类型
#       在epoll中默认的通知模式是
#       LT 水平触发 当事件/数据到达时 会一直通知直到没有数据
#       ET 边沿触发 当事件到达时 只通知一次
#       当收到2048个字节时 用户只接收了100字节
#       LT 一直通知
#       ET 只通知一次 --------> 需要一次读完
# epoll.poll()
#       从操作系统中监听所有套接字 挑选出有事件到达的socket
#       翻译一个列表 元素是元祖形式 (fd, enents)
#       从操作系统中监听所有套接字
#       从操作系统中监听所有套接字
"""import socket
#　非阻塞服务端
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(client_socket.fileno())

client_socket.connect(("192.168.93.40", 8888))
#client_socket.setblocking(False)
print(client_socket.fileno())
while True:
    try:
        recv_data = client_socket.recv(1024)
    except Exception as e:
        print("暂时没有数据到达...", e)
    else:
        print(recv_data)"""

import socket, time
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