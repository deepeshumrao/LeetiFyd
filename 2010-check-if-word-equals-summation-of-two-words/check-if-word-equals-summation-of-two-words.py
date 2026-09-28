class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def alpha2Number(string : str) -> int:
            num=list(string)
            temp=0
            for i in range(len(num)):
                sub=ord(num[i])-ord('a')
                temp=temp*pow(10,len(str(sub)))
                temp+=sub
            return temp
        temp=alpha2Number(firstWord)+alpha2Number(secondWord)
        if temp==alpha2Number(targetWord):
            return True
        return False
