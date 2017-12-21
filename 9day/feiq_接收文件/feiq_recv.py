import feiq_constant
import feiq_send
import feiq_tcp_server


def deal_recv_data(recv_data):
    recv_data = recv_data.decode("gbk")
    data_list = recv_data.split(":", 5)

    data_dict = dict()
    data_dict["version"] = data_list[0]
    data_dict["package_id"] = data_list[1]
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
            # 判断是普通消息还是文件消息,用按位与判断值是否是0x00200000(结果是0x00200100)
            if command_option & 0x00f00000 == feiq_constant.IPMSG_FILEATTACHOPT:
                # 收到的文件消息和ip打包,发送到队列,供tcp客户端connect使用
                # b'1_lbt80_0#131200#28E3475C0E3E#3380#43820#0#4000#9:1506330342:Administrator:2ZX58O463BS7FN4:2097440:
                # \x000:new_1.py:01f1:59bbf8db:1:\x07\x00'
                # 创建字典保存收到的文件消息
                download_file_dict = dict()
                print(data_dict["message"])
                download_file_dict["package_id"] = int(data_dict["package_id"])   # 原为字符串,要转成整形
                # 切割文件消息
                print(recv_data)
                print(recv_data.decode("gbk"))
                print(data_dict["message"])
                index = data_dict["message"].find["\0"]
                file_info_list = data_dict["message"][index+1:].split(":", 5)
                print(file_info_list)
                # 文件序号
                download_file_dict["file_index"] = file_info_list[0]
                download_file_dict["file_name"] = file_info_list[1]
                download_file_dict["file_size"] = int(file_info_list[2], 16)
                download_file_dict["ip"] = recv_addr[0]
                print(download_file_dict)



            else:
                print('收到%s的新消息:%s' % (data_dict["user_name"], data_dict["message"]))
            # 消息确认回复
            recv_msg_back = feiq_send.build_msg(feiq_constant.IPMSG_RECVMSG)
            feiq_send.build_send(recv_msg_back, recv_addr[0])



