'''from collections import Iterable

result = isinstance([1, 2, 3], Iterable)
print("list 是否可迭代:", result)

result = isinstance((1, 2, 3), Iterable)
print("tuple 是否可迭代:", result)

result = isinstance({1, 2, 3}, Iterable)
print("set 是否可迭代:", result)

result = isinstance({"a": 1, "b": 2, "c": 3}, Iterable)
print("dict 是否可迭代:", result)

result = isinstance("hello world", Iterable)
print("str 是否可迭代:", result)

result = isinstance(100, Iterable)
print("int 是否可迭代:", result)'''

from collections import Iterable
print(isinstance([], Iterable))
print(isinstance(set(),Iterable))
print(isinstance(dict(),Iterable))
print(isinstance((),Iterable))

