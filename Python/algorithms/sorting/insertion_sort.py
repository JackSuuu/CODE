# insertion sort algorithm
# Assume the left part of the array is sorted,
# so iterate the current item back-way and insert the correct position
list1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        while arr[i-1] > curr and i > 0:
            print(f"{arr[i-1]} compare with {arr[i]}")
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1

    return arr


print(insertion_sort(list1))
