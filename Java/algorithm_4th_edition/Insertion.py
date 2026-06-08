
def insertion_sort(arr: list):
    N = len(arr)
    for i in range(1, N):
        j = i
        while j>0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    
    return arr

print(insertion_sort([5, 2, 4, 3, 1]))
