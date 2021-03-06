# -*- coding:utf-8 -*-
def fn(x, y):
    """返回整数"""
    return x * 10 + y


def char2num(s):
    """字符串转数字"""
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2num(string):
    """将字符串转为整形"""
    a = map(lambda s: {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s], string)
    return reduce(lambda x, y: x*10+y, a)


def prod(lst):
    """列表求积"""
    def prt():
        print(reduce(lambda x, y: x * y, lst))
    return prt()


def name_format(lst):
    """列表:人名自动格式化"""
    map(lst)


if __name__ == '__main__':
    # print str2num('21397981623')
    prod([3, 4, 5, 6])
