import socket, time


if __name__ == '__main__':
    # creat tcp socket()
    # first:ip address type
    # secend:传输协议
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # conect() 和服务端socket建立连接
    tcp_socket.connect(("192.168.93.118", 6789))
    print("与服务端连接已建立...")
    while True:
        # recvfrom(),1024表示每次接收的最大字节
        recv_data = tcp_socket.recv(1024).decode("gbk")
        print("接收到服务端的数据：%s" % recv_data)
        # close()
        # recv_data.close()
        time.sleep(0.5)

    while True:
        msg = input("Send a massage with tcp:")
        # send(),已经建立好连接，不用ip sendto了
        tcp_socket.send(msg.encode("gbk"))


