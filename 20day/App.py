from pymysql import *

route_list = []
document_templates = './templates'


def route(url):
    def wrapper(func):
        global route_list
        print("开始装饰函数>>>>>>>>>:", func)
        route_list.append((url, func))

        def inner(*args, **kwargs):
            print("-"*20, func, "执行"+"-"*20)
            return func(*args, **kwargs)   # 返回函数返回值
        return inner
    return wrapper


def mysql_object(sql):
    db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    cur = db.cursor()
    cur.execute(sql)
    return db, cur


@route('/index.html')
def index(url):
    try:  # 模板+mysql数据库数据
        f = open(document_templates + url)
    except Exception as e:
        print("/index.html动态文件打开失败", e)
    else:
        content = f.read()
        f.close()

        # 数据库查取数据替换到body内
        sql = """"""

        < tr >
        < th > 序号 < / th >
        < th > 股票代码 < / th >
        < th > 股票简称 < / th >
        < th > 涨跌幅 < / th >
        < th > 换手率 < / th >
        < th > 最新价(元) < / th >
        < th > 前期高点 < / th >
        < th > 前期高点日期 < / th >
        < th > 添加自选 < / th >
    < / tr >
    { % content %}


    print(content)
    return content


@route('/add.html')
def add(url):
    return 'add func worked'


@route('/update.html')
def update(url):
    return 'update func worked'


class Application(object):
    """用来接收动态路径,返回相应资源"""
    def __init__(self, url_list):
        self.url_list = url_list

    def __call__(self, environ, start_response):
        path_info = environ["file_name"]
        for url, func in self.url_list:
            if path_info == url:
                start_response("200 OK", [("Samuel GOD", "CALL ME IF YOU CAN")])
                print("------>动态请求响应成功")
                return func(path_info).encode()
        else:
            start_response("404 Not Found", [("Samuel GOD", "CALL ME IF YOU CAN")])
            print("------>动态请求响应失败")
            return "404 Not Found".encode()


app = Application(route_list)
