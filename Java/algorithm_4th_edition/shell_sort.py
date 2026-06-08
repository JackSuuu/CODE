import random
def shell_sort(arr: list):
    N = len(arr)
    h = 1
    while h < (N/3):
        h = 3 * h + 1
    while h >= 1:
        # h-sort the array
        for i in range(h, N):
            # insert arr[i] among a[i-h]
            j = i
            while j >= h and arr[j] < arr[j-h]:
                arr[j], arr[j-h] = arr[j-h], arr[j]
                j -= h
        h = h//3
    
    return arr

test = [i for i in range(100)]
random.shuffle(test)
print(shell_sort(test))
