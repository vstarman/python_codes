'''import gevent,time
from gevent import monkey
monkey.patch_all()


def f(n):
    for i in range(n):
        time.sleep(0.1)
        print(gevent.getcurrent(), i)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()

import random
mylist = []
while True:
	mylist.append(random.randint(1,10))
	if len(set(mylist)) == 10:
		print(set(mylist))
		break
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#要求：把一个list分成若干等分，合成一个2维数组
numbers = []

def num_list():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    while len(a) > 0:
        b = []
        b.append(a.pop())
        b.append(a.pop())
        numbers.append(b)
        print(a)
        print(b)
        print(numbers)

if __name__ == '__main__':
    num_list()


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst1 = []
lst2 = []
for i in a:
    if i%2 != 0:
        lst1.append(i)
    else:
        lst2.append(i)
print(lst1)
print(lst2)

lst = [5,3,1,5,7,9,3,4,2,2,7]
lst1 = []
lst1.append(lst.pop())
while len(lst) > 0:
    lst_num = lst.pop()
    for num in lst1:
        print(num)
        if lst_num <= num:
            index = lst1.index(num)
            print(index)
            lst1.insert(index, lst_num)

            print(lst1)
            break
    else:
        lst1.append(lst_num)
import random
lst = [random.randint(1,1500) for i in range(1500)]
lst1 = []
lst1.append(lst.pop())
while len(lst) > 0:
    lst_num = lst.pop()
    for num in lst1:
        if lst_num <= num:
            index = lst1.index(num)
            lst1.insert(index, lst_num)
            break
    else:
        lst1.append(lst_num)
print(lst1)
enumerate'''

