#!/usr/bin/python2.7
# -*- coding:utf-8 -*-


class MyList(object):
    """自定义的一个可迭代对象"""
    def __init__(self):
        self.items = []

    def add(self, val):
        self.items.append(val)

    def __iter__(self):
        myiterator = MyIterator(self)
        return myiterator


class MyIterator(object):
    """自定义的供上面可迭代对象使用的一个迭代器"""
    def __init__(self, mylist):
        self.mylist = mylist
        # current用来记录当前访问到的位置
        self.current = 0

    def __next__(self):
        if self.current < len(self.mylist.items):
            item = self.mylist.items[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


def add(x, y):
    return x + y

if __name__ == '__main__':
    # li = [11, 22, 33, 44]
    # li_iter = iter(li)
    # map(lambda x: x, next(li_iter)

    print map(lambda x: x*x, [11, 22, 33])
    print type(map(str, {'a': 1, 'b': 2}))
    print reduce(lambda x, y: x * 10 + y, [1, 3, 5, 7, 9])
