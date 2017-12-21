import socket, time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.connect(("", 8080))
server_socket.listen(128)
# 设置成非阻塞
server_socket.setblocking(False)
while True:
    try:
        client_socket, client_addr = server_socket.accept()
    except Exception as e:
        pass
    else:
        print("一个新客户端来到:", str(client_addr))
