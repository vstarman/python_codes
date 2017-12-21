
from socket import *


udp_socket = socket(AF_INET, SOCK_DGRAM)

dest_addr = ("192.168.23.132", 8080)

send_content = "在吗？"

udp_socket.sendto(send_content.encode("utf-8"), dest_addr)

udp_socket.close()

