import threading, time

'''
def saySorry():
    print("I am sorry,baby")
    time.sleep(0.1)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start()
    print("-------end------")



def sing():
    for i in range(3):
        print("I am sing......",i)
        time.sleep(1)

def dance():
    for i in range(3):
        print(".....I am dance",i)
        time.sleep(1)

if __name__ == '__main__':
    print("------begin-----",time.ctime())

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    print("------end--------")
    # time.sleep(5)
    # print("--------end-------",time.ctime())

    while True:
        length = len(threading.enumerate())
        print("Thread num right now:",length)
        if length <= 1:
            break

        time.sleep(0.5)

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            # name属性当中保存的是当前线程的名字
            msg = "I'm " + self.name + " @ " + str(i)  # name属性当中保存的是当前线程的名字
            print(msg)

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
     test()





class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm "+self.name+' @ '+str(i)
            print(msg)
def test():
    for i in range(5):
        t = MyThread()
        t.start()
if __name__ == '__main__':
    test()
'''


class A(threading.Thread):
    def run(self):
        if mutexA.acquire():
            #print(mutexA.acquire())
            print(self.name, "------do1----up---")
            time.sleep(1)

            if mutexB.acquire():
                print(self.name,"------do1----down---")
                mutexB.release()
            mutexA.release()


class B(threading.Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name, "------do2----up---")
            time.sleep(1)

            if mutexA.acquire():
                print(self.name, "------do2----down---")
                mutexA.release()
            mutexB.release()


mutexA = threading.Lock()
mutexB = threading.Lock()

if __name__ == '__main__':
    t1 = A()
    t2 = B()

    t1.start()
    t2.start()


