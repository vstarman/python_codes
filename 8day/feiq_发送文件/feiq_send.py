import feiq_constant
import time
import main_feiq
import os


def build_msg(command, message=feiq_constant.message):
    feiq_constant.package_id = int(time.time())
    msg = ("%d:%d:%s:%s:%d:%s" % (feiq_constant.feiq_version, feiq_constant.package_id,
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
    # 输入好友序号
    try:
        index = int(input("Please enter friend number:"))
        ip = feiq_constant.online_friends[index]["ip"]
    except:
        print("Error: wrong number,please enter again...")
        return
    file_name = input("Please enter file name:")
    if ip and file_name:
        # 版本号: 包编号:用户名: 主机名:命令字: 消息\0
        # 文件序号: 文件名:文件大小: 文件修改时间:文件类型:
        # 获取文件大小
        file_size = os.path.getsize(file_name)
        file_change_time = int(os.path.getctime(file_name))
        # 文件信息编辑
        file_msg = "\0"+"0:%s:%x:%x:%x:" % (file_name, file_size,
            file_change_time,feiq_constant.IPMSG_FILE_REGULAR)
        # 生成发送文件的消息
        send_file_msg = build_msg(feiq_constant.IPMSG_SENDMSG|feiq_constant.IPMSG_FILEATTACHOPT, file_msg)
        # 发送文件消息
        build_send(send_file_msg, ip)
        # 创建字典封装发送的文件消息
        send_file_dict = dict()
        # 文件包编号
        send_file_dict["package_id"] = feiq_constant.package_id
        # 文件序号
        send_file_dict["file_index"] = 0
        # 文件名
        send_file_dict["file_name"] = file_name
        # 将文件信息放入到文件队列里
        feiq_constant.file_queue.put(send_file_dict)


