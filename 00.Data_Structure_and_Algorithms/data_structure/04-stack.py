class Stack(object):
    """栈实现"""
    def __init__(self):
        self.stack = []

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        return self.stack.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.stack.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.stack[-1]

    def is_empty(self):
        """判断栈是否为空"""
        return self.stack == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
    # stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
