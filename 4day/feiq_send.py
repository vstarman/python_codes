import feiq_constant
import time

# 默认全局发送地址
goal_addr = (feiq_constant.broadcast_ip, feiq_constant.feiq_port)


def build_msg(command_num, option_data=""):
    """抽取公共代码"""
    send_msg = "%s:%d:%s:%s:%d:%s" % (
        feiq_constant.feiq_version, int(time.time()), feiq_constant.feiq_user_name,
        feiq_constant.feiq_host_name, command_num, option_data)

    return send_msg


def build_send(send_msg, addr=goal_addr):
    # 发送
    feiq_constant.udp_socket.sendto(send_msg.encode("gbk"), addr)


# 发送上线提醒
def send_online_msg():
    send_msg = build_msg(feiq_constant.IPMSG_BR_ENTRY)
    # 发送
    build_send(send_msg)


# 发送下线提醒
def send_offline_msg():
    send_msg = build_msg(feiq_constant.IPMSG_BR_EXIT)
    # 发送
    build_send(send_msg)


# 群发消息
def send_allip_msg():
    for i in range(5):
        time.sleep(1)
        print(">> ", end="")
    print("隐藏功能开启:群发消息")
    send_content = input("请输入发送内容：")
    send_msg = build_msg(feiq_constant.IPMSG_SENDMSG, send_content)
    # 发送
    build_send(send_msg, goal_addr)
    if send_content == "00":
        for _ in range(5):
            print(">> ", end="")
            time.sleep(0.5)
        print("二级隐藏功能开启:循环群发消息")
        send_content1 = input("请输入发送内容：")
        while send_content1 != "00":
            send_msg = build_msg(feiq_constant.IPMSG_SENDMSG, send_content)
            # 发送
            build_send(send_msg, goal_addr)
        if send_content1 == "00":
            for _ in range(7):
                time.sleep(0.5)
                print(">> ", end="")
            print("三级隐藏功能开启:程序员的礼物")
            for _ in range(10):
                time.sleep(0.5)
                print(">> ", end="")
            for i in range(1, 10):
                for j in range(1, i+1):
                    print("%d*%d=%d\t" % (j, i, i*j), end="")
                    time.sleep(0.5)
                time.sleep(0.5)
                print()
            time.sleep(2)
            print("尽情背诵...")


# 给指定ip发消息
def send_ip_msg():
    send_ip = input("请输入目标ip：")
    send_content = input("请输入发送内容：")
    send_msg = build_msg(feiq_constant.IPMSG_SENDMSG, send_content)
    # 目标地址,重新赋值
    goal_addr = (send_ip, feiq_constant.feiq_port)
    # 发送
    build_send(send_msg, goal_addr)


def send_Iam_online(goal_addr):
    # 通报对方，我已在线
    answer_msg = build_msg(feiq_constant.IPMSG_ANSENTRY)
    build_send(answer_msg, goal_addr)


def send_recv_back_msg(goal_addr):
    # 给对方发送消息确认
    recv_back_msg = build_msg(feiq_constant.IPMSG_RECVMSG)
    build_send(recv_back_msg, (goal_addr[0], feiq_constant.feiq_port))