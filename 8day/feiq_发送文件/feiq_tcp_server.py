# 发送文件和下载文件模块
import socket
import feiq_constant
import threading
import feiq_recv  # 导入处理接收信息模块用来处理接收到的文件消息

# 用列表保存发送的文件消息
send_file_list = list()


def deal_file_option(file_option):
    # 59c7a345:0:0:  处理文件选项信息
    # 切割文件选项,返回列表
    file_option_list = file_option.split(":", 3)
    # 创建接收文件信息字典,保存接受的的文件下载请求信息选项
    recv_file_dict = dict()
    # 文件包编号
    # 将收到的16进制包编号和序号转为10进制
    recv_file_dict["package_id"] = int(file_option_list[0], 16)
    # 文件序号
    recv_file_dict["file_index"] = int(file_option_list[1], 16)
    return recv_file_dict


def recv_client_data(tcp_service):
    # 接收客户端发送文件请求信息
    # 1_lbt80_0#131200#28E3475C0E3E#3380#43820#0#4000#9:1506259596:Administrator:2ZX58O463BS7FN4:96:59c772a4:0:0:
    # 59c772a4:0:0:,文件包编号:文件序号:从那下载(断点续传)
    recv_data = tcp_service.recv(1024)
    # 调用feiq_recv模块处理接收到的消息
    recv_dict = feiq_recv.deal_recv_data(recv_data)
    # 处理接收到的文件选项信息
    recv_file_dict = deal_file_option(recv_dict["message"])
    # 遍历发送的文件消息列表,将收到的文件消息请求与之前发送的文件消息匹配
    for send_file_dict in send_file_list:
        if (send_file_dict["package_id"] == recv_file_dict["package_id"] and
                send_file_dict["file_index"] == recv_file_dict["file_index"]):
            # 获取文件名
            file_name = send_file_dict["file_name"]
            # 找到文件名,打开文件,传输数据给请求文件的客户端
            file = open(file_name, "rb")
            # 为防止传输出现错误,使用try捕获异常
            # try:
            #     for i in file.readlines():
            #         tcp_service.send(i)
            #     file.close()
            # except Exception as e:
            #     print("发送文件出现异常:", e)
            # else:
            #     print("%s文件发送成功!" % file_name)
            # break

            try:
                while True:
                    send_data = file.read(1024)
                    if send_data:  # 文件发送为空自动跳出循环
                        tcp_service.send(send_data)
                        # 数据要以二进制格式传输,所以文件打开方式使用二进制
                    else:
                        break
                file.close()
            except Exception as e:
                print("发送文件出现异常:", e)
            else:
                print("%s文件发送成功!" % file_name)
            break


    # 关闭客户端socket
    tcp_service.close()


def recv_queue_data(file_queue):
    # 循环接收队列里的文件信息
    while True:
        # 将队列里发送的文件消息,保存到列表
        send_file_list.append(file_queue.get())  # 在tcp主进程里接收信息,会阻塞主进程,所以建立子线程接收


def tcp_main(file_queue):  # 接收主进程里,接收的文件信息字典,通过queue取出
    # 创建子线程获取队列中的文件消息
    queue_thread = threading.Thread(target=recv_queue_data, args=(file_queue,))
    queue_thread.start()

    # 创建tcp_socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    tcp_server_socket.bind(("", feiq_constant.feiq_port))
    # 开启监听莫斯
    tcp_server_socket.listen(128)
    # 创建客服与客户端一对一链接
    while True:
        tcp_service, addr = tcp_server_socket.accept()
        # 创建线程分别与客服链接
        recv_thread = threading.Thread(target=recv_client_data, args=(tcp_service,))
        recv_thread.start()
    # 关闭被动套接字
    tcp_server_socket.close()