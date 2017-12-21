# from collections import Iterable, Iterator
#
# class Mylist:
#     def __init__(self):
#         self.items = list()
#
#     def append_item(self, item):
#         self.items.append(item)
#
#     def __iter__(self):
#         myIterator = MyIterator(self.items)
#         return myIterator
#
# class MyIterator:
#     def __init__(self, items):
#         self.items = items
#         self.current_index = 0
#         result = isinstance(self, Iterator)
#         print("MyIterator是否是可迭代对象:",result)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current_index < len(self.items):
#             self.current_index += 1
#             return self.items[self.current_index - 1]
#         else:
#             raise StopIteration
# mylist = Mylist()
# mylist.append_item("pig")
# mylist.append_item("dog")
# print("mylist是否可迭代:",isinstance(mylist, Iterable))
# for i in mylist:
#     print(i)

# def test1():
#     print("------test1-1-------")
#     print(num)
#     print("------test1-2-------")
#
# def test2():
#     print("------test2-1-------")
#     test1()
#     print("------test2-2-------")
#
# def test3():
#     try:
#         print("------test3-1-------")
#         test2()
#         print("------test3-2-------")
#     except Exception as result:
#         print("捕获到异常,信息:%s"%result)
#         print("------test3-3-------")
#
# test3()
# print("------华丽的分割线-------")
# test2()
# 定义迭代器,完成斐波那契数列
# class Fibnacci():
#     def __init__(self, num):
#         # 记录输入过来的数字,生成对应的数据
#         self.num = num
#         self.a = 0
#         self.b = 1
#         # 当前迭代次数的索引
#         self.current_index = 0
#
#     # 如果外加使用iter函数会调用__iter__方法
#     def __iter__(self):
#         return self
#     # 如果外加使用next函数会调用__next__方法
#     def __next__(self):
#         if self.current_index < self.num:
#             result = self.a
#             self.a, self.b = self.b, self.a+self.b
#             self.current_index += 1
#             return result
#         else:
#             raise StopIteration
#     def __setitem__(self, key, value):
#
# f = Fibnacci(980)
# for i in f:
#     print(i)
#
# def fib(num):
#     a = 0
#     b = 1
#     current_index = 0
#     while current_index < num:
#         result = a
#         a, b = b , a+b
#         current_index += 1
#         c = yield result
#         print(c)
#
# result = fib(20)
# #print(result)
# # for i in result:
# #     print(next(result))
#
# # while 1:
# #     try:
# #         print(next(result))
# #     except StopIteration as e:
# #         print(e.value)
# #         break
# print(result.send(None))
# print(result.send("hello"))
import time

# def w1():
#     for i in range(5):
#         print("-----1------",i)
#         yield
# def w2():
#     for i in range(5):
#         print("-----2------",i)
#         yield
#
# w1 = w1()
# w2 = w2()
#
# while w1:
#     try:
#         next(w1)
#         next(w2)
#     except StopIteration as e:
#         print(e.value)
#         break

# from greenlet import greenlet
# import time
#
# def work1():
#     for i in range(5):
#         print("work1-------:",i)
#         g2.switch()
# def work2():
#     for i in range(5):
#         print("work2-------:",i)
#         g1.switch()
# g1 = greenlet(work1)
# g2 = greenlet(work2)
# g1.switch()

# import gevent
# from gevent import monkey
# monkey.patch_all()
#
# def work1():
#     for i in range(5):
#         # gevent.getcurrent() 获取当前协程
#         print("w1------:", i, gevent.getcurrent())
#         gevent.sleep(0.5)
#
# def work2():
#     for i in range(5):
#         # gevent.getcurrent() 获取当前协程
#         print("w2------:", i, gevent.getcurrent())
#         # 使用gevent的耗时操作完成协程直接的自动切换
#         gevent.sleep(0.5)
#
# g1 = gevent.spawn(work1)
# g2 = gevent.spawn(work2)
# g1.join()
# g2.join()

import urllib.request
import gevent

def download_image(image_url, image_name):
    # 此处有耗时
    response = urllib.request.urlopen(image_url)
    print(gevent.getcurrent())
    image_data = response.read()
    with open(image_name, "wb") as file:
        file.write(image_data)
image_url1 = ""
image_url2 = ""
image_url3 = ""

gevent.joinall([
    gevent.spawn(download_image, image_url1, "1.jpg"),
    gevent.spawn(download_image, image_url2, "2.jpg"),
    gevent.spawn(download_image, image_url3, "3.jpg")
])