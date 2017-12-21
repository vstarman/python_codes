import time
import threading

# 全局变量
mylist = []

# work1
def work1():
    for i in range(5):
        mylist.append(i)
        time.sleep(0.5)

def work2():
    print(mylist)


if __name__ == "__main__":
    work1_thread = threading.Thread(target=work1)
    work1_thread.start()

    # 等待２秒
    time.sleep(2)
    # work1().join()

    work2_thread = threading.Thread(target=work2)
    work2_thread.start()

