class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        element=None
        count=0
        for i in nums:
            if count==0:
                element=i
                count=1
            elif element==i:
                count+=1
            else:
                count-=1
        CountMajorityElement=nums.count(element)
        if CountMajorityElement>(len(nums)//2):
            return element
        return None