class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # keep track of the unique element pos
        j = 1
        for i in range(1, len(nums)):
            # encounter an unique element
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j