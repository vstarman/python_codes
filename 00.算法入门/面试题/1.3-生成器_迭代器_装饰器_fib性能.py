from time import time


def time_cost(fn):
    """Decorator, used to calculate function execution time"""
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        stop_time = time()
        print('The time cost: {}s'.format(stop_time-start_time))
        return result
    return wrapper


# 缓存装饰器, 减少fib函数时间花销
def demo(fn):
    cache = {}
    miss = object()

    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result
    return wrapper


# @time_cost
@demo
def simple_fib(num):
    if num < 2:
        return num
    return simple_fib(num-1) + simple_fib(num-2)


class Fib(object):
    """docstring for my iterator"""
    def __init__(self, num):
        super(Fib, self).__init__()
        self.num = num
        self.n, self.a, self.b = 0, 0, 1

    def __next__(self):
        if self.n < self.num:
            result = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
            return result
        raise StopIteration

    def __iter__(self):
        return self


def fib(num):
    result_list = [i for i in Fib(num)]
    return result_list[-1]


def generator_fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield a


"""
单独运行,fn(10)-->1.6s
装饰器运行,fn(150)-->The time cost: 0.002596139907836914s
                    Num is:  9969216677189303386214405760200
类,fn(150)-->The time cost: 0.00012040138244628906s
            9969216677189303386214405760200
生成器,
"""
if __name__ == '__main__':
    # 以函数形式调用时间装饰器
    # print(time_cost(simple_fib)(150))

    print(time_cost(fib)(150))
