import re

# 字符	功能
# *	匹配前一个字符出现0次或者无限次，即可有可无
# +	匹配前一个字符出现1次或者无限次，即至少有1次
# ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
# {m}	匹配前一个字符出现m次
# {m,n}	匹配前一个字符出现从m到n次


# *匹配0次或更多次
ret = re.match("t.*o","to")
print(ret)
print(ret.group())

# +匹配一个或无线个
ret = re.match("t[w]+o","twwwwwo")
print(ret)
print(ret.group())

# ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
ret = re.match("http[s]?","http")
print(ret.group())
ret = re.match("http[s]?","https")
print(ret.group())


ret = re.match("http[s]?","hello python")
print(ret.group())

