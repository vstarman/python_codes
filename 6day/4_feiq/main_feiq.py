import socket
import threading
from multiprocessing import Queue, Process
import feiq_constant
import feiq_send
import feiq_recv
import feiq_file_tcp


def create_udp_socket():
    feiq_constant.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 广播(1.表示运行当前socket开启广播,2.表示广播选项,3.表示是否开启广播)
    feiq_constant.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # 绑定
    feiq_constant.udp_socket.bind(("", feiq_constant.feiq_port))


def show_online_friends():
    print("="*50)
    num = 0
    for friend_info in feiq_constant.online_friends:
        print(num, "-->", friend_info)
        num += 1
    print("=" * 50)


# 打印功能提示
def print_menu():
    print("-" * 50)
    print("    Dimple v3.57")
    print("1: Online")
    print("2: Offline")
    print("3: Send message")
    print("4: Send file")
    print("5: Show all friends")
    print("0: Quit")
    print("-" * 50)
    num = input("Please input number:")
    return num


def main():
    # 创建文件消息队列
    feiq_constant.file_queue = Queue()
    tcp_process = Process(target=feiq_file_tcp.tcp_main, args=(feiq_constant.file_queue, ))
    tcp_process.daemon = True
    tcp_process.start()

    # 循环接收消息线程
    create_udp_socket()
    recv_thread = threading.Thread(target=feiq_recv.recv_msg)
    # 线程守护
    recv_thread.setDaemon(True)
    recv_thread.start()

    while True:
        num = print_menu()
        if num == "1":
            feiq_send.send_online_msg()
        if num == "2":
            feiq_send.send_offline_msg()
        if num == "3":
            feiq_send.send_ip_msg()
        if num == "4":
            feiq_send.send_file()
        if num == "5":
            show_online_friends()
        if num == "0":
            feiq_send.send_offline_msg()
            # close udp_socket
            feiq_constant.udp_socket.close()
            exit()

if __name__ == '__main__':
    main()













