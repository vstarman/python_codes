from collections import Iterable, Iterator


class Mylist():
    """自定义迭代对象,仿照列表"""
    def __init__(self):
        self.items = list()

    # 添加元素
    def append_item(self, item):
        self.items.append(item)

    # 添加__iter__方法,表示对象可以迭代
    def __iter__(self):
        # 返回迭代器,return
        # 可迭代对象的本质是通过迭代器来获取下一数据
        myIteraor = MyIterator(self.items)
        return myIteraor

class MyIterator():
    def __init__(self, items):
        self.items = items
        # 当前下标
        self.current_index = 0
        result = isinstance(self,Iterator)
        print(result)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.items):
            self.current_index += 1
            return self.items[self.current_index - 1]
        else:
            # 抛出迭代完成的异常信息
            raise StopIteration


# 迭代器:如果类里面由__iter__和__next__表示迭代器
# 记录当前遍历的位置和对应的值


# 创建自定义类对象,添加元素
mylist = Mylist()
mylist.append_item("bob")
mylist.append_item("john")
# for 内部处理了迭代完成后抛出的异常,自己用try处理了
for i in mylist:
    print(i)


# class MyList():
#     def __init__(self):
#         self.container = list()
#
#     def add(self, item):
#         self.container.append(item)
#
#     def __inte
#
# l = MyList()
# l.add(1)
# l.add(2)
# l.add(3)
# for i in l:
#     print(i)