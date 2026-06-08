import random

test_arr = [random.randint(1, 10) for _ in range(5)]


# insertion sort optimize edition
# ASCENDING ORDER
# 内循环将大于 curr_num 的数字逐步向右移动
def insertionSort(alist):
    for i in range(1, len(alist)):
        curr_num = alist[i]
        curr_index = i
        while alist[curr_index - 1] > curr_num and curr_index > 0:
            alist[curr_index] = alist[curr_index - 1]
            curr_index -= 1
        alist[curr_index] = curr_num
    return alist


print(insertionSort(test_arr))
