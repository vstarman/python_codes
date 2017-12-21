import threading, time


class MyThread(threading.Thread):
    def run(self):
        for i in range(30):
            time.sleep(1)
            msg = "I'm "+self.name+' @ '+str(i)
            print(msg)


def test():
    for i in range(1000):
        t = MyThread()
        t.start()
if __name__ == '__main__':
    test()
