# 关卡一
#
# 练习题:
#
# 1.简述你对闭包的理解？
# 闭包是指函数内定义的函数,且该函数用到外边函数的变量,则该函数与用到的变量统称为闭包

# 2.描述闭包的优点与注意点？
# 优点:提高代码的可移植性;缺点:用到的变量没及时释放,会占用内存

# 3.什么是装饰器？
# 装饰器是对一些函数进行相同功能的扩展时,采用的一中优美的函数编程方式

# 4.简述装饰器的功能？
# 1.日志
# 2.时间统计
# 3.函数前预备
# 4.汉书后清理
# 5.权限校验
# 6.缓存

# 5.一个函数同时使用两个装饰器，执行顺序是怎么执行的？
# 优先执行定义函数上最近的装饰器,之后再执行上面的装饰器



# 关卡二
#
# 练习题：
#
# 1.代码书写遵循什么原则？并解释？
# 开放封闭原则(对扩展开发开放;对已实现的功能代码块封闭)

# 2.完成一个装饰器，函数无参数
# def a(func):
#     def b():
#         print("------1------", func.__name__)
#         func()
#         print("------1------")
#     return b
# @a
# def c():
#     print("------2------")
# c()

# 3.完成一个装饰器，函数有参数

# def timefunc(func):
#     def inner(*args):
#         print(args)
#         func(*args)
#     return inner
#
#
# @timefunc
# def sonfunc(a,b):
#     print("参数乘积:", a*b)
# sonfunc(8,5)

# 4.完成一个装饰器，函数有返回值
def timefunc(func):
    def inner(*args):
        print(args)
        return func(*args)
    return inner


@timefunc
def sonfunc(a, b):
    print("参数乘积:", a*b)
    return "参数和", a+b

result = sonfunc(8, 5)

print(result)


from time import ctime, sleep


def timefun(func):
    def wrappend_func():
        print("-1-", ctime())
        return func()
    return wrappend_func


@timefun
def gettime():
    return "yohoooohhhhhh~~~~"
print(gettime())
# 1.调用装饰器装饰gettime,将gettime传入装饰器timefun(gettime)
# 2.调用def wrappend_func()
# 3.打印"-1-"
# 4.将传入的gettime()的返回值传出来
# 5.打印传出来的函数

# 注意：书写流程，写明注释

flist = []
for i in range(3):
    def foo(x):
        print(x+i)
        flist.append(foo)

for f in flist:
    f(2)


