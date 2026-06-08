
arr = [10, 3, 5, 8, 1, 2]


# Selection Sort 的基本思想为每次找到最小的，将最小值插入对应位置
def selection_sort(a_list: list):
    for i in range(0, len(a_list) - 1):
        min_value = a_list[i]
        index = i
        for j in range(i+1, len(a_list)):
            if a_list[j] < min_value:
                min_value = a_list[j]
                index = j
        a_list[i], a_list[index] = a_list[index], a_list[i]

    return a_list


# print(selection_sort(arr))


# A simplify version of Selection Sort
def find_min(array):
    min_val = arr[0]
    min_index = 0
    for i in range(len(array)):
        if min_val > array[i]:
            min_val = array[i]
            min_index = i
    return min_index


def selection_sort_op(ar: list):
    res_arr = []
    for j in range(len(ar)):
        min_item = ar.pop(find_min(ar))
        res_arr.append(min_item)
    return res_arr


print(selection_sort_op(arr))
