def merge_sort_3way(arr):
    """
    Implements a 3-way merge sort algorithm.
    
    Args:
        arr: A list to be sorted
    
    Returns:
        The sorted list
    """
    if len(arr) <= 1:
        return arr
    
    # Divide the array into three parts
    third = len(arr) // 3
    left = merge_sort_3way(arr[:third])
    middle = merge_sort_3way(arr[third:2*third])
    right = merge_sort_3way(arr[2*third:])
    
    # Merge the three sorted parts
    return merge_3way(left, middle, right)

def merge_3way(left, middle, right):
    """
    Merges three sorted arrays into one sorted array.
    
    Args:
        left: First sorted array
        middle: Second sorted array
        right: Third sorted array
        
    Returns:
        A merged sorted array
    """
    merged = []
    i = j = k = 0
    
    # Compare elements from all three arrays and add the smallest to the result
    while i < len(left) and j < len(middle) and k < len(right):
        if left[i] <= middle[j] and left[i] <= right[k]:
            merged.append(left[i])
            i += 1
        elif middle[j] <= left[i] and middle[j] <= right[k]:
            merged.append(middle[j])
            j += 1
        else:
            merged.append(right[k])
            k += 1
    
    # Two arrays might still have elements, let's merge them two at a time
    
    # Left and middle arrays
    while i < len(left) and j < len(middle):
        if left[i] <= middle[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(middle[j])
            j += 1
    
    # Left and right arrays
    while i < len(left) and k < len(right):
        if left[i] <= right[k]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[k])
            k += 1
    
    # Middle and right arrays
    while j < len(middle) and k < len(right):
        if middle[j] <= right[k]:
            merged.append(middle[j])
            j += 1
        else:
            merged.append(right[k])
            k += 1
    
    # Any remaining elements
    while i < len(left):
        merged.append(left[i])
        i += 1
        
    while j < len(middle):
        merged.append(middle[j])
        j += 1
        
    while k < len(right):
        merged.append(right[k])
        k += 1
    
    return merged

# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10, 15, 22, 50]
    print("Original array:", arr)
    sorted_arr = merge_sort_3way(arr)
    print("Sorted array:", sorted_arr)