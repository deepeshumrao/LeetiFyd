class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive=[]
        for positive_num in nums:
            if positive_num>0:
                positive.append(positive_num)
        negative=[]
        for negative_num in nums:
            if negative_num<0:
                negative.append(negative_num)
        result = []
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
            
        return result