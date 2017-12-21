import re

img_url = """<img data-original="https://rpic.douyucdn.cn/appCovers/2017/09/13/688928_20170913203807_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/09/13/688928_20170913203807_big.jpg" width="283" height="163" style="display: block;">.jpg"""

# 第二个问号表示非贪婪,没有的话会默认选字符串最后的.jpg
# ret = re.search("http[s]?://.*\.jpg", img_url)
ret = re.search("http[s]?://.*?\.jpg", img_url)
if ret:
    print(ret.group())
else:
    print("无法匹配")


s = "This is a number 234-235-22-432"

ret = re.match(".*?(\d+-\d+-\d+-\d+)", s)
if ret:
    print(ret.group(1))
else:
    print("无法匹配")

