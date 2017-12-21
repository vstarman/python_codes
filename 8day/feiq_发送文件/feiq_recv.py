import feiq_constant
import feiq_send


def deal_recv_data(recv_data):
    recv_data = recv_data.decode("gbk")
    data_list = recv_data.split(":", 5)

    data_dict = dict()
    data_dict["version"] = data_list[0]
    data_dict["packet_id"] = data_list[1]
    data_dict["user_name"] = data_list[2]
    data_dict["host_name"] = data_list[3]
    data_dict["command_num"] = data_list[4]
    data_dict["message"] = data_list[5]
    return data_dict


def deal_command_option(command_num):
    """处理command命令和选项"""
    command = int(command_num) & 0x000000ff
    command_option = int(command_num) & 0xffffff00
    return command, command_option


def add_online_friend(user_name, ip):
    for friend_info in feiq_constant.online_friends:
        if ip == friend_info["ip"]:
            break
    else:
        friend_info = dict()
        friend_info["user_name"] = user_name
        friend_info["ip"] = ip
        feiq_constant.online_friends.append(friend_info)


def del_offline_friend(ip):
    for friend_info in feiq_constant.online_friends:
        if ip == friend_info["ip"]:
            feiq_constant.online_friends.remove(friend_info)
            break


def recv_msg():
    """接受消息"""
    while True:
        recv_data, recv_addr = feiq_constant.udp_socket.recvfrom(1024)
        data_dict = deal_recv_data(recv_data)
        command, command_option = deal_command_option(data_dict["command_num"])
        if command == feiq_constant.IPMSG_BR_ENTRY:  # 用户上线
            print('%s上线' % data_dict["message"])
            # 找名字
            index = data_dict["message"].find("\0")
            if index != -1:
                user_name = data_dict["message"][:index]
            else:
                user_name = data_dict["user_name"]
            add_online_friend(user_name, recv_addr[0])

            # 通报在线
            answer_online_msg = feiq_send.build_msg(feiq_constant.IPMSG_ANSENTRY)
            feiq_send.build_send(answer_online_msg, recv_addr[0])

        elif command == feiq_constant.IPMSG_BR_EXIT:   # 用户下线
            print('%s下线' % data_dict["user_name"])
            del_offline_friend(recv_addr[0])

        elif command == feiq_constant.IPMSG_ANSENTRY:   # 用户已在线
            print('%s已在线' % data_dict["message"])
            add_online_friend(data_dict["message"][:data_dict["message"].find("\0")], recv_addr[0])

        elif command == feiq_constant.IPMSG_SENDMSG:    # 收消息确认
            print('收到%s的新消息:%s' % (data_dict["user_name"], data_dict["message"]))
            # 消息确认回复
            recv_msg_back = feiq_send.build_msg(feiq_constant.IPMSG_RECVMSG)
            feiq_send.build_send(recv_msg_back, recv_addr[0])



