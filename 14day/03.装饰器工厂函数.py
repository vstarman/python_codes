# import time
#
# '''更具参数的不同 实现一个类似但是又不同的装饰器'''
#
# def factory(arg=None):
#     def timefun(func):
#         def wrappd_func():
#             if arg:
#                 print("%s called at %s" % (func.__name__, time.ctime()))
#             else:
#                 print("%s called at %s" % (func.__name__, time.time()))
#             return func()
#
#         return wrappd_func
#
#     return timefun
#
#
# @factory()
# def test():
#     for i in range(10):
#         print("雅黑~~")
#
# test()
import time


def clothes(func):
    print("开始穿衣:",time.time())
    def inner():
        return "+花裤衩+" + func() + "+绿裤衩+"
    return inner


@clothes
def person():
    print("穿衣结束:",time.time())
    return ">>>>>>>对,我没穿衣服>>>>>>"


print(person())
