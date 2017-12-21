from multiprocessing import Pool
import random,os,time

'''def worker(num):
    for i in range(3):
        print(num, "--------pid = %d------" % os.getpid())
        time.sleep(0.3)

# 3表示进程池最多有3个进程一起执行
pool = Pool(3)

for i in range(0,10):
    print("=====%d====="%i)
    # 向进程池中添加任务
    # 注意:如果添加任务数量超过了 进程池中进程个数的话,那么不会导致添加不进去
    #      添加倒进车的任务 如果还没有被执行的话,那么此时 他们会等待进程池中的
    #      进程完成一个任务后,自动添加到刚刚那个进程 完成当前的新任务
    time.sleep(0.5)
    pool.apply_async(worker,(i,))

pool.close()  # 关闭进程池,不能再次添加新任务了
pool.join()   # 主进程 创建/添加 任务后,主进程默认不会等待进程池中的任务执行完后才结束,
              # 而是直接结束,所要想子进程任务执行完毕在结束,就要用join等待
'''

def worker(num):
    for i in range(3):
        print(num, "--------pid = %d------" % os.getpid())
        time.sleep(0.3)

# 3表示进程池最多有3个进程一起执行
pool = Pool(3)

for i in range(0,10):
    print("=====%d====="%i)
    pool.apply(worker,(i,))

pool.close()  # 关闭进程池,不能再次添加新任务了
pool.join()   # 主进程 创建/添加 任务后,主进程默认不会等待进程池中的任务执行完后才结束,
              # 而是直接结束,所要想子进程任务执行完毕在结束,就要用join等待














