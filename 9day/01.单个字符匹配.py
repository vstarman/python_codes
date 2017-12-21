#1/usr/bin/python
import re
# ret = re.match("t.o","two")
# print(ret)
# print(ret.group())

# l = ["hello", "help", "alpha", "None"]
# for i in l:
#     ret = re.match("[Hh]^\w*",i)
#     if ret:
#         print(i,ret.group())
#     else:
#         print(ret)
#         print("没有匹配到")

ret = re.match(".","M")
print(ret.group())


ret = re.match("t.o","too")
print(ret.group())
ret = re.match("t.o","two")
print(ret.group())

ret = re.match("h[a-zA-Z0-9_ ]*","hello python")
print(ret.group())
