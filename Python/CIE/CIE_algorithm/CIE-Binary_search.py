test_arr = [1, 2, 3, 4, 5]


# ARRAY MUST BE SORTED
def binarySearch(arr: list, item):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if item == arr[mid]:
            return "index is: " + str(mid)
        elif item > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1


print(binarySearch(test_arr, 5))
