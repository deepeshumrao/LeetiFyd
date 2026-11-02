class Solution:
    def hammingWeight(self, n: int) -> int:
        n=list(str(bin(n)))
        return n.count("1")
