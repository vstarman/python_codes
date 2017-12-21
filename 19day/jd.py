from pymysql import *
from hashlib import *
import time


class JD(object):
    def __init__(self):
        # 创建数据库链接对象和操作对象
        self.db = connect(host='localhost', port=3306, database='demo',
                          user='root', password='mysql', charset='utf8')
        self.cur = self.db.cursor()
        self.customer_id = None   # 记录登录状态

    def start(self):
        while True:
            num = self.show_menu()
            if num == "1":
                self.show_goods()
            elif num == "2":
                self.order()
            elif num == "3":
                self.login()
            elif num == "4":
                self.register()
            elif num == "5":
                break
            else:
                print("输入有误,请重新输入...")

    def show_goods(self):
        """显示商品信息表"""
        # id | name                 | cate_id | brand_id | price    | is_show | is_saleoff
        #  1 | r510vc 15.6英寸笔记本 |       5 |        2 |  3399.00 |        |
        sql = """select g.id, g.name, c.name, b.name, g.price from goods as g
                 inner join goods_cates as c on g.cate_id=c.id
                 inner join goods_brands as b on g.brand_id=b.id"""
        self.cur.execute(sql)        # 执行sql语句
        ret = self.cur.fetchall()    # 返回所有查到的信息
        # 打印商品
        for i in ret:
            print(i)

    def order(self):
        """下订单"""
        goods_id = input("请输入商品编号:")
        # 查询是否登录
        if self.customer_id is None:
            print("下订单前, 请先登录...")
            return
        # 下订单:向订单表 和 订单详情表插入数据
        if goods_id.isdigit():
            # 获取当前时间
            order_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(time.localtime())
            print(order_time)
            sql = """insert into orders (order_date_time, customer_id) values (%s, %s)"""
            self.cur.execute(sql, [order_time, self.customer_id])
            last_id = self.cur.lastrowid  # 获取上一步操作的id
            # 订单详情表
            sql = """insert into order_detail (order_id, goods_id, quantity) values (%s, %s, %s)"""
            self.cur.execute(sql, [last_id, goods_id, "1"])
            self.db.commit()

    def login(self):
        """进行登录"""
        name = input("请输入用户名：")
        passwd = input("请输入密码：")
        # 避免撞库遍历出密码,python自带加密模块
        sha = sha1()  # 创建sha对象
        sha.update(passwd.encode())  # 将编码后的密码传入
        sha_pwd = sha.hexdigest()  # 加密成功
        sql = """select * from customer where name = %s and passwd = %s"""
        self.cur.execute(sql, [name, sha_pwd])
        ret = self.cur.fetchone()
        if ret:
            print("登陆成功...")
            self.customer_id = ret[0]
            return
        else:
            print("登录失败,请重新输入...")

    def register(self):
        """进行注册"""
        name = input("请输入用户名：")
        tel = input("请输入电话号码：")
        passwd = input("请输入密码：")
        # 判断用户名是否以存在
        sql = """select * from customer where name = %s"""
        self.cur.execute(sql, [name])
        ret = self.cur.fetchone()
        if ret:
            print("用户名以存在,请重新注册")
            return
        # 避免撞库遍历出密码,python自带加密模块
        sha = sha1()                  # 创建sha对象
        sha.update(passwd.encode())   # 将编码后的密码传入
        sha_pwd = sha.hexdigest()     # 加密成功

        sql = "insert into customer (name, tel, passwd) values (%s, %s, %s)"
        self.cur.execute(sql, [name, tel, sha_pwd])  # 执行
        self.db.commit()                             # 提交
        print(">>>>注册成功>>>>")

    def __del__(self):
        self.cur.close()
        self.db.close()

    @staticmethod
    def show_menu():
        """打印功能菜单"""
        print("------京东商城-------")
        print("1: 显示所有的商品")
        print("2: 下订单")
        print("3: 登录")
        print("4: 注册")
        print("5: 退出")
        return input("请输入对应的数字: ")



def main():
    jd = JD()
    jd.start()


if __name__ == '__main__':
    main()
