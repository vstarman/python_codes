# upd 客户端socket
from socket import *


if __name__ == "__main__":
    # 创建udp客户端的socket
    # 第一个参数：地址的类型
    # 第二个参数：数据的传输协议
    upd_client_socket = socket(AF_INET, SOCK_DGRAM)
    # 绑定端口，提示：
    # ip地址为空，“”说明绑定本地任一电脑ip都行，防止多个网卡出现的多个ip的问题
    # 一般服务端socket会绑定端口号
    upd_client_socket.bind(("", 2314))

    send_content = "你好，我是客户端小白"
    upd_client_socket.sendto(send_content.encode("gbk"), ("192.168.93.24", 8080))

    #　接收用户发送的数据
    recv_data, ipport = upd_client_socket.recvfrom(1024)
    # 解码数据
    recv_content = recv_data.decode("gbk")
    print("接收数据：%s,%s"%(recv_content, ipport))
    # 发送给客户端
    upd_client_socket.sendto("您的问题已收到，现在程序员正在急速处理..".encode("gbk"), ipport)
    # 关闭服务器
    upd_client_socket.close()