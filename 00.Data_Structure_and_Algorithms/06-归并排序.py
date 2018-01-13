def merge_sort(li):
    """归并排序
    最优时间复杂度：O(nlogn)
    最坏时间复杂度：O(nlogn)
    稳定性：稳定
    :param li: A need sorted list
    :return: None
    """
    if len(li) <= 1:
        return li
    # 二分分解
    num = len(li) // 2
    left = merge_sort(li[:num])
    right = merge_sort(li[num:])
    # 合并
    return merge(left, right)


def merge(left, right):
    """
    合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组
    :param left: array left
    :param right: array right
    :return: sorted list
    """
    # left与right的下标指针
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # 将剩余的列表添加到后边
    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':   
    my_li = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    print(merge_sort(my_li))
