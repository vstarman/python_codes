def shell_sort(li):
    """希尔排序:效率与步长有关
    最优时间复杂度：根据步长序列的不同而不同
    最坏时间复杂度：O(n2)
    稳定性：不稳定
    :param li: A need sorted list
    :return: None
    """
    n = len(li)
    # 初始步长
    gap = n // 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            # 插入排序
            j = i
            while j >= gap and li[j-gap] > li[j]:
                li[j-gap], li[j] = li[j], li[j-gap]
                j -= gap
        # 新步长
        gap //= 2


def shell_sort_1(li):
    count = len(li)
    step = 2
    group = count // step
    while group > 0:
        # 一共需排序group次
        for i in range(0, group):
            # 每组元素的下标
            j = i + group
            # 当下标没有超出列表长度
            while j < count:
                k = j - group
                key = li[j]
                while k >= 0:
                    if li[k] > key:
                        li[k+group] = li[k]
                        li[k] = key
                    k -= group
                j += group
        group //= step


if __name__ == '__main__':   
    my_li = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    shell_sort_1(my_li)
    print(my_li)
