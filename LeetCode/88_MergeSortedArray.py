class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for j in range(n):
            nums1[m+j] = nums2[j]
        nums1.sort()

nums1 = [1,2,3,0,0,0] 
m = 3 
nums2 = [2,5,6]
n = 3

Solution().merge(nums1, m, nums2, n)
print(nums1)