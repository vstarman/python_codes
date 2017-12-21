import re

# search 查找
ret = re.search("\d+","水果为:苹果,橘子,鸭梨,总数为33个")
if ret:
    print(ret.group())
else:
    print("------Error-----")


# 查找所有
ret_list = re.findall("\d+","水果为:苹果10个,橘子20个,鸭梨30个,总数为60个")
if ret:
    print(ret_list)
else:
    print("------Error-----")


# 替换
ret = re.sub("\d+","1000","阅读数:8")
print(ret)

# sub定义函数
def show_msg(data):
    result = data.group()
    return "阅读数>>>" + result

ret = re.sub("\d+",show_msg,"阅读数:8")
print(ret)


# split
str1 = "hehe:xixi:haha 哈哈"
str_list = re.split(":| ",str1)
print(str_list)