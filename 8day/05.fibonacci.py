# def 迭代器
class Fibonacci():
    def __init__(self, num):
        # 记录传入数字,生成对应数据
        self.num = num
        self.a = 0
        self.b = 1
        # 当前迭代次数索引
        self.current_index = 0

    # 如果外界使用iter函数,调用__iter__方法
    def __iter__(self):
        return self

    # 如果外界使用iter函数,调用__iter__方法
    def __next__(self):
        if self.current_index < self.num:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result
        else:
            raise StopIteration

f = Fibonacci(5)
for i in f:
    print(i)