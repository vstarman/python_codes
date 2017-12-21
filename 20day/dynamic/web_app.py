import random, time, urllib.parse, re, threading
from pymysql import *

route_list = list()
# 模板路徑
document_templates = "./templates"


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


@route("/index.html")
def index(url):
    # index.html 模板样式+mysql数据
    # 打开文件
    try:
        f = open(document_templates + url)
    except Exception as e:
        return print("动态文件打开失败:", e)
    else:
        # 获取文件内容
        content = f.read()
        f.close()

        # 数据库对象
        db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        # 数据库操作对象
        cur = db.cursor()
        # sql
        sql = "select * from info"
        cur.execute(sql)
        ret = cur.fetchall()
        print(ret)
        # 置换html中的信息
        html_template = """<tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>
                            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
                        </td>
                    </tr>"""
        html = ""
        # < th > 序号 < / th >
        # < th > 股票代码 < / th >
        # < th > 股票简称 < / th >
        # < th > 涨跌幅 < / th >
        # < th > 换手率 < / th >
        # < th > 最新价(元) < / th >
        # < th > 前期高点 < / th >
        # < th > 前期高点日期 < / th >
        # < th > 添加自选 < / th >
        # (94, '603993', '洛阳钼业', '2.94%', '2.50%', Decimal('7.36'), Decimal('7.16'), datetime.date(2017, 7, 19))
        for item in ret:
            html += html_template % (item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[1])
        # 将之前表级 {%content%} 替换为html
        content = re.sub(r"\{%content%\}", html, content)

        return content


@route("/center.html")
def center(url):
    # index.html 模板样式+mysql数据
    # 打开文件
    try:
        f = open(document_templates + url)
    except Exception as e:
        return print("动态文件打开失败:", e)
    else:
        # 获取文件内容
        content = f.read()
        f.close()

        # 数据库对象
        db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        # 数据库操作对象
        cur = db.cursor()
        # sql  | id | note_info                | info_id |
        sql = """select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info from info as i inner join focus as f on i.id = f.info_id"""
        cur.execute(sql)
        ret = cur.fetchall()
        print(ret)
        # 置换html中的信息
        html_template = """<tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                       <td>
                           <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                       </td>
                       <td>
                           <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
                       </td>
                   </tr>"""
        html = ""

        for item in ret:
            html += html_template % (item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[0], item[0])
        # 将之前表级 {%content%} 替换为html
        content = re.sub(r"\{%content%\}", html, content)

        return content


@route("/add/(\d{6})\.html")
def add(pattern, url):
    # /add/000007.html
    code = re.match(pattern, url).group(1)

    # 数据库对象,操作对象,sql语句
    db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    cur = db.cursor()
    # 用正则匹配到的股票代号,往表focus加入数据
    # id = (select id from info where code = %s)
    # insert into focus (info_id) values (select id from info where code = %s)
    sql = """insert into focus (info_id) select id from info where code = %s"""
    ret = cur.execute(sql, [code])
    print("执行结果:", ret)
    db.commit()
    cur.close()
    db.close()

    return "添加成功"


@route("/del/(\d{6})\.html")
def delete(pattern, url):
    # /del/300268.html
    code = re.match(pattern, url).group(1)

    # 数据库对象,操作对象,sql语句
    db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    cur = db.cursor()
    # 用正则匹配到的股票代号,从表focus删除数据
    # id = (select id from info where code = %s)
    # insert into focus (info_id) values (select id from info where code = %s)
    sql = """delete from focus where info_id = (select id from info where code = %s)"""
    cur.execute(sql, [code])
    db.commit()
    cur.close()
    db.close()

    return "删除成功"


@route("/update/(\d{6})\.html")
def update_page(pattern, url):
    # /update/000007.html
    code = re.match(pattern, url).group(1)
    try:
        f = open(document_templates + "/update.html")
    except Exception as e:
        return print("动态文件打开失败:", e)
    else:
        content = f.read()
        f.close()

        # 数据库对象,操作对象,sql语句
        db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cur = db.cursor()
        # 用code查询股票的的id 和 focus中的note_info信息,替换给{%code%}{%note_info%}
        # select note_info from focus where info_id = (select id from info where code = %s)
        sql = """select i.short, f.note_info from focus as f inner join info as i on f.info_id = i.id where info_id = (select id from info where code = %s)"""
        cur.execute(sql, [code])
        ret = cur.fetchone()
        print(ret)
        # 正则替换
        content = re.sub(r"{%code%}", ret[0], content)
        content = re.sub(r"{%note_info%}", ret[1], content)
        cur.close()
        db.close()

    return content


@route("/update/(\d{6})\.html")
def update_page(pattern, url):
    # /update/%E6%96%B0%E9%9B%86%E8%83%BD%E6%BA%90/.html ---> 解码
    short = re.match(pattern, url).group(1)       # 股票简称
    note_info = re.match(pattern, url).group(2)   # 备注信息
    # 将url编码后的数据(三个%xx为一个中文)解码
    short = urllib.parse.unquote(short)
    note_info = urllib.parse.unquote(note_info)
    # 数据库对象,操作对象,sql语句
    db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    cur = db.cursor()
    # 根据股票简称info.short修改focus.note_info
    # update focus set not_info = %s where info.id = (select id from info where short = %s)
    sql = """update focus set not_info = %s where info.id = (select id from info where short = %s)"""
    cur.execute(sql, [note_info, short])
    db.commit()
    cur.close()
    db.close()

    return "更新成功"


@route(r"/login\.html\?user=(.*)")
def login(user):
    print("开始执行到函数内部>>>>>>", user)
    return """<!DOCTYPE html> <html lang = "zh">
        <head> <meta charset = "UTF-8"> <title> 欢迎 </title > </head>
        <body> <p> >>>>欢迎登录, %s>>>> </p> </body>
        </html> """ % urllib.parse.unquote(user)


class Application(object):
    def __init__(self):
        self.url_list = route_list

    def __call__(self, environ, start_response):
        path_info = environ["file_name"]
        print("---------->", self.url_list)
        for url, func in self.url_list:
            if url == path_info:
                start_response("200 OK", [("Sever", "WSGIServer dynamic response1.1")])
                return func(url).encode()
            # 如果url有正则,就不能进行相等操作,将url传入函数中,让函数内部进行处理
            if re.match(url, path_info):
                start_response("200 OK", [("Sever", "WSGIServer dynamic response1.1")])
                print(url, path_info)
                return func(url, path_info).encode()

        else:
            start_response("404 Not Found", [("Sever", "WSGIServer dynamic response1.1")])
            return open("./static/super404/index.html", "rb").read()


app = Application()