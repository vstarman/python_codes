# 字符	功能
# |	匹配左右任意一个表达式
# (ab)	将括号中字符作为一个分组
# \num	引用分组num匹配到的字符串
# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串

import re
l = ["apple","pear","apricot","banana"]
for i in l:
    ret = re.match("apple|banana",i)
    if ret:
        print("i love >>>>",ret.group())
    else:
        print("i hate-----",i)

# 匹配11位的手机号
ret = re.match("1[34578][0-9]{9}","16758987564")
if ret:
    print(ret.group())
else:
    print("------Error-----")

# 匹配11位的手机号,最后不要4,7
ret = re.match("1[34578][0-9]{8}[0-35-68-9]","18758987568")
if ret:
    print(ret.group())
else:
    print("------Error-----")

