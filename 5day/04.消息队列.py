import multiprocessing

if __name__ == '__main__':
    # 表示最多向队列里面分享三个消息
    queue = multiprocessing.Queue(3)
    # put可以放入任意类型
    queue.put("hello")
    queue.put("123")
    queue.put([2,3,4,5])
    # 如果消息队列满了，那么在放入数据一直等待队列中有空闲位置才能进入
    # 如果加上超时时间，到时队列还是满的，那么直接崩溃（原因：queue.Full）
    #queue.put((22,31,14), timeout = 1)
    print(queue)
    print(queue.get())
    print(queue.get())
    print(queue.get())
    # 如果队列为空，那么取值的时候一直等待队列有值才会获取
    # 可以设置timeout=time ，超市奔溃（原因：queue.Empty）
    # print(queue.get(timeout=1))


