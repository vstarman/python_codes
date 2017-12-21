"""飞秋常量数据模块"""

udp_socket = None
online_friends = list()  # 保存在线用户列
file_queue = None
package_id = None        # 包编号


feiq_version = 1
user_name = "To be or not to be"
host_name = "Sirius"
message = "Sirius"
broadcast_ip = "255.255.255.255"
feiq_port = 2425

# all command
IPMSG_BR_ENTRY = 0x00000001
IPMSG_BR_EXIT = 0x00000002
IPMSG_ANSENTRY = 0x00000003  # 通报在线
IPMSG_SENDMSG = 0x00000020   # 发送消息
IPMSG_RECVMSG = 0x00000021  # 收消息确认

# option for all command
IPMSG_FILEATTACHOPT = 0x00200000  # 文件消息  # -------添加---------

# file types for fileattach command
IPMSG_FILE_REGULAR = 0x00000001  # 普通文件  # -------添加---------
