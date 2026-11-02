class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        if n<0:
            return False
        str_list=list(str(bin(n)))
        c=str_list.count("1")
        if c==1:
            return True
        return False