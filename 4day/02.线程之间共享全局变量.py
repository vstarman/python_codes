import threading, time

num = 0

# work1 num + 100 times
def work1(number):
    global num
    for i in range(number):
        num += 1
        time.sleep(0.01)
    print("work1 num=",num)

# work1 num + 100 times
def work2(number):
    global num
    for i in range(number):
        num += 1
        time.sleep(0.01)
    print("work2 num=", num)


if __name__ == "__main__":
    work1_thread = threading.Thread(target=work1, args=(100,))
    work1_thread.daemon = True
    work2_thread = threading.Thread(target=work2, args=(100,))

    work1_thread.start()
    # ｊｏｉｎ一个线程执行完，另一个线程再执行
    #work1_thread.join()
    work2_thread.start()
    exit()
