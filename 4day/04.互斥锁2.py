import threading

num = 0


# 创建互斥锁
lock = threading.Lock()


# work1 num + 100 times
def work1(number):
    global num
    for i in range(number):
        # 上锁
        lock.acquire()
        # 核心代码上锁
        num += 1
        # 释放锁
        lock.release()
    print("work1 num=", num)


# work1 num + 100 times
def work2(number):
    global num
    for i in range(number):
        # 上锁
        lock.acquire()
        num += 1
        # 释放锁
        lock.release()
    print("work2 num=", num)



if __name__ == "__main__":
    # 创建线程，传参要元祖（1000000,）
    work1_thread = threading.Thread(target=work1, args=(1000000,))
    work2_thread = threading.Thread(target=work2, args=(1000000,))

    work1_thread.start()
    work2_thread.start()
