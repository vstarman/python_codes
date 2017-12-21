import feiq_constant
import feiq_send

def deal_recv_data():
    data, addr = feiq_constant.udp_socket.recvfrom(1024)
    msg_data = data.decode("gbk")
    msg_str_list = msg_data.split(":", 5)
    data_dict = dict()
    data_dict["user_name"] = msg_str_list[2]
    data_dict["massage"] = msg_str_list[5]
    data_dict["command_str"] = msg_str_list[4]
    data_dict["ip"] = addr[0]
    #print(msg_data)
    return data_dict


def deal_commade(command_str):
    """处理接收到的command选项"""
    command = int(command_str) & 0x000000ff
    command_option = int(command_str) & 0xffffff00
    return command, command_option


def add_online_list(user_name, ip):
    # 判断用户是否在列表，然后添加
    for i in feiq_constant.online_list:
        if ip == i["ip"]:
            break
    else:
        user_info = dict()
        user_info["user_name"] = user_name
        user_info["ip"] = ip
        feiq_constant.online_list.append(user_info)


def del_offline_list(ip):
    for i in feiq_constant.online_list:
        if ip == i["ip"]:
            feiq_constant.online_list.remove(i)
            break


def recv_msg():
    while 1:
        data_dict = deal_recv_data()
        command, command_option = deal_commade(data_dict["command_str"])
        if command == feiq_constant.IPMSG_BR_ENTRY:
            print("%s上线" % data_dict["user_name"])
            add_online_list(data_dict["user_name"], data_dict["ip"])  # 添加用户到列表

        elif command == feiq_constant.IPMSG_BR_EXIT:
            print("%s下线" % data_dict["user_name"])
            del_offline_list(data_dict["ip"])  # 删除用户到列表

        elif command == feiq_constant.IPMSG_ANSENTRY:
            print("%s已在线" % data_dict["user_name"])
            add_online_list(data_dict["user_name"], data_dict["ip"])  # 添加用户到列表

        elif command == feiq_constant.IPMSG_SENDMSG:
            print("来自%s的消息:%s" % (data_dict["user_name"], data_dict["massage"]))
            feiq_send.send_recv_back_msg(data_dict["ip"])
