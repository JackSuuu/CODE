class Solution:
    def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        
        l = 0
        r = len(nums)

        mid = ((l + r) / 2)

        print(l, r, mid)

        if (mid % 2) != 0 and int(mid) != 1:
            return float(nums[int(mid)])
        else:
            return (nums[int(mid)-1] + nums[int(mid)]) / 2


print(Solution.findMedianSortedArrays([], [2, 3]))
