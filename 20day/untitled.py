# class Mylist(object):
# 	def __init__(self):
# 		self.container = []
# 	def add(self, item):
# 		self.container.append(item)
# 	def __iter__(self):
# 		pass

# mylist = Mylist()
# from collections import Iterable
# print(isinstance(mylist, Iterable))

import gevent

def f(n):
	for i in range(n):
		print(gevent.get_current(), )



import re

y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'

ret = re.findall("^\w+@\w+\.com$", y)


import socket
socket.socket(SOL)