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
result = isinstance(mylist, Iterable)

# iter 函数获取迭代对象中的迭代器
myIterator = iter(mylist)
print(myIterator)

# 使用next函数获取迭代器中下一个值
# value = next(myIterator)
# print(value)
# value = next(myIterator)
# print(value)
# value = next(myIterator)
# print(value)
# value = next(myIterator)
# print(value)

while True:
    try:
        value = next(myIterator)
        print(value)
    except StopIteration as e:
        #print("迭代完成",e)
        break

# for in 循环的本质,里边通过next获取迭代器中的下一个值,自己捕获停止迭代的异常(StopIteration)
# 可以直接用for in 遍历该迭代器
# for in 如果遍历的是可迭代对象,那么他会通过iter遍历其中迭代器,如果是迭代器,则直接遍历
for i in mylist:
    print(i)



l = [1,2]
# 获取列表的迭代器
for i in iter(l):
    print(i)


