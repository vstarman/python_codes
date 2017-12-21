# 寻找列表最频繁的数的
lst1 = [1,2,2,3,4,4,45,5,6,6,6,7,7,8,8,8,5,4,9]
print(max(set(lst1),key=lst1.count))