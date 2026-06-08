import random
import numpy as np


def sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        # Just use the + operator to join lists
        return sort(less)+equal+sort(greater)
    # Note that you want equal ^^^^^ not pivot
    # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
    else:
        return array


test_arr = np.arange(10)
random.shuffle(test_arr)

print(sort(test_arr))
# test_arr.max()
# print(test_arr)
