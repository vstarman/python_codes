class Deque(object):
    """创建一个空的双端队列"""
    def __init__(self):
        self.deque = []
        
    def add_front(self, item):
        """从队头加入一个item元素"""
        return self.deque.insert(0, item)
    
    def add_rear(self, item):
        """从队尾加入一个item元素"""
        return self.deque.append(item)
    
    def remove_front(self):
        """从队头删除一个item元素"""
        return self.deque.pop(0)
    
    def remove_rear(self):
        """从队尾删除一个item元素"""
        return self.deque.pop()
    
    def is_empty(self):
        """判断双端队列是否为空"""
        return self.deque == []
    
    def size(self):
        """返回队列的大小"""
        return len(self.deque)

    def traversal(self):
        """遍历列表"""
        return [i for i in self.deque]


if __name__ == '__main__':
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(deque.traversal())
    print(deque.size())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_rear())
    print(deque.remove_rear())
