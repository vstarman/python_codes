def binary_search(item, li):
    """二分查找, 递归实现
    最优时间复杂度：O(1)
    最坏时间复杂度：O(log n)
    :param item: Then element want to find
    :param li: The list
    :return: True or False
    """
    if len(li) == 0:
        return False
    mid_index = len(li) // 2
    if item == li[mid_index]:
        return True
    elif item > li[mid_index]:
        return binary_search(item, li[mid_index+1:])
    else:
        return binary_search(item, li[:mid_index])


def binary_search_1(item, li):
    """二分查找, 非递归实现1
    最优时间复杂度：O(1)
    最坏时间复杂度：O(log n)
    :param item: Then element want to find
    :param li: The list
    :return: Index or False
    """
    # 查找区间的开头/结尾索引
    first = 0
    last = len(li) - 1
    while first <= last:
        mid_index = (first + last) // 2
        if li[mid_index] == item:
            return mid_index
        elif item < li[mid_index]:
            last = mid_index - 1
        else:
            first = mid_index + 1
    return False


def binary_search_2(item, li):
    """二分查找, 非递归实现2
    最优时间复杂度：O(1)
    最坏时间复杂度：O(log n)
    :param item: Then element want to find
    :param li: The list
    :return: True or False
    """
    mid_index = len(li) // 2
    while mid_index > 0:
        if item == li[mid_index]:
            return True
        else:
            if item < li[mid_index]:
                li = li[:mid_index]
            else:
                li = li[mid_index+1:]
            mid_index = len(li) // 2
    return False


if __name__ == '__main__':   
    my_li = [i for i in range(1000)]
    print(binary_search_1(100, my_li))
