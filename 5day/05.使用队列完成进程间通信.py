import multiprocessing,time


def write(queue):
    for i in range(10):
        if queue.full():   # full（）判断队列满了没有
            print("队列满了")
            break
        else:
            queue.put(i)
            time.sleep(0.1)


def read(queue):
    while 1:
        if queue.empty():   # empty（）判断队列空了没有
            print("队列空了")
            break
        print(queue.get())


if __name__ == '__main__':
    # 创建两个进程
    queue = multiprocessing.Queue(10)
    # 创建两个进程
    write_process = multiprocessing.Process(target=write, args=(queue, ))
    read_process = multiprocessing.Process(target=read, args=(queue, ))

    write_process.start()
    read_process.start()
