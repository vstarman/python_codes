import socket
import threading
import feiq_constant
import feiq_send
import feiq_recv


def menu():
    print("-" * 50)
    print("   飞秋 v3.58")
    print("1:上线")
    print("2:下线")
    print("3:向指定ip发送消息")
    print("4:打印在线成员列表")
    print("0:退出")
    print("-" * 50)


def creat_socket():
    """创建套接字:internet进程通信，SOCK_DGRAM udp协议流式套接字"""
    feiq_constant.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    feiq_constant.udp_socket.bind(("", feiq_constant.feiq_port))
    # 允许广播
    feiq_constant.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


def print_onlin_users():
    print("=" * 50)
    for i, user_info in enumerate(feiq_constant.online_list):
        print(i, user_info)
    print("=" * 50)


def main():
    creat_socket()
    recv_thread = threading.Thread(target=feiq_recv.recv_msg)
    # 开启线程守护，同生共死
    recv_thread.setDaemon(1)
    recv_thread.start()
    while 1:
        menu()
        num = input("请输入操作序号：")
        if num == "1":
            feiq_send.send_online_msg()
        elif num == "2":
            feiq_send.send_offline_msg()
        elif num == "3":
            feiq_send.send_ip_msg()
        elif num == "4":
            print_onlin_users()
        elif num == "0":
            feiq_send.send_offline_msg()
            feiq_constant.udp_socket.close()
            break


if __name__ == '__main__':
    main()

