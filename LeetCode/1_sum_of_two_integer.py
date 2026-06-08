from typing import List

nums_arr = [3, 2, 3]
target_sum = 6


# using linear for to achieve the algorithm
def pPlus(nums, target):
    left = 0
    right = len(nums) - 1
    left_num = 0
    right_num = 0
    result = []
    seq = nums.copy()
    seq.sort()

    for i in range(len(seq)):
        if seq[left] + seq[right] == target:
            left_num = seq[left]
            right_num = seq[right]
            break
        if seq[left] + seq[right] > target:
            right -= 1
        else:
            left += 1

    for n in range(len(nums)):
        if left_num == right_num and nums[n] in (left_num, right_num):
            result.append(n)
        else:
            if nums[n] == left_num:
                result.append(n)
            if nums[n] == right_num:
                result.append(n)
    return result


print(pPlus(nums_arr, target_sum))


# 哈希映射
def twoSum(nums: List[int], target: int):
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
        print(hashtable)
    return []


print(twoSum(nums_arr, target_sum))
