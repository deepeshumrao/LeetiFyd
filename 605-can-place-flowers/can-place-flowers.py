class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0] 
        count01 = 0
        
        for num in flowerbed:
            if num == 0:
                count01 += 1
                if count01 == 3:
                    n -= 1
                    count01 = 1
            else:
                count01 = 0    
        return n <= 0