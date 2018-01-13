def insert_sort(li):
    """
    最优时间复杂度：O(n2)
    最坏时间复杂度：O(n2)
    稳定性：不稳定
    :param li: A need sorted list
    :return: None
    """
    # 从第二个位置，即下标为1的元素开始向前插入
    n = 0
    for i in range(1, len(li)):
        # 遍历排序好的
        for j in range(i, 0, -1):
            # 与前边两两比较,遇到大于自己的,就交换位置
            n += 1
            print(n)   # 测试遍历时间
            if li[j] < li[j-1]:
                li[j], li[j - 1] = li[j-1], li[j]
            else:
                # 插入后就退出遍历
                break


if __name__ == '__main__':   
    my_li = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(my_li)
    print(my_li)
