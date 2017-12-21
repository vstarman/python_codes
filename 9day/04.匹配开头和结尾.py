import re
# # 以数字开头
# ret = re.match("^[0-9].*","hello")
# if ret:
#     print(ret.group())
# else:
#     print("None")
#
# ret = re.match("^[0-9].*","9hello")
# if ret:
#     print(ret.group())
# else:
#     print("None")
#
# # 以数字开头,以数字4,7结尾
# ret = re.match("^[0-9].*[47]$","9hello4d")
# if ret:
#     print(ret.group())
# else:
#     print("None")
#
# # 以数字开头,结尾不是47
# # [^47]除了指定字符意外,都匹配
# ret = re.match("^[0-9].*[^47]$","9hello4d")
# if ret:
#     print(ret.group())
# else:
#     print("None")

# 除了a-z,都匹配
ret = re.match("^[a-zA-Z].*[^a-z]$","helloW")
if ret:
    print(ret.group())
else:
    print("None")

# ret = re.search("#[^#]+#","dsd#asda#sd#asdasd")
# if ret:
#     print(ret.group())
# else:
#     print("None")