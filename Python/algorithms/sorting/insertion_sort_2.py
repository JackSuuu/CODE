

list1 = [2, 4, 9, 8, 1]

# Perform insertion sort without swapping elements repeatedly
def insertion_sort_new(arr):
    length = len(arr)
    for i in range(0, length):
        current = arr[i]
        for n in range(i, -1, -1):
            if arr[n-1] > current and n > 0:
                arr[n], arr[n-1] = arr[n-1], arr[n]
    return arr


print(insertion_sort_new(list1))
