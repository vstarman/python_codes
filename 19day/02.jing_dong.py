from pymysql import *


class JD(object):
    def __init__(self):
        # 创建数据库对象 和 数据库操作对象
        self.qd_liu = connect(
            host='localhost',
            port=3306,
            database='jd_market',
            user='root',
            password='mysql',
            charset='utf8')
        self.cursor = self.qd_liu.cursor()

    @staticmethod
    def print_menu():
        """打印功能菜单"""
        print("----------------京东商城--------------")
        print("1:显示所有商品")
        print("2:下订单")
        print("3:登陆")
        print("4:注册")
        print("5:退出")
        return input("请输入功能编号:")

    def run(self):
        while True:
            number = self.print_menu()
            if number == "1":
                self.show_all_goods()
            elif number == "2":
                self.order()
            elif number == "3":
                self.login()
            elif number == "4":
                self.register()
            elif number == "5":
                self.__quit__()
                return
            else:
                print("输入功能序号有误,请重新输入...")

    def show_all_goods(self):
        pass

    def order(self):
        pass

    def login(self):
        pass

    def register(self):
        pass

    def __quit__(self):
        self.cursor.close()
        self.qd_liu.close()
        print("系统已登出...")


def main():
    jd = JD()
    jd.run()


if __name__ == '__main__':
    main()
