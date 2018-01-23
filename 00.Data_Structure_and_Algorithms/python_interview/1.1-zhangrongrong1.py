# 笔试题
# 一、 python 部分
# 1.1 请列举 python2 与 python3 的区别，请将下面的 python2 代码转换成python3。
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

points = [Point(9, 2), Point(1,5), Point(2, 7), Point(3, 8), Point(2, 5)]
sorted_points = sorted(
    points,
    lambda (x0, y0), (x1, y1): x0 - x1 if x0 != x1 else y0 - y1,
    lambda point: (point.x, point.y))

sorted_points = sorted(
    points,
    lambda (x0, y0), (x1, y1): x0 - x1 if x0 != x1 else y0 - y1,
    lambda point: (point.x, point.y))
# 预期结果为(1, 5), (2, 5), (2, 7), (3, 8), (9, 2)
print ', '.join(map(str, sorted_points)
"""


# 1.2 请用 python 写一个正则表达式实现电话号码的提取功能，下面是需要满足条
# 件：
# a. 匹配(123)-456-7890 和 123-456-7890
# b. 不匹配(123-456-7890 和 123)-456-7890


# 1.3 请用 python 写一个正则表达式实现如下内容的匹配，并实现数据的结构化
# b6b2af4a-02cb-4a45-819e-c35a74186608 300363 关于公司为全资子公司 Porton
# USA,L.L.C.申请融资提供担保的公告 2017-01-25
# {
# 'uuid': 'b6b2af4a-02cb-4a45-819e-c35a74186608',
# 'code': '300363',
# 'title': '关于公司为全资子公司 Porton USA,L.L.C.申请融资提供担保的公告',
# 'date': '2017-01-25'
# }
# 1.4 描述 python 开发中，协程，线程和进程的区别，请将下面代码改成可以在多
# 核 CPU 上并行执行的程序。
# import os
# import sys
# def dump_file(input_dir):
# if not os.path.exists(input_dir):
# print('dir {} not exists'.format(input_dir))
# return
# path_list = [os.path.join(input_dir, f).strip('\n') for f in
# os.listdir(input_dir)]
# file_path_list = filter(lambda file_path: os.path.isfile(file_path),
# path_list)
# for file_path in file_path_list:
# print('{}:{} size:{}'.format(os.getpid(), file_path,
# os.path.getsize(file_path)))
# if __name__ == '__main__':
# if len(sys.argv) > 1:
# dump_file(sys.argv[1])
# else:
# dump_file(os.getcwd())


# 1.5 请列常用的 python library，并说明其作用基本使用示例


# 1.6 请解释什么是 CORS 问题，在什么样的情况下，会遇到这个问题，常用的
# python 库里面该怎么解决这个问题。


# 二、 Linux 部分
# 2.1 假设这里有一台服务器地址为 192.168.0.2，开放的端口为 6623，如何连接到
# 远程服务器操作？
# 2.2 找出当前目录下 2 天内新创建的所有 json 文件。
# 2.3 如何查看(监控)CPU 使用情况，硬盘读写情况以及网络读写情况？
# 2.4 简述在浏览器中输入网址到网页内容展现出来，经过了一个什么样的过程。
# 2.5 如何查看系统某个端口是否已经被其他程序占用？
# 2.6 如何设置定时任务，如果定时任务执行命令的结果和在命令行直接执行该命令
# 的结果不同，请考虑可能存在什么问题。
# 2.7 git rebase 命令和 git merge 命令有什么区别，2 个命令对系统会造成什么影响。
# 三、 其他
# 3.1 请简单描述您对人工智能，知识图谱的了解。
# 3.2 请简单描述您未来 5 年的规划。
# 3.3 请介绍一下最近看的 5 本书.
