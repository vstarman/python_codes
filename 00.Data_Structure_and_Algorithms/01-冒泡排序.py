def bubble_sort(li):
    """冒泡排序"""
    # 遍历列表元素
    n = len(li)
    # 遍历n-1次, 每次冒泡一个最大值到最后
    num = 0
    for e in range(n-1, 0, -1):
        # 1.每次遍历都将最大值换到最后
        for i in range(e):
            num += 1
            print(num)
            # 2.循环比较相邻两个元素大小
            if li[i] > li[i+1]:
                # 3.如果大于后者,交换位置
                li[i], li[i+1] = li[i+1], li[i]
    # 直至没有元素需要比较


if __name__ == '__main__':
    my_list = [109, 3, 33, 22, 14, 88, 39, 37, 99, 37]
    bubble_sort(my_list)
    print(my_list)
    # bubble_sort(my_list)
    # print(my_list)
    # bubble_sort(my_list)
    # print(my_list)
    # bubble_sort(my_list)
    # print(my_list)