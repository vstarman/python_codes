# 飞鸽传书模块
import socket

#　判断该模块是否是程序入口
if __name__ == "__main__":
    #　创建socket
    # 第一个参数：地址的类型
    # 第二个参数：数据的传输协议
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 允许当前的socket发送广播
    # 第一个参数表示运行当前的socket 开启广播
    # 第二个参数 广播选项
    # 第三个参数表示 是否开启广播
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    # 发送的数据
    send_content = "1:123456789:1:Mark:32:如果快乐你就拍拍手～嘿～嘿" # 1，上线，0下线，32发送消息
    #　发送消息
    udp_socket.sendto(send_content.encode("gbk"), ("255.255.255.255", 2425))
    # 关闭链接
    udp_socket.close()