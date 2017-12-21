import socket
import threading
import multiprocessing
import feiq_constant
import feiq_send
import feiq_recv
import feiq_tcp_server


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
    # 创建队列接收文件信息,将队列传入tcp,保存发送的文件消息
    feiq_constant.file_queue = multiprocessing.Queue()

    # 创建tcp子进程(1.等待tcp客户端建立连接;2发送文件内容给tcp客户端)
    # 将队列传tcp服务端,用来从queue中获取发送的文件消息
    # tcp_service.accept会阻塞主进程,所以建立子进程来接收客户端请求
    tcp_process = multiprocessing.Process(target=feiq_tcp_server.tcp_main, args=(feiq_constant.file_queue,))
    # 开启进程守护
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













