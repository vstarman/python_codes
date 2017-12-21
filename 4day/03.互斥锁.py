import threading

num = 0


# 创建互斥锁
lock = threading.Lock()


# work1 num + 100 times
def work1(number):
    # 上锁
    lock.acquire()
    global num
    for i in range(number):
        num += 1
    print("work1 num=", num)
    # 释放锁
    lock.release()


# work1 num + 100 times
def work2(number):
    # 上锁
    lock.acquire()
    global num
    for i in range(number):
        num += 1
    print("work2 num=", num)
    # 释放锁
    lock.release()


if __name__ == "__main__":
    # 创建线程，传参要元祖（1000000,）
    work1_thread = threading.Thread(target=work1, args=(1000000,))
    work2_thread = threading.Thread(target=work2, args=(1000000,))

    work1_thread.start()
    # join一个线程执行完，另一个线程再执行
    #work1_thread.join()
    work2_thread.start()
