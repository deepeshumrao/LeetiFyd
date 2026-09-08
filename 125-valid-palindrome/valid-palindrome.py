class Solution:
    def isPalindrome(self, s: str) -> bool:
        resstr=""
        lower=s.lower()
        for ch in lower:
            if ch.isalpha() or ch.isdigit():
                resstr+=ch
        return resstr==resstr[::-1]