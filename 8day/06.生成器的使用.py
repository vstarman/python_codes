
'''# 生成器是特殊的迭代器可用next()获取下一个值
# 如果在函数里出现了yield这个关键字,它就是生成器
def fib(num):
    a = 0
    b = 1
    current_index = 0
    print("---------1---------")
    while current_index < num:
        result = a
        a, b = b, a+b
        current_index += 1
        print("---------2---------")
        # 如果函数里出现了yield表示生成器
        yield result
        print("---------3---------")
        #return result

result = fib(5)
print(result)
print(next(result))
print(next(result))
print(next(result))

# yield 特点
# 程序执行到yield时会暂停返回值,下一次调用会继续一轮到下次yield返回值再停止
# return 只会返回一次值,但是yield可以多次返回值


def fib():
    a, b = 0, 1
    for i in range(5):
        yield b
        a, b = b, a+b
a = fib()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())'''


def test():
    i = 0
    while i < 5:
        temp = yield i
        i += 1

a = test()
print(a.__next__())
