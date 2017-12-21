import time
def use_time(func):
    def inner():
        a = time.time()
        func()
        b = time.time()
        print("use time:",b-a)
    return inner

def w1(func):
    def inner():
        time.sleep(1)
        print("inner-------w1")
        func()
        time.sleep(1)
        print("# 验证1\n# 验证2\n# 验证3")
    return inner
def w2(func):
    def inner():
        time.sleep(1)
        print("inner-------w2")
        func()
        time.sleep(1)
        print("# 验证4\n# 验证5\n# 验证6")
    return inner
@use_time
@w2
@w1
def f1():
    print('f1')
@w1
def f2():
    print('f2')
@w1
def f3():
    print('f3')
@w1
def f4():
    print('f4')

if __name__ == '__main__':
    f1()