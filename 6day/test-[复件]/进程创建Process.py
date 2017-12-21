from multiprocessing import Process
import os
import time


def r1():
    print("son process pid:%s" % os.getpid())
    print("son process was ended")

if __name__ == '__main__':
    print("father process pid:%s" % os.getpid())
    p = Process(target=r1)
    p.start()