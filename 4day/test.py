'''
# 将列表中数字组成互不相同，且无重复的三位数
lst = [1, 2, 3, 4]
lst1 = []
for i in lst:
    for j in lst:
        for k in lst:
            lst1.append(int("%s%s%s" % (i, j, k)))
# lst2 = set(lst1)
# print(len(lst1), len(lst2))
print(lst1)




# 奖金计算
i = int(input("当月利润："))
level = [1000000, 600000, 400000, 200000, 100000, 0]
percent = [0.001, 0.015, 0.03, 0.05, 0.075, 0.1]
money = 0
for j in range(6):
    if i > level[j]:
        money += (i - level[j]) * percent[j]
        i = level[j]
print(money)

import math
num = 1
flag = 1
lst = []

while flag <= 3:
    if math.sqrt(num + 100) == int(math.sqrt(num + 100)) and math.sqrt(num + 268) == int(math.sqrt(num + 268)):
        lst.append(num)
        flag += 1
        print(num)
    num += 1
print(lst)


# 题目：输入某年某月某日，判断这一天是这一年的第几天？
import datetime
import time
dtstr = str(input('输入一个日期（20170819）：'))
dt = datetime.datetime.strptime(dtstr, '%Y%m%d')
another_dtstr = dtstr[:4] + '0101'
another_dt = datetime.datetime.strptime(another_dtstr, '%Y%m%d')
print(int((dt-another_dt).days) + 1)


#题目：输出9*9口诀。
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d+%d=%d\t" % (j, i, i*j), end="")
    print()


#题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
#　　　后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# ???????????????
hare1 = 1
hare2 = 1
for i in range(1, 12, 2):
    print("%d>>%d" % (hare1, hare2))
    hare1 += hare2
    hare2 += hare1


# 题目：判断101-200之间有多少个素数，并输出所有素数

for i in range(101, 201, 2):
    for j in range(2, int(i/2)+1):
        if i % j == 0:
            break
    else:
        print(i)

# 【程序13】
# 题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数
# 本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。


for i in range(100, 1000):
    a = i % 10
    b = (int(i // 10)) % 10
    c = i // 100
    if (a ** 3) + (b ** 3) + (c ** 3) == i:
        print(i)
'''

