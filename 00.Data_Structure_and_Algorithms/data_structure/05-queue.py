class Queue(object):
    """队列实现"""
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        """往队列中添加一个item元素"""
        return self.queue.insert(0, item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.queue.pop()

    def is_empty(self):
        """判断队列是否为空"""
        return self.queue == []

    def size(self):
        """返回队列的元素个数"""
        return len(self.queue)


if __name__ == '__main__':
    queue = Queue()
    # queue = Stack()
    queue.enqueue("hello")
    queue.enqueue("world")
    queue.enqueue("itcast")
    print(queue.size())
    print(queue.is_empty())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
