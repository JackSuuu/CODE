def moveZeroes(nums):
    # Two pointers: i tracks non-zero position, j iterates
    i = 0
    for j in range(len(nums)):
        print(f"i = {i}, j = {j}, nums = {nums}")
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]  # Swap
            i += 1
    return nums

# Test: [0,1,0,3,12] -> [1,3,12,0,0]
print(moveZeroes(nums=[0,1,0,3,12]))