import numpy as np

def bucket_sort(arr, bucket_size=5):
    if len(arr) == 0:
        return arr
    
    # Determine minimum and maximum values
    min_val, max_val = min(arr), max(arr)
    
    # Calculate the number of buckets
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    
    # Distribute elements into buckets
    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[index].append(num)
    
    # Sort each bucket and concatenate results
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))
    
    return sorted_array

# Example usage
if __name__ == "__main__":
    np.random.seed(42)
    arr = np.random.randint(1, 100, 10).tolist()  # Generate random numbers
    print("Original array:", arr)
    sorted_arr = bucket_sort(arr, bucket_size=10)
    print("Sorted array:", sorted_arr)