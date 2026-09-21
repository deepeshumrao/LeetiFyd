class Solution:
    def palindrome(self,s,i,j):
            while(i<j):
                if(s[i]!=s[j]):
                    return False
                i+=1
                j-=1
            return True


    def validPalindrome(self, s: str) -> bool:
        n=len(s)
        i=0;j=n-1
        flag=True
        while(i<j):
            if s[i]!=s[j]:
                return self.palindrome(s,(i+1),j) or self.palindrome(s,i,(j-1))
            else:
                i+=1
            j-=1
        return True