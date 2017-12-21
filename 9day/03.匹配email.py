import re
# .s是特殊字符,需要\转印成无效.字符
ret = re.match("\w{4,20}@163\.com$","hello@163.com")
if ret:
    print(ret.group())
else:
    print("无匹配")


