class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        IndexList=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                s=nums[i]+nums[j]
                if s==target:
                    IndexList.append(i)
                    IndexList.append(j)
                else:
                    ...
        return IndexList