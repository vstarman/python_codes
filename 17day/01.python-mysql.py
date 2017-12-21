from pymysql import *


def insert():
    # 创建数据库链接对象
    """ 参数host：连接的mysql主机，如果本机是'localhost'
        参数port：连接的mysql主机的端口，默认是3306
        参数database：数据库的名称
        参数user：连接的用户名
        参数password：连接的密码
        参数charset：通信采用的编码方式，推荐使用utf8
        host=None, user=None, password="",
        database=None, port=0, unix_socket=None,
        charset='',
    """
    conn = connect(host='localhost',
                   user="root",
                   password="mysql",
                   database="python",
                   port=3306,
                   charset="utf8")
    # 获得数据库操作对象Cursor
    curs = conn.cursor()
    # 编写sql语句
    sql = """insert into classes (name) values ('python222')"""
    # 执行sql语句
    curs.execute(sql)
    # 若是数据更新操作 应该用commit TODO 待完成
    conn.commit()
    # 关闭Cursor对象,connection对象
    curs.close()
    conn.close()


def select():
    # 创建数据库链接对象
    """ 参数host：连接的mysql主机，如果本机是'localhost'
        参数port：连接的mysql主机的端口，默认是3306
        参数database：数据库的名称
        参数user：连接的用户名
        参数password：连接的密码
        参数charset：通信采用的编码方式，推荐使用utf8
        host=None, user=None, password="",
        database=None, port=0, unix_socket=None,
        charset='',
    """
    conn = connect(host='localhost',
                   user="root",
                   password="mysql",
                   database="python",
                   port=3306,
                   charset="utf8")
    # 获得数据库操作对象Cursor
    curs = conn.cursor()
    # 编写sql语句
    sql = """select * from students where id = 10000"""
    # 执行sql语句
    ret = curs.execute(sql)
    for i in curs.fetchall():
        print(i)

    print(curs.fetchall())
    print(curs.fetchone())
    print(curs.fetchone())
    print(curs.fetchone())
    print(ret)
    # 若是数据更新操作 应该用commit TODO 待完成
    #conn.commit()
    # 关闭Cursor对象,connection对象
    curs.close()
    conn.close()


def update():
    # 创建数据库链接对象
    """ 参数host：连接的mysql主机，如果本机是'localhost'
        参数port：连接的mysql主机的端口，默认是3306
        参数database：数据库的名称
        参数user：连接的用户名
        参数password：连接的密码
        参数charset：通信采用的编码方式，推荐使用utf8
        host=None, user=None, password="",
        database=None, port=0, unix_socket=None,
        charset='',
    """
    conn = connect(host='localhost',
                   user="root",
                   password="mysql",
                   database="python",
                   port=3306,
                   charset="utf8")
    # 获得数据库操作对象Cursor
    curs = conn.cursor()
    # 编写sql语句
    sql = """update classes set name = 'python 666' where id = 5"""
    # 执行sql语句
    ret = curs.execute(sql)
    print(ret)
    # 若是数据更新操作 应该用commit TODO 待完成
    conn.commit()
    # 关闭Cursor对象,connection对象
    curs.close()
    conn.close()


def delete():
    # 创建数据库链接对象
    """ 参数host：连接的mysql主机，如果本机是'localhost'
        参数port：连接的mysql主机的端口，默认是3306
        参数database：数据库的名称
        参数user：连接的用户名
        参数password：连接的密码
        参数charset：通信采用的编码方式，推荐使用utf8
        host=None, user=None, password="",
        database=None, port=0, unix_socket=None,
        charset='',
    """
    conn = connect(host='localhost',
                   user="root",
                   password="mysql",
                   database="python",
                   port=3306,
                   charset="utf8")
    # 获得数据库操作对象Cursor
    curs = conn.cursor()
    # 编写sql语句
    sql = """delete from classes where id = 5"""
    # 执行sql语句
    ret = curs.execute(sql)

    print(ret)
    # 若是数据更新操作 应该用commit TODO 待完成
    conn.commit()
    # 关闭Cursor对象,connection对象
    curs.close()
    conn.close()


def main():
    print("-" * 50)
    print("1.查询班级")
    print("2.增加班级")
    print("3.修改班级")
    print("4.删除班级")
    print("0.退除")
    print("-" * 50)
    return input("请输入操作序号:")

if __name__ == '__main__':
    # num = main()
    # if num == 1:
    #     select()
    # elif num == 2:
    #     insert()
    # elif num == 3:
    #     insert()
    # elif num == 4:
    #     insert()
    # else:
    #     exit()
    #select()
    #update()
    delete()
