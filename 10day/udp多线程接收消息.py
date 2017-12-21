from socket import *
import threading

def recv_msg():
    while True:
        recv_data, addr = udp_socket.recvfrom(1024)
        print(addr, recv_data.decode("gbk"))
        if addr not in addr_list:
            addr_list.append(addr)

def show_menu():
    print("-" * 50)
    print("  优优聊天室 v3.58")
    print("1: 发送消息")
    print("2: 跳过")
    print("-" * 50)
    num = input("请输入回复消息:")
    return num

def show_all_user():
    print("=" * 50)
    for i, j in enumerate(addr_list):
        print(i, "\t", j)
    print("=" * 50)

def send_msg():
    show_all_user()
    try:
        index = int(input("请输入好友序号(Q退出):"))
        while 1:
            msg = input("请输入发送的信息:")
            if msg == "q" or msg == "Q":
                break
            else:
                send_msg = "\n 来自徐伟的消息:" + msg
                udp_socket.sendto(send_msg.encode("gbk"), addr_list[index])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 创建socket
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.getsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    udp_socket.bind(("", 2426))

    # 保存地址信息变量
    addr_list = list()
    # 开启接收线程
    recv_thread = threading.Thread(target=recv_msg)
    recv_thread.setDaemon(1)
    recv_thread.start()
    while True:
        try:
            num = show_menu()
            if num == "1":
                send_msg()
            else:
                break
        except Exception as e:
            print(e)

