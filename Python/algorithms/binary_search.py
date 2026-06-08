
arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 3


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while True:
        mid = int((left + right) / 2)
        if arr[mid] == target:
            out = f"target is {target}, index is {mid}"
            return out
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        if right < left:
            break


print(binary_search(arr, target))
