
'''# tcp客户端建立
import socket
# 创建
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "192.168.93.47"
port = 8080
# 与特定ip,服务端建立连接
tcp_client_socket.connect((ip,port))
# 发送消息
while True:
    send_msg = input("要发送的消息:")
    tcp_client_socket.send((send_msg+"\n").encode("gbk"))
    if send_msg == "0":
        break
    # 接受消息
    recv_data = tcp_client_socket.recv(1024).decode("gbk")
    print("收到来自服务端消息:", recv_data)'''

# tcp服务端建立
import socket
# creat
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# bind
tcp_server_socket.bind(("",6789))
# listen
tcp_server_socket.listen(128)
# accept,creat_service_socket
tcp_service, addr = tcp_server_socket.accept()
while True:
    recv_data = tcp_service.recv(1024).decode("gbk")
    print(addr,"收到来自客户端的消息",recv_data)
    send_msg = input("发送消息:")
    tcp_service.send(send_msg.encode("gbk"))