# greelet 对协程进行了封装,更容易的完成切换,需手动开启
from greenlet import greenlet
import time
def w1():
    for i in range(5):
        print(">>>>>w1:",i)
        time.sleep(0.3)
        # 切换到w1执行
        g2.switch()

def w2():
    for i in range(5):
        print(">>>>>w2:",i)
        time.sleep(0.3)
        # 切换到w1执行
        g1.switch()


g1 = greenlet(w1)
g2 = greenlet(w2)

# 启动greenlet协程
g1.switch()