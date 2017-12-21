# import re
#
# y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
#
# ret = re.search("\w+@\w+\.com", y)
# print(ret.group())
#
import time


def A():
    while True:
        print("--------1------")
        yield
        time.sleep(0.5)


def B(c):
    while True:
        print("--------2------")
        c.next()
        time.sleep(0.5)


a = A()
B(a)
