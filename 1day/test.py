# 倒入模块
import socket
import time

# 创建socket
num = input("please choose num(1.online 2.offline 3.Quit):")
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
while True:
    if num == 1:
        send_msg = ":online"
        send_content = "1:"+str(int(time.time()))+":Samuel:FiguerPro:"+str(num)+send_msg
        udp_socket.sendto(send_content.encode("gbk"), ("255.255.255.255", 2425))
        print(send_content)
    elif num == 2:
        send_msg = ":offline"
        send_content = "1:"+str(int(time.time()))+":Samuel:FiguerPro:"+str(num)+send_msg
        udp_socket.sendto(send_content.encode("gbk"), ("255.255.255.255", 2425))
    elif num == 0:
        exit()
