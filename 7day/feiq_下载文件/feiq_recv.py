import feiq_constant
import feiq_send


def deal_recv_data(recv_data):
    recv_data = recv_data.decode("gbk", errors="ignore")
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
            # 判断接收的消息是普通消息还是文件消息
            if command_option & 0x00f00000 == feiq_constant.IPMSG_FILEATTACHOPT:
                print("收到文件消息")
                print(recv_data)
                # 保存下载文件信息
                download_file_dict = dict()
                download_file_dict["package_id"] = int(data_dict["packet_id"])
                # 获取文件选项信息
                download_file_option = data_dict["message"]
                # 获取"\0"位置
                index = download_file_option.find("\0")
                file_option_str = download_file_option[index+1:]
                #print(file_option_str)
                # 切割字符串
                file_option_list = file_option_str.split(":", 5)
                # 文件序号
                download_file_dict["file_index"] = int(file_option_list[0])
                download_file_dict["file_name"] = file_option_list[1]
                download_file_dict["file_size"] = int(file_option_list[2], 16)  # 转成16进制
                # 目的ip
                download_file_dict["ip"] = recv_addr[0]
                feiq_constant.download_file_list.append(download_file_dict)
                print(download_file_dict)


            else:
                print('收到%s的新消息:%s' % (data_dict["user_name"], data_dict["message"]))
            # 消息确认回复
            recv_msg_back = feiq_send.build_msg(feiq_constant.IPMSG_RECVMSG)
            feiq_send.build_send(recv_msg_back, recv_addr[0])



