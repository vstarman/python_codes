# 1.python中yield关键字作用? 使用时间? 优点
# yield是python中定义为生成器函数,其本质是封装了__iter__和__next__方法的迭代器.

# 2. __new__和__init__区别
# __new__ :创建实例时调用,返回该实例,为静态方法
# __init__:初始化实例时调用,然后设置对象的一些初始属性
# 过程:__new__在__init__之前调用,__new__返回的实例作为第一个参数传递给__init__,然后__init__给这个实例设置一些属性

# 3.with open文件时,做了那些事情? 为什么不用去close()这个文件
"""
close()是为了释放资源。
如果不close()，那就要等到垃圾回收时，自动释放资源。垃圾回收的时机是不确定的，也无法控制的。

如果程序是一个命令，很快就执行完了，那么可能影响不大（注意：并不是说就保证没问题）。
但如果程序是一个服务，或是需要很长时间才能执行完，或者很大并发执行，就可能导致资源被耗尽，也有可能导致死锁。

使用with打开文件时,紧跟with的语句被求值后,返回对象的__enter__()方法被调用,这个方法的返回值将被赋予给as后的变量.
当with后的代码快执行完毕后,将调用前面返回对象的__exit__()方法.
"""

# 4.对dirA按照value值得索引为1进行排序
"""
dirA = {'a': ['a', 2], 'b': ['b', 1], 'c': ['c', 3]}
dirB = sorted(dirA.items(), key=lambda x: x[1][1])

print(dirB)
"""

# 5.map(), filter(), zip(), lambda作用和用法
"""
1.lambda其实就是一条语句，lambda(x):body。x是lambda函数的参数，参数可以有任意多个(包括可选参数);
    body是函数体，只能是一个表达式，并且直接返回该表达式的值。
2.filter(func, list)接受两个参数：一个函数func和一个列表list，返回一个列表。函数func只能有一个参数。
    filter的功能：列表中所有元素作为参数传递给函数，返回可以另func返回真的元素的列表
3.zip([iterable, ...])函数接受任意多个序列作为参数，将所有序列按相同的索引组合成一个元素是各个序列合并成的tuple的新序列，
    新的序列的长度以参数中最短的序列为准。另外(*)操作符与zip函数配合可以实现与zip相反的功能，即将合并的序列拆成多个tuple
4.map(function, iterable, ...)操作list,py2返回列表,py3返回迭代器,绑定的函数为修改list中每一个值的函数
    map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
"""

# 6.匹配出ip和url
"""
import re
msg = '192.168.0.1 25/Otc/2012:14:46:34 "GET /api/HTTP/1.1" 200 44 "http://abc.com/search"'
regex = re.compile(r'(\d+.\d+.\d+.\d+?).+HTTP://(.+)"$', re.I)
result = re.search(regex, msg)
print(result.groups())
"""

# 7.多层列表展开
"""
listA = [1, 2, [3, 4, 5, [6, 7, [8], 9]], 10, [11, [12, 13, [14, 15]], 16], 17, [18]]


def flatten(input_list):
    output_list = []
    while True:
        if input_list == []:
            break
        for index, i in enumerate(input_list):
            if type(i) == list:
                input_list = i + input_list[index+1:]
                break
            else:
                output_list.append(i)
                input_list.pop(index)
                break
    return output_list

print(flatten(listA))
"""

# 8.写一个装饰器,实现对parse_json(db_info)函数的key值校验,确保其中'User,Password,Database'为必须
"""
db_info = {'Type': 'oracle', 'User': 'oracle', 'Password': 'system',
           'Database': 'docker', 'Addr': 'localhost', 'Port': '1512'}


def key_verify(func):
    def inner(*args, **kwargs):
        # print(*args)
        if 'User' and 'Password' and 'Database' in list(*args):
            return func(*args, **kwargs)
        return 'Verify False'
    return inner


@key_verify
def parse_json(db_info):
    return [key for key in db_info.keys()]

print(parse_json(db_info))
"""

# 9.将一个正整数分解质因数.例如:输入90,打印90=2*3*3*5
number = int(input('Enter a number: '))
prime_list = list()


def get_prime(num):
    import math
    is_prime = True
    for i in range(1, int(math.sqrt(num + 1)) + 1):
        if (num % i) == 0 and i != 1:
            prime_list.append(i)
            is_prime = False
            get_prime(num / i)
            break
    if is_prime:
        prime_list.append(num)

get_prime(number)
print(prime_list)
