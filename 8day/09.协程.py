import time
# 携程可以在单线程完成多任务


def w1():
    for i in range(5):
        print("----1----",i)
        yield


def w2():
    for i in range(5):
        print("----2----",i)
        yield

if __name__ == '__main__':
    w1 = w1()
    w2 = w2()
    try:
        while True:
            next(w1)
            next(w2)
    except Exception as e:
        print(e)



