import socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.93.40", 8080))
# 设置成非阻塞
sock.setblocking(False)
while True:
    time.sleep(1)
    # 默认情况下 网络IO就是阻塞的通信模式
    # 操作系统会将该线程挂起 知道有数据的时候恢复
    # 新建 - 就绪ready - 执行running - 阻塞block
    # 就绪态: 完事具备  只差cpu资源
    # 阻塞态: 等待某个时间或数据到达
    # 阻塞的通信模式 效率低下 需要来回切换三个状态

    # 非阻塞就是没有数据到来,会抛出一个异常
    try:
        recv_data = sock.recv(1024)
    # except 后边异常类型尽量写成具体异常类型,不然会匹配异常类型耗费资源
    except Exception as e:
        print("暂时没数据到达...")
    else:
        print("Receive message:", recv_data)
