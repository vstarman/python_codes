import feiq_constant
import time
import feiq_main

def build_msg(command, massage=feiq_constant.massage):
    """构建发送信息包"""
    #  # 1:1500816649:dongge-test:mac-pro:1:dongge-test
    msg = "%d:%d:%s:%s:%d:%s" % (feiq_constant.feiq_verson, int(time.time()), feiq_constant.user_name, feiq_constant.host_name, command, massage)
    return msg


def build_send(msg, ip=feiq_constant.broadcast_ip):
    feiq_constant.udp_socket.sendto(msg.encode("gbk"), (ip, feiq_constant.feiq_port))


def send_online_msg():
    msg = build_msg(feiq_constant.IPMSG_BR_ENTRY)
    # 发送上线广播
    build_send(msg)


def send_offline_msg():
    msg = build_msg(feiq_constant.IPMSG_BR_EXIT)
    # 发送下线广播
    build_send(msg)


def send_ip_msg():
    feiq_main.print_onlin_users()
    try:
        num = int(input("请输入用户序号："))
        massage = input("请输入要发送的讯息：")
        ip = feiq_constant.online_list[num]["ip"]
    except:
        print("序号输入有误，请重新输入")
        msg = build_msg(feiq_constant.IPMSG_SENDMSG, massage)
        # 发送massage
        build_send(msg, ip)


def send_recv_back_msg(ip):
    msg = build_msg(feiq_constant.IPMSG_RECVMSG)
    # 发送收到回应
    build_send(msg, ip)


# 发送文件
def send
