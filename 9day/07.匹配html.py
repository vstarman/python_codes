import re

content = "<html>hh<html>"

ret = re.match("<[a-zA-Z0-9]+>.*</[a-zA-Z0-9]+>",content)
if ret:
    print(ret.group())
else:
    print("-----error-----")


# \的使用,保证前后匹配结果在后面也可以使用
# \1 表示使用第一组数据
