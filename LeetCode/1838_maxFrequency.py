
# URL: https://leetcode.com/problems/frequency-of-the-most-frequent-element/


def maxFrequency(nums: list[int], k: int):
    nums.sort()
    left = 0
    freq = 0
    curr = 0

    for right in range(len(nums)):
        target = nums[right]
        curr += target

        while (right - left + 1) * target - curr > k:
            curr -= nums[left]
            left += 1

        freq = max(freq, right - left + 1)

    return freq


# ex_1 -> expected output: 3
nums = [1, 4, 8, 13]
k = 5

print(maxFrequency(nums, k))

