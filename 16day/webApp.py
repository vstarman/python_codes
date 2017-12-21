import time, random

route_list = list()


def route(url):
    def warpper(func):
        # 关联url和对应的函数代码
        global route_list
        route_list.append((url, func))

        def inner(*args, **kwargs):
            # func 开始执行,记录下args kwargs的所有值
            ret = func(*args, **kwargs)
            # 执行完成 释放一些资源
            return ret
        return inner
    return warpper


@route("/gettime.py")
def gettime():
    return time.ctime()


@route("/gettemp.py")
def gettemp():
    """用随机数 模拟提供气温数据"""
    html = """<!DOCTYPE html>
            <html lang="zh">
            <head> <meta charset = "UTF-8"><title> 获取气温 </title > </head>
            <body><p> 您现在所在的位置气温是 %s 摄氏度 </p></body >
            </html >
            """ % random.randint(-20, 40)
    return html


class Application(object):
    def __init__(self, url_list):
        self.url_list = url_list
        print("路由列表的信息:", self.url_list)

    def __call__(self, environ, start_response):
        path_info = environ["file_name"]
        for url, func in route_list:
            if url == path_info:
                start_response('200 OK', [('Content-Type', 'text/html')])
                print(func())
                return func().encode()
        else:
            start_response('400 not found', [('Content-Type', 'text/html')])
            return "Sorry ,File Not Fould!"

app = Application(route_list)

