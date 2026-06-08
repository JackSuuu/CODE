

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
target = [0, 1, 2, 3]
k_ans = 3


def remove_duplicate(nums: list):
    temp = nums[0]
    for each in nums:
        if each != temp:
            nums[nums.index(temp) + 1] = each
            temp = each
    k = nums.index(temp) + 1
    return k, nums


print(remove_duplicate(nums))
