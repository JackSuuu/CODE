
arr = [5, 3, 2, 0, 7]


def reverse_selection_sort(alist):
    for i in range(0, len(alist)):
        max_value = alist[len(alist) - i - 1]
        max_index = len(alist) - i - 1
        for j in range(len(alist)-i-1, -1, -1):
            if alist[j] > max_value:
                max_value = alist[j]
                max_index = j
        alist[len(alist) - i - 1], alist[max_index] = alist[max_index], alist[len(alist) - i - 1]
    return alist


print(reverse_selection_sort(arr))
