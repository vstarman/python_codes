import threading

# 创建互斥锁
lock = threading.Lock()


def work(index):
    mylist = [11, 22, 33, 44, 55]
    lock.acquire()
    print(lock.acquire())

    if index >= len(mylist):
        print("下标越界")
        # 如果锁不释放，后面线程会一直等待，形成死锁
        lock.release()

        return
    print(mylist[index])
    lock.release()
    print(lock.release())

if __name__ == '__main__':
    for i in range(60):
        thread = threading.Thread(target=work, args=(i,))
        thread.start()


