class Solution:
    def isPalindrome(self, s: str) -> bool:
        resstr=""
        lower=s.lower()
        for ch in lower:
            if ch.isalnum():
                resstr+=ch
        return resstr==resstr[::-1]