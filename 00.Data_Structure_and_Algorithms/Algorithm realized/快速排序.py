test = [3, 4, 12312, 3, 412, 12, 123, 2]


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
