test_arr_2 = [0, 1, 2, 3, 4, 5, 6]


def binarySearch_recursion(alist: list, left, right, x):
    # base case
    if left <= right:
        mid = (left + right) // 2

        if x < alist[mid]:
            # if 5.5 = 5, it needs to minus 1 in order to move left
            return binarySearch_recursion(alist, left, mid - 1, x)

        # else the element can only be present in right subarray
        elif x > alist[mid]:
            # if 5.5 = 5, it needs to add 1 in order to move right
            return binarySearch_recursion(alist, mid + 1, right, x)

        # else x equals to the mid, return index
        elif x == alist[mid]:
            return mid

    else:
        return -1


print(binarySearch_recursion(test_arr_2, 0, 6, 5))
