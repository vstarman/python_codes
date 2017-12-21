# coding=utf-8
import socket

if __name__ == "__main__":

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,True)
    send_content = "1:123456789:What_the_huck!:localhost:32:come on ,baby!"
    udp_socket.sendto(send_content.encode("utf-8"),("255.255.255.255", 2425))
    udp_socket.close()


    #简笔画