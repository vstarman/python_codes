def quick_sort_1(li):
    """要占用新内存,空间消耗大
    最优时间复杂度：O(nlogn)
    最坏时间复杂度：O(n2)
    稳定性：不稳定
    :param li: A need sorted list
    :return: None
    """
    if len(li) < 2:
        return li
    point = li[0]
    less = [i for i in li[1:] if i <= point]
    greater = [i for i in li[1:] if i > point]
    return quick_sort_1(less) + [point] + quick_sort_1(greater)


def quick_sort(li, start, end):
    """修改原列表,空间消耗小
    最优时间复杂度：O(nlogn)
    最坏时间复杂度：O(n2)
    稳定性：不稳定
    :param li: A need sorted list
    :param start: Start index
    :param end: End index
    :return: 
    """
    # 递归的退出条件
    if start >= end:
        return
    # 设定起始元素为要寻找位置的基准元素
    mid = li[start]
    # low为序列左边的由左向右移动的游标
    low = start
    # high为序列右边的由右向左移动的游标
    high = end

    # 循环一次将列表分为三部分
    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and li[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        li[low] = li[high]
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and li[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        li[high] = li[low]
    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    li[low] = mid
    # 对基准元素左边的子序列进行快速排序
    quick_sort(li, start, low - 1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort(li, low + 1, end)


if __name__ == '__main__':   
    my_li = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(my_li, 0, len(my_li) - 1)
    print(my_li)
