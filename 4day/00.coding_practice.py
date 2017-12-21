'''
# 用互斥锁解决上面题目出现的num不是200万的问题
import threading,time
num = 0
def a(number):
    global num
    for i in range(number):
        mulexa.acquire()
        num += 1
        mulexa.release()
        time.sleep(0.5)
        print("----a----",num)
def b(number):
    global num
    for i in range(number):
        mulexb.acquire()
        num += 1
        mulexb.release()
        time.sleep(0.5)
        print("----b----",num)

mulexa = threading.Lock()
mulexb = threading.Lock()

if __name__ == '__main__':
    a_thread = threading.Thread(target=a,args=(1000000,))
    b_thread = threading.Thread(target=b,args=(1000000,))
    a_thread.start()
    b_thread.start()

# 创建1个子线程，让子线程每隔1秒钟打印1个数字，数字从1开始一直到10，即1.2.3......10

import threading, time

def a():
    for i in range(1, 11):
        print(i)
        time.sleep(1)
if __name__ == '__main__':
    a_thread = threading.Thread(target=a)
    a_thread.start()

'''

# 什么进程？
# 进程是程序用到的资源+代码的总称,它是操作系统分配资源的基本单位.

# 线程和进程有什么不同？
#区别:
# 1,线程执行开销小,不利于资源的管理和保护;而进程正相反
# 2,不同进程直接运行,某一进程挂了,其他进程互不影响;同一进程内多线程运行,某一线程挂了,其他所有线程都一起挂
# 3,同一进程里线程间共享资源;进程间不共享资源,创建新进程,相当于在内存里重新开辟一个副本
# 4,线程间共享资源,添加线程不一定需要再加资源,但是只要开辟进程就需要系统分配资源

# 多进程用来做什么？
# 用来执行多任务,

# 父进程和子进程的执行顺序确定么？
# 父进程和子进程是无序的

# 多进程会共享全局变量？
# 不会

# 同步是什么意思？怎样理解？
# 同步是指线程,进程一起配合,某一线程的执行需要其他线程执行后返回的结果,这就称之为同步

# 队列是什么？
# 队列是一种先进先出的数据表结构类似于一个管道

# 程序和进程有什么区别？
# 程序是代码和资源的集合体,它是静态的;进程是运行程序的一次执行,它是动态的
# 程序是永存的;进程是暂时性的,是程序在数据集上的一次执行,有创建有撤销,存在是暂时的
# 进程具有并发性,而程序没有
# 进程是竞争计算机资源的基本单位,程序不是
# 进程和程序不是一一对应的,一个程序可以对应多个进程;而一个进程只对应一个程序

# 子进程和父进程是什么？
# 父进程是指执行任务时,为防止线程出现因算法错误等原因,破坏进程内的数据,一般会在进程内创建一个子进程处理这些数据,从而就确保了父进程中与子进程无关的数据

# getpid、getppid的作用是什么？
#

# 创建出来的多个子进程，同时对一个相同名字的全局变量操作时会出错么？为什么？


# 创建出来的子进程和父进程到底是谁先执行？为什么？


# multiprocessing模块的目的是什么？


# 怎样用multiprocessing模块中的Process创建一个子进程？请写出基本代码


# multiprocessing模块中的Process创建了一个子进程后，怎样让子进程开始执行？


# 什么是进程池？有什么用？


# 为了完成多个任务一起执行，可以创建多个子进程来执行任务，那么为什么还要进程池呢？
# 什么是进程间通信？
# 为什么需要进程间通信？
# multiprocessing模块中Queue怎样发送、取出数据？





