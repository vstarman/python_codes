from multiprocessing import Process
import time, os

'''
def run():
    """The child process execution code"""
    while True:
        print("______2_____")
        time.sleep(0.1)


if __name__ == '__main__':
    p = Process(target=run)
    p.start()
    while True:
        print("......1........")
        time.sleep(0.1)



def run():
    """the chile process execution code"""
    # os.getpid() 获取当前进程号
    print("thr chile process in the operation:pid = %d" % os.getpid())
    time.sleep(2)
    print("the child process is going to end...")


if __name__ == '__main__':
    print("the father process pid = %d" % os.getpid())
    p = Process(target=run)
    p.start()
    p.join(timeout=1)
    print(p.is_alive())

# the father process pid = 7196
# thr chile process in the operation:pid = 7280
# the child process is going to end...


from multiprocessing import Queue
q = Queue(3)  # 初始化一个Queue对象,最多可接手三条put消息
q.put("massage1")
q.put("massage2")
print(q.full())  # false
q.put("massage3")
print(q.full())
try:
    q.put("massage4", True, 2)  # 第二参数,检测队列是否满了,如果是True,2秒后抛出异常
except:
    print("消息队列已满,现有消息数:%s"%q.qsize())

try:
    q.put_nowait("massage4")    # put_nowait() 不进行等待,满了就抛出异常
except:
    print("消息队列已满,现有消息数:%s" % q.qsize())

if not q.full():
    q.put("massage4")


if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())

print("现有消息数:%s" % q.qsize())
print()

from multiprocessing import Queue
q = Queue()
print(q)
for i in range(10):
    q.put("message:%d"% i)
    time.sleep(0.5)
    print(i,"-号信息已存入")
print(q.qsize())
for _ in range(10):
    print(q.get(2),"--取出")
    time.sleep(0.5)

from multiprocessing import Process
import time
def print_num():
    for i in range(10):
        print(i+1)
        time.sleep(1)

def main():
    p = Process(target=print_num)
    p.start()

if __name__ == '__main__':
    main()'''

# from multiprocessing import Queue, Process
# import time
# def parent_mission(que):
#     data = que.get()
#     print(data)
#
# def children_mission(que):
#     data = "hello"
#     que.put(data)
#
#
# def main():
#     q = Queue()
#     p = Process(target=children_mission, args=(q,))
#     p.start()
#     parent_mission(q)
#     p.join()
#
# if __name__ == '__main__':
#     main()

from multiprocessing import Process
import os
def file_copy(oldpath,newpath):
    old = open(oldpath,"rb")
    new = open(newpath,"wb")
    while new.write(old.read(1024)) == 1024:
        pass

def mul_file_copy(oldpathlist,newpathlist):
    if len(oldpathlist) != len(newpathlist):
        return
    for index,oldpath in enumerate(oldpathlist):
        print(oldpath+"开始复制"+newpathlist)
        file_copy(oldpath,newpathlist[index])
        print(oldpath+"复制到"+newpathlist[index]+"完成")

if __name__ == '__main__':
    filepath = "/user/lib/python3.5"
    oldpathlist = [filepath+"/"+i for i in os.listdir(filepath) if i.endswith(".py")]
    newpathlist = ["/home/python/Desktop/Test/"+i for i in os.listdir(filepath) if i.endswith(".py")]
    os.mkdir("/home/pythin/Desktop/Test")
    file_count = len(oldpathlist)

    oldpathlist1 = oldpathlist[:file_count//2]
    oldpathlist2 = oldpathlist[file_count//2:]

    newpathlist1 = newpathlist[:file_count // 2]
    newpathlist2 = newpathlist[file_count // 2:]


    p1 = Process(target=mul_file_copy,args=(oldpathlist1,newpathlist1))
    p2 = Process(target=mul_file_copy,args=(oldpathlist2,newpathlist2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


