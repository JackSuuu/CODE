

def quickSort(arr, lo, hi):
    if (hi <= lo):
        return
    j = partition(arr, lo, hi)
    quickSort(arr, lo, j-1)
    quickSort(arr, j+1, hi)

def partition(arr, lo, hi):
    # Partition into arr[lo..i-1], arr[i], arr[i+1..hi].
    i = lo
    j = hi
    # left and right scan indices
    v = arr[lo]  # partitioning item

    # focus on the structure, 
    # it looks like binary search
    while True:
        # Scan right, scan left, 
        # check for scan complete, and exchange.
        while (arr[i] <= v):
            i += 1
            if i == hi:
                break
        while (v <= arr[j]):
            j -= 1
            if j == lo:
                break
        if i >= j:
            break
        # Exchange elements at indices i and j
        arr[i], arr[j] = arr[j], arr[i]

    # Put v = arr[j] into position
    arr[lo], arr[j] = arr[j], arr[lo]
    return j  # with arr[lo..j-1] <= arr[j] <= arr[j+1..hi]

# Helper functions used in the partition function
def less(a, b):
    return a < b

def exch(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

test = [10, 1, 8, 9, 2, 3]
quickSort(test, 0, len(test)-1)
print(test)