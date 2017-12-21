def binary_search(list1, item):
    """用二分法查询数值"""
    # low & high 用于跟踪要在列表中查找的列表部分
    low = 0
    high = len(list1) - 1

    # 记录步数
    temp = 0
    while low <= high:
        temp += 1
        # 只要范围没有缩小的只包含一个元素,就检查中间元素
        mid = (low + high) // 2
        guess = list1[mid]
        # 找到了该元素
        if guess == item:
            print("搜索%d次查到元素:%d" % (temp, mid))
            return mid, temp
        # 猜的数字大了
        if guess > item:
            high = mid - 1
        # 猜的数字小了
        else:
            low = mid + 1
    # 没有指定元素
    return None


list1 = [i for i in range(1000)]
binary_search(list1, 886)

'''
练习
1.1 假设有一个包含128个名字的有序列表，你要使用二分查找在其中查找一个名字，请
问最多需要几步才能找到？
math.log2(128) = 7
1.2 上面列表的长度翻倍后，最多需要几步？
8

1.3 在电话簿中根据名字查找电话号码。
O(n)
1.4 在电话簿中根据电话号码找人。（提示：你必须查找整个电话簿。）
O(11)
1.5 阅读电话簿中每个人的电话号码。
O(11*n)
1.6 阅读电话簿中姓名以A打头的人的电话号码。这个问题比较棘手，它涉及第4章的概
念。答案可能让你感到惊讶！
O(11*n**2)
'''