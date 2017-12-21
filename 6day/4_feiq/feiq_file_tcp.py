import socket
import feiq_constant
import threading
import feiq_recv

# 保存发送文件的信息列表
send_file_list = list()


def recv_queue_data(file_queue):
    """1024bite每次获取文件信息"""
    while True:
        # 获取信息
        file_info_dict = file_queue.get()
        send_file_list.append(file_info_dict)


def deal_file_info(message):
    """处理文件message信息"""
    # 切割文件选项信息
    file_info_list = message.split(":", 3)
    # 封装字典
    file_info_dict = dict()
    # 获取包编号
    file_info_dict["package_id"] = int(file_info_list[0], 16)
    # 获取文件序号
    file_info_dict["file_index"] = int(file_info_list[1])
    return file_info_dict


def recv_client_data(service_client_socket):
    """线程客服 获取客户请求"""
    # 接收客户端发送文件的请求信息
    recv_data = service_client_socket.recv(1024)
    # 处理接受用户请求要发送的文件信息
    data_dict = feiq_recv.deal_recv_data(recv_data)
    print(data_dict["message"])
    # 处理请求选项信息
    file_info_dict = deal_file_info(data_dict["message"])
    # 遍历发送文件的列表,找到用户请求发送的文件信息
    for file_info in send_file_list:
        if (file_info["package_id"] == file_info_dict["package_id"] and
            file_info["file_index"] == file_info_dict["file_index"]):
            # 获取文件名
            file_name = file_info["file_name"]

            try:
                file = open(file_name, "rb")
                while True:
                    recv_file_data = file.read(1024)
                    if recv_file_data:
                        service_client_socket.send(recv_file_data)
                    else:
                        break
                file.close()
            except Exception as e:
                print("Error from senf file:",e)
            else:
                print("%s send succeed.")
            break


def tcp_main(file_queue):
    """tcp 服务端入口"""
    # 创建线程接收文件队列里面的文件信息数据
    queue_thread = threading.Thread(target=recv_queue_data, args=(file_queue,))
    queue_thread.start()

    # 创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind
    tcp_server_socket.bind(("", feiq_constant.feiq_port))
    # 设置监听模式,薅猴毛变猴子
    tcp_server_socket.listen(128)
    while True:
        # 接收客户端链接
        service_client_socket, ip_port = tcp_server_socket.accept()
        # 创建线程连上客户端
        recv_thread = threading.Thread(target=recv_client_data, args=(service_client_socket, ))
        recv_thread.start()
    # 关闭被动套接字
    tcp_server_socket.close()








