udp_socket = None
user_list = []

feiq_version = "1"  # 飞秋版本
feiq_user_name = "Eva Piroska"  # 飞秋用户名
feiq_host_name = "Eva Piroska"  # 飞秋主机名
feiq_msg = "Eva Piroska"  # 昵称&发送的消息
broadcast_ip = "255.255.255.255"  # 广播ip
feiq_port = 2425  # 飞秋端口

IPMSG_BR_ENTRY = 0x00000001  # 上线命令
IPMSG_BR_EXIT = 0x00000002   # 下线命令
IPMSG_SENDMSG = 0x00000020   # 发送单个消息
IPMSG_ANSENTRY = 0x00000003  # 表示 通报在线
IPMSG_RECVMSG = 0x00000021   # 告知对方,已收到消息
