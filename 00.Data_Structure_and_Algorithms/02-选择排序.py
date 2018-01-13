def select_sort(li):
    """
    最优时间复杂度：O(n2)
    最坏时间复杂度：O(n2)
    稳定性：不稳定
    :param li: A need sorted list
    :return: None
    """
    n = len(li)
    # 需要进行n-1次选择操作
    for i in range(n-1):
        # 记录最小位置
        min_index = i
        # 从i+1位置到末尾选择出最小数据
        for j in range(i+1, n):
            if li[j] < li[min_index]:
                min_index = j
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            li[i], li[min_index] = li[min_index], li[i]


if __name__ == '__main__':   
    my_li = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    select_sort(my_li)
    print(my_li)
