import multiprocessing, time

# 全局变量
lst = list()

def add_lst():
    for i in range(5):
        lst.append(i)
        time.sleep(0.1)
    print("add 添加完成：", lst)


def read_lst():
    print("read 进程读取全局变量：", lst)


if __name__ == '__main__':
    w_process = multiprocessing.Process(target=add_lst)
    w2_process = multiprocessing.Process(target=add_lst())
    print(id(w_process),id(w2_process))
    r_process = multiprocessing.Process(target=read_lst)

    w_process.start()
    # 等待写入进程结束后再读取数据
    w_process.join()

    r_process.start()