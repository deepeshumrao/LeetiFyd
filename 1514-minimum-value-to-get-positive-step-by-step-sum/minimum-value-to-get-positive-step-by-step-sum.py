class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        def valid(x):
            for num in nums:
                x += num
                if x < 1:
                    return False
            return True

        l = 1
        r = 100 * len(nums) + 1  
        result = r

        while l <= r:
            mid = (l + r) // 2
            if valid(mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return result