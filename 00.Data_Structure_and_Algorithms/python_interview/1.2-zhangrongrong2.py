# 1.python中yield关键字作用? 使用时间? 优点

# 2. __new__和__init__区别
"""
__new__ :创建实例时调用,返回该实例,为静态方法
__init__:初始化实例时调用,然后设置对象的一些初始属性
过程:__new__在__init__之前调用,__new__返回的实例作为第一个参数传递给__init__,
    然后__init__给这个实例设置一些属性
"""

# 3.with open文件时,做了那些事情? 为什么不用去close()这个文件

# 4.现有字典d = {'a':24, 'g':53, '1': 12, 'k':33}


# 5.map(), filter(), zip(), lambda作用和用法

# 6.msg =
# 匹配出ip和url

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

# 8.实现parse_json()函数,对json数据key值校验

# 9.将一个正整数分解质因数.例如:输入90,打印90=2*3*3*5


