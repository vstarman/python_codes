import multiprocessing, time


def show(title, name, age):
    for i in range(10):

        print(i, "   %s;  %s;  %d" % (title, name, age))
        time.sleep(0.1)

if __name__ == '__main__':
    # 创建进程，参数以元祖，字典传参（注意字典中key名要和参数名一样）
    sub_process = multiprocessing.Process(target=show, args=("hello",), kwargs={"name": "Samuel", "age": 25})
    # 守护主进程，同生共死
    sub_process.daemon = True
    # 执行进程
    sub_process.start()

    # time.sleep(0.5)
    # print("over")
    time.sleep(0.5)
    # sub_process.terminate()   # 不管任务是否完成，立即终止子进程
    print("over")
    exit()

    # sub_process.join()    # 是否等待子进程执行结束，或等待多少秒
    # print("over")

pool.apply_async()