import time, multiprocessing
import os


def work1():
    for i in range(10):
        print("------1子进程:", multiprocessing.current_process().pid)
        # 获取父进程pid
        print("------2子进程:", os.getppid())
        time.sleep(0.5)

if __name__ == '__main__':
    w1_process = multiprocessing.Process(target=work1)
    w1_process.start()

    while 1:
        print("主进程:", multiprocessing.current_process().pid)
        time.sleep(0.5)


