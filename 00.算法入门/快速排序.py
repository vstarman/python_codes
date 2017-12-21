test = [3, 4, 12312, 3, 412, 12, 123, 2]

# def sum_list(test):
#     if len(test) == 0:
#         return 0
#     else:
#         return test.pop() + sum_list(test)
#
#
# result = sum_list(test)
# print(result)


'''
def sort_list(lst):
    if len(lst) < 2:
        return lst
    else:
        value = lst.pop()
        mid_lst = [value]
        min_lst = list()
        max_lst = list()
        for i in lst:
            if i < value:
                min_lst.append(i)
            elif i > value:
                max_lst.append(i)
            else:
                mid_lst.append(i)
        return sort_list(min_lst) + mid_lst + sort_list(max_lst)
b = sort_list(test)
print(b)'''


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

sort_list = quick_sort(test)
print(sort_list)
