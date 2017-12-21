import multiprocessing, time, os


# 复制
def copy_msg():
    print("copping ....")
    print("当前进程编号....", os.getpid())
    time.sleep(0.1)


if __name__ == '__main__':
    # 创建进程池 ---> 处理批量重复操作
    # 3:进程池中最大有三个进程
    pool = multiprocessing.Pool(3)

    for i in range(10):
        # 异步执行，不等待任务执行完
        # 第一个参数表示进程执行的函数名，后面为参数
        pool.apply_async(copy_msg, (i,))

    # 主线程不等待你的任务执行完成

    # 等待进程池执行完
    pool.join()

    # 关闭任务池
    pool.close()