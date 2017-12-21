# 163,126,qq,foxmail,sina
# 字符	功能
# |	匹配左右任意一个表达式
# (ab)	将括号中字符作为一个分组
# \num	引用分组num匹配到的字符串
# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串
import re
# 小括号分成一个组,可以通过组数获取对应的值
ret = re.match("\w{4,20}@(163|126|qq|foxmail|sina)\.com$","haha@126.com")
if ret:
    print(ret.group())
else:
    pass

ret = re.match("(^0[1-9][0-9]{1,2})-?([256478][0-9]{6,7}$)","0104383384")
if ret:
    print(ret.group())
else:
    print("------error-----")


