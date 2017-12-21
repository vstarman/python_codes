import gevent
import time
from gevent import monkey

# mokey代码要最先执行
# 猴子补丁含义:是默认阻塞的程序代码,变到非阻塞(协程切环基础)
# 补丁的含义就是＂破解＂代码，改成非阻塞代码
# 给所有耗时操作打补丁,用于给gevent之间携程自动切换
monkey.patch_all()

def w1():
    for i in range(5):
        print(">>>>>w1:",i,gevent.getcurrent())
        time.sleep(0.3)
        # 使用gevent的耗时操作.完成对协程的自动切换
        #gevent.sleep(0.3)

def w2():
    for i in range(5):
        print(">>>>>w2:",i,gevent.getcurrent())
        time.sleep(0.3)
        #gevent.sleep(0.3)

# 使用gevent执行任务
g1 = gevent.spawn(w1)
g2 = gevent.spawn(w2)

# 等待协程执行完
g1.join()
g2.join()
