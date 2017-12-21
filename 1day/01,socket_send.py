import socket

# 定义全局变量
udp_socket = None


# 创建socket
def creat_socket():
    global udp_socket
    # 创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 创建上线提醒
def send_online_msg():
    # 1:123456789:itcast-python:localhost:32:hello
    # 飞秋的版本号：包编号：用户名：命令字：消息选项
    send_msg = "1:123456789:基地组织:localhost:32:基地组织给你邮递了个包裹，请取一下.."
    # 发送上线消息
    udp_socket.sendto(send_msg.encode("gbk"), ("192.168.93.24", 2425))

if __name__ == "__main__":
    # creat socket
    creat_socket()
    # send online message
    send_online_msg()
    # close socket
    udp_socket.close()


