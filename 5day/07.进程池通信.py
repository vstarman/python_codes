import multiprocessing, time


def write(queue):
    for i in range(10):
        queue.put(i)
        time.sleep(0.1)


def read(queue):
    while True:
        if queue.empty():
            break
        print(queue.get())




if __name__ == '__main__':
    # 不写数字，自动根据任务创建
    pool = multiprocessing.Pool(2)

    # 创建进程池的queue,队列不指定大小，那么可以没有限制
    queue = multiprocessing.Manager().Queue()
    # 使用进程池执行任务
    pool.apply_async(write, (queue, ))
    time.sleep(1)

    pool.apply_async(read, (queue, ))

    pool.close()

    # 等待进程池执行完
    pool.join()