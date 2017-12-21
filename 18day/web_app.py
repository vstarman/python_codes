import random, time, urllib.parse, re

route_list = list()


def route(url):
    def wrapper(func):  # 包装url和func函数到列表
        global route_list
        route_list.append((url, func))
        print("开始装饰函数>>>>>>", func)

        def inner(*args, **kwargs):  # 执行装饰的函数,防止函数用到参数,用*args记录下来
            print("-----------发卡---------")
            return func(*args, **kwargs)  # 将函数返回值传回去
        return inner
    return wrapper


@route(r"/login\.py\?user=(.*)")
def login(user):
    print("开始执行到函数内部>>>>>>", user)
    return """<!DOCTYPE html> <html lang = "zh">
        <head> <meta charset = "UTF-8"> <title> 欢迎 </title > </head>
        <body> <p> %s, 你好 </p> </body>
        </html> """ % urllib.parse.unquote(user)


@route("/gettime.py")
def gettime():
    print("---------here2-------")
    return time.ctime()


@route("/gettemp.py")
def gettemp():
    return """<!DOCTYPE html><html lang="zh">
        <head> <meta charset = "UTF-8"> <title> 获取气温 </title > </head>
        <body> <p> 您现在所在的位置气温是 %s 摄氏度 </p> </body >
        </html > """ % random.randint(-20, 50)


class Application(object):
    def __init__(self):
        self.url_list = route_list

    def __call__(self, environ, start_response):
        path_info = environ["file_name"]
        print("---------->", self.url_list)
        for url, func in self.url_list:
            if url == path_info:
                start_response("200 OK", [("Sever", "WSGIServer dynamic response1.1")])
                return func().encode()
            # 用正则匹配用户姓名
            ret = re.match(url, path_info)
            if ret:
                user_name = ret.group(1)
                print("--------------->", user_name)
                start_response("200 OK", [("Sever", "WSGIServer dynamic response1.1")])
                return func(user_name).encode()

        else:
            start_response("404 Not Found", [("Sever", "WSGIServer dynamic response1.1")])
            return open("./static/super404/index.html", "rb").read()


app = Application()
login("hello")