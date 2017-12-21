import time, random
"""将应用程序属性实现为一个可调用的对象"""

def gettime():
    return time.ctime().encode()


def gettemp():
    """用随机数模拟天气"""
    html = """<!DOCTYPE html>
    <html
    lang="zh">
    <head>
    <meta charset = "UTF-8">
    <title> 获取气温 </title > </head>
    <body>

    <p> 您现在所在的位置气温是 %d 摄氏度 </p>

    </body >
    </html >""" % random.randint(-20, 40)
    return html.encode()

route_list = [
    ("/gettime.py", gettime),
    ("/gettemp.py", gettemp)
]



class application(object):
    def __init__(self, url_list):
        self.url_list = url_list
        print("路由列表的信息:", self.url_list)

    def __call__(self, environ, start_response):
        path_iinfo = environ["FileName"]
        for url, func in self.url_list:
            if url == path_iinfo:
                start_response("200 OK", [("Server", "PythonWSGIServer1.0")])
                return func()
        else:
            start_response("404 Not Found", [("Server", "PythonWSGIServer1.0")])
            return "hello world from WSGI".encode()


app = application(route_list)