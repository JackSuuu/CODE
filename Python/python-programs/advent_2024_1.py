def calculate_total_distance(left_list, right_list):
    # Step 1: Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Step 2: Calculate pairwise distances
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    
    return total_distance

# Example input
left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 9, 3]

# Calculate and print the total distance
total_distance = calculate_total_distance(left_list, right_list)
print(f"Total distance: {total_distance}")