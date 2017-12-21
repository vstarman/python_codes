# 生成器是特殊的迭代器可用next()获取下一个值
# 如果在函数里出现了yield这个关键字,它就是生成器
def fib(num):
    a = 0
    b = 1
    current_index = 0
    while current_index < num:
        result = a
        a, b = b, a+b
        # 如果函数里出现了yield表示生成器
        # params 可以给生成器传入这个参数
        print("-------2------")
        params = yield result
        print("传入参数为:", params)
        print("-------3------")

result = fib(5)
# 一般会使用next执行第一次,若果想要用send,第一次调用传值为None
#print(next(result))
print(result.send(None))
print(result.send("hello"))

