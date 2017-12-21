# 生成器是特殊的迭代器可用next()获取下一个值
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
        if current_index == 2:
            return "finish"
        print("---------3---------")

result = fib(5)
print(result)
while True:
    try:
        print(next(result))
    except StopIteration as e:
        # 获取生成器中的return的返回值
        # 如果生成器有return,那么执行到return会报错,抛出异常
        # 如果要获取return的返回值,可以使用异常的value值
        print(e.value)
        break


# yield 特点
# 程序执行到yield时会暂停返回值,下一次调用会继续一轮到下次yield返回值再停止
# return 只会返回一次值,但是yield可以多次返回值

