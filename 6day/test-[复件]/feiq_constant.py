
# 初始化套接字
udp_socket = None
online_list = list()

feiq_verson = 1
user_name = "Eva Piroska"
host_name = "Eva Piroska"
massage = "Eva Piroska?"
broadcast_ip = "255.255.255.255"
feiq_port = 2425  # 飞鸽传书的端口

# feiq command
IPMSG_BR_ENTRY = 0x00000001
IPMSG_BR_EXIT = 0x00000002
IPMSG_ANSENTRY = 0x00000003  # 通报在线
IPMSG_SENDMSG = 0x00000020   # 发送消息
IPMSG_RECVMSG = 0x00000021  # 收消息确认
