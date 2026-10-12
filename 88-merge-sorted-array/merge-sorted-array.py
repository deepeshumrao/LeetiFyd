class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(n):
            nums1[i+m]=nums2[i]
        nums1.sort()
        return nums1