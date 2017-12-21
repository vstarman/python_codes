import socket
import threading
import feiq_constant
import feiq_send
import feiq_recv

# 功能选项
def menu():
    print("    飞秋 v6.58")
    print("1:发送上线提醒")
    print("2:发送下线提醒")
    print("3:指定ip发送消息")
    print("4:显示所有在线用户")
    print("0:退出系统")
    print("-"*40)
    return input("请输入功能选项：")


# 创建套接字
def creat_udp_socket():
    feiq_constant.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    #feiq_constant.udp_socket.bind(("", feiq_constant.feiq_port))

    # 设置允许广播
    feiq_constant.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# 显示所有用户列表
def print_all_online_users():
    for info in feiq_constant.user_list:
        print(info)


# 定义main函数
def main():
    # 构建socket
    creat_udp_socket()
    # 加入线程，上线自动收消息
    recv_thread = threading.Thread(target=feiq_recv.recv_msg)
    # 守护主线程，与主线程同生共死
    recv_thread.setDaemon(True)
    recv_thread.start()

    # 循环系统
    while 1:
        # 功能选项打印即捕获输入
        num = menu()
        # 群发消息
        if num == "00":
            feiq_send.send_allip_msg()
        # 上线提醒
        if num == "1":
            feiq_send.send_online_msg()
        # 下线提醒
        if num == "2":
            feiq_send.send_offline_msg()
        # 指定ip发送消息
        if num == "3":
            feiq_send.send_ip_msg()
        # 群发消息
        if num == "4":
            print_all_online_users()
        # 退出系统
        if num == "0":
            feiq_send.send_offline_msg()
            # 关闭套接字
            feiq_constant.udp_socket.close()
            print("系统已退出...")
            break


if __name__ == "__main__":
    main()