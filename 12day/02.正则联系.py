import re

txt = '''当处理正则表达式时，除了正则表达式对象之外，还有另一个对象类型：匹配对象。这
些是成功调用 match()或者 search()返回的对象。匹配对象有两个主要的方法：group()和
groups()。
group()要么返回整个匹配对象，要么根据要求返回特定子组。groups()则仅返回一个包含
唯一或者全部子组的元组。如果没有子组的要求，那么当group()仍然返回整个匹配时，groups()
返回一个空元组。
Python 正则表达式也允许命名匹配，这部分内容超出了本节的范围。建议读者查阅完整
的 re 模块文档，里面有这里省略掉的关于这些高级主题的详细内容。
1.3.4 使用 match()方法匹配字符串
match()是将要介绍的第一个 re 模块函数和正则表达式对象（regex object）方法。match()
函数试图从字符串的起始部分对模式进行匹配。如果匹配成功，就返回一个匹配对象；如果
匹配失败，就返回 None，匹配对象的 group()方法能够用于显示那个成功的匹配'''
ret = re.match("(a(b))", "ab")
print(ret.group())
print(ret.group(1))
print(ret.group(2))
print(ret.groups())

m = re.mat