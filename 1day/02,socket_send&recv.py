# upd 客户端socket
from socket import *

# 接受客户端数据
dest_ip = input("请输入对方ip：")

while 1:
    if __name__ == "__main__":
        # 创建socket
        upd_client_socket = socket(AF_INET, SOCK_DGRAM)
        send_content = input("请输入要发送的内容：")
        # 对字符串编码
        send_data = send_content.encode("gbk")
        # 收发数据
        if send_content == "q":
            # 关闭socket
            upd_client_socket.close()
            break
        if dest_ip and send_content:
            # 发送数据
            upd_client_socket.sendto(send_data, (dest_ip, 8080))  #无法发送到飞秋，需要广播
            # 接收数据
            recv_data, ipport = upd_client_socket.recvfrom(1024)
            # 解码数据
            recv_content = recv_data.decode("gbk")
            print(recv_content, ipport)

