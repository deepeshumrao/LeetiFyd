class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        
        
        def help(idx,nums,temp,res):
            if idx>=len(nums):
                res.append(temp[:])
                return
            
            temp.append(nums[idx])
            help(idx+1,nums,temp,res)
            
            temp.pop()
            help(idx+1,nums,temp,res)
        res=[]
        help(0,nums,[],res)
        return res
        