class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
       peak=max(nums)
       i=nums.index(peak)
       return i