
"""将应用程序属性实现为一个可调用的 对象"""
import time
import random


def gettime():
    return time.ctime().encode()


def gettemp():
    """用随机数 模拟提供气温数据"""
    html = """<!DOCTYPE html>
    <html
    lang="zh">
    <head>
    <meta charset = "UTF-8">
    <title> 获取气温 </title > </head>
    <body>

    <p> 您现在所在的位置气温是 %s 摄氏度 </p>

    </body >
    </html >
    """

    # %s是一个占位符  等待真正的数据到达 进行替换

    # data = get_data_from_database()
    data = random.randint(-20, 50)
    html_data = html % data
    # html_data = html
    return html_data.encode()

route_list = [
    ("/gettime.py", gettime),
    ("/gettemp.py", gettemp)
]


class application(object):
    def __init__(self, url_list):
        self.url_list = url_list

    def __call__(self, environ, start_response):
        path_info = environ['FILE_NAME']
        for url, func in self.url_list:
            if url == path_info:
                start_response("200 OK", [("Server", "PythonWSGIServer1.0")])
                return func()
        else:
            start_response("404 Not Found", [("Server", "PythonWSGIServer1.0")])
            return "hello world from WSGI".encode()


app = application(route_list)
# 判断一个对象是否可调用 使用callable(obj) 返回值为真表示可调用 为假表示不可调用
