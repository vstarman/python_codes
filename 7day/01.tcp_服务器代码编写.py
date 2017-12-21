from socket import *
from multiprocessing import Process

"""tcp 单项联系"""
'''
# socket()-->bind()-->listen()-->accept()

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(("",6789))

tcp_server_socket.listen(128)

client_socket, client_addr = tcp_server_socket.accept()

recv_data = client_socket.recv(1024)

print("%s:%s" % (str(client_addr), recv_data))

client_socket.close()
tcp_server_socket.close()

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(("192.168.93.40", 6789)

client_socket.send("haha".encode("gbk"))
recv_data = client_socket.recv(1024)
print(recv_data.decode("gbk"))


def client_service(tcp_service_socket):
    tcp_service_socket.send("\n客服为您服务,有什么可以帮到您的呢?" .encode("gbk"))
    while True:
        recv_data = tcp_service_socket.recv(1024)
        # 接收消息为零,意味着客户端关闭了连接
        if len(recv_data) > 0:
            print("recv:", recv_data.decode("gbk"))
        else:
            break
        send_data = input("send:")
        tcp_service_socket.send(send_data)
    tcp_service_socket.close()


tcp_server_socket = socket(AF_INET, SOCK_STREAM)
tcp_server_socket.bind(("", 6789))
tcp_server_socket.listen(128)

while True:
    # 接收用户端请求,生成客服对接
    tcp_service_socket, client_addr = tcp_server_socket.accept()
    # 新客服循环接收客户信息
    p = Process(target=client_service, args=(tcp_service_socket,))
    p.start()

from socket import *
# server_socket:socket-->bind-->listen-->recv-->send
# client_socket:socket-->connect((ip,port))-->send-->recv

def deal_data():
    while 1:
        recv_data = tcp_client_socket.recv(1024)

        print('recv:',recv_data.decode("gbk"))

        send_data = input("send:")

        tcp_client_socket.send(('\n'+ send_data).encode("gbk"))

        if send_data == "0":
            tcp_client_socket.close()
            break
if __name__ == '__main__':

    tcp_client_socket = socket(AF_INET,SOCK_STREAM)

    connect_addr = ("192.168.93.40", 5678)

    tcp_client_socket.connect(connect_addr)
    tcp_client_socket.send("连接已建立..".encode("gbk"))

    deal_data()

import threading

num = 0
def add_1(number):
	for _ in range(number):
		global num
		num += 1
	print("result:",num)

def add_2(number):
	for _ in range(number):
		global num
		num += 1
	print("result:",num)

if __name__ == '__main__':
	add_1 = threading.Thread(target=add_1,args=(1000000,))
	add_2 = threading.Thread(target=add_2,args=(1000000,))
	add_1.start()
	add_2.start()


import socket,threading

def udp_A():
    udp_A = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_A.bind(("192.168.93.147", 6789))
    while 1:
        data, addr = udp_A.recvfrom(1024)
        print("接收到消息：",data.decode("gbk"))

def udp_B():
    udp_B = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_B.bind(("192.168.93.147",6788))
    while 1:
        msg = input("输入发送的消息：")
        udp_B.sendto(msg.encode("gbk"), ("192.168.93.147",6789))


if __name__ == '__main__':
        b = threading.Thread(target=udp_B)
        a = threading.Thread(target=udp_A)
        a.start()
        b.start()


import socket,threading
def deal_client_data(tcp_client_socket):
	while True:
		recv_data = tcp_client_socket.recv(1024)
		if len(recv_data) > 0:
			print("接收到信息：",recv_data.decode("gbk"))
			tcp_client_socket.send("已收到！谢谢！".encode("gbk"))
		else:
			break

if __name__ == '__main__':
	tcp_server_socket = socket.socket(socket.AF_INNET,socket.SOCK_STREAM)
	tcp_server_socket.bind("", 5678)
	tcp_server_socket.listen(128)
	while True:
		tcp_client_socket, client_addr = tcp_server_socket.accept()
		client_thread = threading.Thread(target=deal_client_data,args=(tcp_client_socket,))
		client_thread.start()

from multiprocessing import Process
import time
def print_num():
	for i in range(1,11):
		time.sleep(1)
		print(i)
if __name__ == '__main__':
	process1 = Process(target=print_num)
	process1.start()


import threading

num = 0
def add_1(number):
	global num
	for _ in range(number):
		if mutex1.acquire():
			num += 1
			mutex1.release()
	print("result:",num)

def add_2(number):
	global num
	for _ in range(number):
		if mutex1.acquire():
			num += 1
			mutex1.release()
	print("result:",num)

mutex1 = threading.Lock()
mutex2 = threading.Lock()

if __name__ == '__main__':
	add_1 = threading.Thread(target=add_1,args=(1000000,))
	add_2 = threading.Thread(target=add_2,args=(1000000,))
	add_1.start()
	add_2.start()

import threading, time, random

lock_1 = threading.Lock()
lock_2 = threading.Lock()
lock_3 = threading.Lock()
lock_4 = threading.Lock()
lock_5 = threading.Lock()

def pig_1():
    if lock_1.acquire():
        print("Pig 1 get 1 chopstick")
        if lock_2.acquire():
            print("Pig 1 eat it")
            lock_1.release()

def pig_2():
    if lock_2.acquire():
        print("Pig 2 get 1 chopstick")
        if lock_3.acquire():
            print("Pig 2 eat it")
            lock_2.release()


def pig_3():
    if lock_3.acquire():
        print("Pig 3 get 1 chopstick")
        if lock_4.acquire():
            print("Pig 3 eat it")
            lock_3.release()


def pig_4():
    if lock_4.acquire():
        print("Pig 4 get 1 chopstick")
        if lock_5.acquire():
            print("Pig 4 eat it")
            lock_4.release()


def pig_5():
    if lock_5.acquire():
        print("Pig 5 get 1 chopstick")
        if lock_1.acquire():
            print("Pig 5 eat it")
            lock_5.release()


if __name__ == '__main__':
    thread_1 = threading.Thread(target=pig_1)
    thread_2 = threading.Thread(target=pig_2)
    thread_3 = threading.Thread(target=pig_3)
    thread_4 = threading.Thread(target=pig_4)
    thread_5 = threading.Thread(target=pig_5)
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_5.start()

import threading, time, random

lock_1 = threading.Lock()
lock_2 = threading.Lock()
lock_3 = threading.Lock()
lock_4 = threading.Lock()
lock_5 = threading.Lock()

def pig_1():
    if lock_1.acquire():
        print("Pig 1 get 1 chopstick")
        if lock_2.acquire():
            print("Pig 1 eat it")
            lock_1.release()
            lock_2.release()
        else:
            lock_1.release()


def pig_2():
    if lock_2.acquire():
        print("Pig 2 get 1 chopstick")
        if lock_3.acquire():
            print("Pig 2 eat it")
            lock_2.release()
            lock_3.release()
        else:
            lock_2.release()


def pig_3():
    if lock_3.acquire():
        print("Pig 3 get 1 chopstick")
        if lock_4.acquire():
            print("Pig 3 eat it")
            lock_3.release()
            lock_4.release()
        else:
            lock_3.release()


def pig_4():
    if lock_4.acquire():
        print("Pig 4 get 1 chopstick")
        if lock_5.acquire():
            print("Pig 4 eat it")
            lock_4.release()
            lock_5.release()
        else:
            lock_4.release()


def pig_5():
    if lock_5.acquire():
        print("Pig 5 get 1 chopstick")
        if lock_1.acquire():
            print("Pig 5 eat it")
            lock_5.release()


if __name__ == '__main__':
    thread_1 = threading.Thread(target=pig_1)
    thread_2 = threading.Thread(target=pig_2)
    thread_3 = threading.Thread(target=pig_3)
    thread_4 = threading.Thread(target=pig_4)
    thread_5 = threading.Thread(target=pig_5)
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_5.start()'''

from socket import *
udp_socket = socket(AF_INET, SOCK_DGRAM)

