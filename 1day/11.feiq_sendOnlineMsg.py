import socket
import time

# 定义全局变量
udp_socket = None
# feiQ版本
feiq_version = 1
# user name
user_name = "基地组织"
# host name
host_name = "From March"
# 发送广播地址
broad_ip = "255.255.255.255"
# feiQ端口号
feiq_port = 2425
# feiQ command
ipmsg_enter = 0x00000001  # 上线
ipmsg_exit = 0x00000002   # 下线


# 创建socket
def creat_socket():
    global udp_socket
    # 创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 设置允许广播(1,运行当前广播，2，广播选项，3，是否开启广播)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

# 发送上线提醒
def send_online_msg():
    # 1:123456789:itcast-python:localhost:32:hello
    # 飞秋的版本号：包编号：用户名：命令字：消息选项
    send_msg = "%d:%d:%s:%s:%d:%s" % (feiq_version, int(time.time()), user_name, host_name, ipmsg_enter, user_name)
    # 发送上线消息
    udp_socket.sendto(send_msg.encode("gbk"), (broad_ip, feiq_port))
    print(send_msg)

# 发送下线提醒
def send_offline_msg():
    # 1:123456789:itcast-python:localhost:32:hello
    # 飞秋的版本号：包编号：用户名：命令字：消息选项
    send_msg = "%d:%d:%s:%s:%d:%s" % (feiq_version, int(time.time()), user_name, host_name, ipmsg_exit, user_name)
    # 发送上线消息
    udp_socket.sendto(send_msg.encode("gbk"), (broad_ip, feiq_port))

# 打印飞鸽传书选项
def show_menu():
    print("       飞鸽传书")
    print("1.上线")
    print("2.下线")
    print("0.退出")
    return input("请输入操作选项：")


if __name__ == "__main__":
    # creat socket
    creat_socket()
    while True:
        menu = show_menu()
        if menu == "1":
            send_online_msg()
        elif menu == "2":
            send_offline_msg()
        elif menu == "0":
            exit()
    # 关闭socket
    udp_socket.close()

