import random

test_arr = [random.randint(1, 10) for _ in range(5)]


# ASCENDING ORDER
def bubble_sort(arr: list):
    sort = False
    for outer in range(len(arr) - 1):
        for inner in range(len(arr) - 1 - outer):
            if arr[inner] > arr[inner + 1]:
                sort = True
                arr[inner], arr[inner + 1] = arr[inner + 1], arr[inner]
        if not sort:
            return arr
    return arr


print(bubble_sort(test_arr))
