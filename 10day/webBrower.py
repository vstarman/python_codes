from socket import *

# 创建tcp链接
tcp_socket = socket(AF_INET, SOCK_STREAM)
# 建立和web服务器的连接
tcp_socket.connect(('192.168.43.122',8080))

# 发送http请求报文
request_line = "GET /index.html HTTP/1.1\r\n"
request_header = "Host: 127.0.0.1\r\n"
request_data = request_line + request_header + "\r\n"

tcp_socket.send(request_data.encode())

# 收报文
response_data = tcp_socket.recv(4096)
print("recv data :",response_data)

# 响应数据
# 响应数据以字符串形式
response_data_str = response_data.decode()
index = response_data_str.find("\r\n\r\n") + 4

#４个字符\r\n\r\n,前两个来自最后一个响应头数据
print(response_data_str[index:])
tcp_socket.close()