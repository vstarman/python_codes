import functools
result = (lambda k:functools.reduce(int.__mul__,range(1,k+1),1))(int(input("请输入一个数，求其阶乘：")))
print(result)
