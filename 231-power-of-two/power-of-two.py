class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count=1
        if n<0:
            return False
        while count<=n:
            if count==n:
                return True
            count*=2
        return False