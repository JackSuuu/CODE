

test = [3, 1, 2]


def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        curr_num = arr[i]
        curr_index = i
        while curr_num < arr[curr_index - 1] and curr_index > 0:
            arr[curr_index] = arr[curr_index - 1]
            curr_index -= 1
        arr[curr_index] = curr_num
    return arr


print(insertion_sort(test))
