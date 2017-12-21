import feiq_constant
import time
import main_feiq
import os


def build_msg(command, message=feiq_constant.message):
    msg = ("%d:%d:%s:%s:%d:%s" % (feiq_constant.feiq_version, int(time.time()),
                                  feiq_constant.user_name, feiq_constant.host_name,
                                  command, message)).encode("gbk")
    return msg


def build_send(msg, ip=feiq_constant.broadcast_ip):
    feiq_constant.udp_socket.sendto(msg, (ip, feiq_constant.feiq_port))


def send_online_msg():
    msg = build_msg(feiq_constant.IPMSG_BR_ENTRY)
    build_send(msg)


def send_offline_msg():
    msg = build_msg(feiq_constant.IPMSG_BR_EXIT)
    build_send(msg)


def send_ip_msg():
    main_feiq.show_online_friends()
    index = int(input("Please input your friend number:"))
    ip = feiq_constant.online_friends[index]["ip"]
    message = input("Please input the message:")
    msg = build_msg(feiq_constant.IPMSG_SENDMSG, message)
    build_send(msg, ip)


def send_file():
    main_feiq.show_online_friends()
    index = int(input("Please input your friend number:"))
    ip = feiq_constant.online_friends[index]["ip"]
    file_name = input("Please input file name:")
    if ip and file_name:
        # 版本号: 包编号:用户名: 主机名:命令字: 消息\0
        # 文件序号: 文件名:文件大小: 文件修改时间:文件类型:
        # 获取文件大小
        file_size = os.path.getsize(file_name)
        # 获取文件修改时间
        file_chage_time = int(os.path.getctime(file_name))
        # 文件选项内容
        file_option = "0:%s:%x:%x:%x:" % (file_name, file_size, file_chage_time, feiq_constant.IPMSG_FILE_REGULAR)
        # 拼接\0 区分消息和文件选项内容
        file_option = "\0" + file_option
        # 生成发送文件消息
        send_file_msg = build_msg(feiq_constant.IPMSG_SENDMSG | feiq_constant.IPMSG_FILEATTACHOPT, file_option)
        # 发送文件消息
        build_send(send_file_msg, ip)

        # 创建字典封装发送文件信息
        send_file_dict = dict()
        send_file_dict["package_ip"] = feiq_constant.package_id
        send_file_dict["file_index"] = 0
        send_file_dict["file_name"] = file_name

        feiq_constant.file_queue.put(send_file_dict)