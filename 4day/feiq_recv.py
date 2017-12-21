import feiq_constant
import feiq_send


def deal_recv_data(recv_data):
    # 解码消息,errors="ignore",忽略不能解码的信息
    recv_str = recv_data.decode("gbk", errors="ignore")
    # ":"切割解码后的字符串,返回列表
    data_list = recv_str.split(":", 5)
    # 列表转字典
    data_dict = {}
    data_dict["version"] = data_list[0]
    data_dict["package_num"] = data_list[1]
    data_dict["user_name"] = data_list[2]
    data_dict["host_name"] = data_list[3]
    data_dict["command"] = data_list[4]
    data_dict["massage"] = data_list[5]
    return data_dict


def deal_command_option_num(command_num):
    """提取命令中的字体以及选项"""
    command = int(command_num) & 0x000000ff
    command_option = int(command_num) & 0xffffff00
    return command, command_option


def judge_online_add(user_name, goal_ip):
    """判断用户是否在列表中，没有则添加进列表"""
    for info in feiq_constant.user_list:
        if info["goal_ip"] == goal_ip:
            break

    else:
        online_user = {}
        online_user["goal_ip"] = goal_ip
        online_user["user_name"] = user_name
        feiq_constant.user_list.append(online_user)


def judge_offline_del(goal_ip):
    """用户下线，删除"""
    for info in feiq_constant.user_list:
        if info["goal_ip"] == goal_ip:
            feiq_constant.user_list.remove(info)
            break


# 接收消息
def recv_msg():
    while 1:
        recv_data, goal_addr = feiq_constant.udp_socket.recvfrom(1024)
        data_dict = deal_recv_data(recv_data)
        command, command_option = deal_command_option_num(data_dict["command"])
        #print(data_dict)
        if command == feiq_constant.IPMSG_BR_ENTRY:
            # 用户上线
            print("%s上线" % data_dict["massage"])

            # 添加用户到列表
            user_name = data_dict["user_name"]
            judge_online_add(user_name, goal_addr[0])
            # 通报对方，我已在线
            feiq_send.send_Iam_online(goal_addr)

        if command == feiq_constant.IPMSG_BR_EXIT:
            # 用户下线
            print("%s下线" % data_dict["user_name"])
            # 删除下线用户
            judge_offline_del(goal_addr[0])

        if command == feiq_constant.IPMSG_ANSENTRY:
            # 用户已在线
            print("%s已在线" % data_dict["user_name"])
            # 查询是否在列表中
            judge_online_add(data_dict["user_name"], goal_addr[0])

        if command == feiq_constant.IPMSG_SENDMSG:
            # 接收新消息
            print("收到%s的新消息：%s" % (data_dict["user_name"], data_dict["massage"]))

            # 给对方发送消息确认
            feiq_send.send_recv_back_msg(goal_addr)


