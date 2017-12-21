from pymysql import *
from hashlib import *
import time


class JD(object):
    def __init__(self):
        self.db = connect(host='localhost', port=3306, database='demo', user='root', password='mysql', charset='utf8')
        self.cur = self.db.cursor()
        self.customer_id = None

    def run(self):
        while True:
            op = self.print_menu()
            if op == "1":
                self.show_goods()
            elif op == "2":
                self.order()
            elif op == "3":
                self.login()
            elif op == "4":
                self.register()
            elif op == "5":
                break
            else:
                print("输入有误, 请重新输入")


    def print_menu(self):
        """打印功能菜单"""
        print("------京东商城-------")
        print("1: 显示所有的商品")
        print("2: 下订单")
        print("3: 登录")
        print("4: 注册")
        print("5: 退出")
        op = input("请输入对应的数字: ")
        return op

    def __del__(self):
        self.cur.close()
        self.db.close()

    def show_goods(self):
        # sql
        sql = """select g.id, g.name, g.price, c.name, b.name from goods as g
                  inner join goods_cates as c on g.cate_id = c.id
                  inner join goods_brands as b on g.brand_id = b.id"""
        self.cur.execute(sql)
        ret = self.cur.fetchall()
        for item in ret:
            print(item)

    def register(self):
        """注册"""
        name = input("请输入用户名: ")
        tel = input("请输入电话号码: ")
        pwd = input("请输入密码: ")

        # 根据用户名到数据库中查询该用户有没有对应的信息 有: 用户已经存在 不能够注册, 没有: 注册
        sql = "select * from customer where  name = %s"
        self.cur.execute(sql, [name])
        ret = self.cur.fetchone()
        if ret:
            # 不为None
            print("用户名已经存在, 请重新选择")
            return

        # 撞库

        # python 中加密?
        sha = sha1()
        sha.update(pwd.encode())
        sha_pwd = sha.hexdigest()
        sql = "insert into customer (name, passwd,tel) values (%s, %s, %s)"
        self.cur.execute(sql, [name, sha_pwd, tel])

        # 数据的更新操作 需要提交
        self.db.commit()
        # 关闭
        print(">>>> 注册成功 >>>>")

    def login(self):
        """登录"""
        name = input("请输入用户名: ")
        pwd = input("请输入密码: ")

        sha = sha1()
        sha.update(pwd.encode())
        sha_pwd = sha.hexdigest()

        sql = "select * from customer where name = %s and passwd = %s"
        self.cur.execute(sql, [name, sha_pwd])
        ret = self.cur.fetchone()
        if ret:
            # 有结果
            print("用户名密码正确, 登录成功")
            self.customer_id = ret[0]
        else:
            print("用户名或密码错误, 登录失败")

    def order(self):
        goods_id = input("请输入商品编号: ")
        # 判断是否登录 登录
        if self.customer_id is None:
            print("下订单前, 请先登录")
            return

        # 下订单 向订单表 和订单详情表中插入数据
        if goods_id.isdigit():
            # 获取当前时间 --> 格式化成为 2017-11-11 11:11:11
            order_date =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            sql = "insert into orders (order_date_time, customer_id) values (%s, %s)"
            self.cur.execute(sql, [order_date, self.customer_id])
            print("------------1-----------")
            last_id = self.cur.lastrowid
            print(last_id)
            # 订单详情表
            sql = "insert into order_detail (order_id, goods_id, quantity) values (%s, %s, %s)"

            self.cur.execute(sql, [last_id, goods_id, '1'])
            print("------------2-----------")
            # 提交
            self.db.commit()



def main():
    # 实例化 jd对象
    jd = JD()
    # jd 持续不断的提供服务
    jd.run()

if __name__ == '__main__':
    main()