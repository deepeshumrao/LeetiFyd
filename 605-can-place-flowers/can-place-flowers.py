class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Pad with 0s to handle edge cases without extra if-statements
        flowerbed = [0] + flowerbed + [0] 
        count01 = 0
        
        for num in flowerbed:
            if num == 0:
                count01 += 1
                if count01 == 3:
                    n -= 1
                    count01 = 1  # Reset to 1 because the newly planted flower acts as a boundary
            else:
                count01 = 0      # Reset completely when you see a 1
                
        return n <= 0