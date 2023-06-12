class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0]+flowerbed+[0]
        possibleflowers = 0
        for i in range(1, len(flowerbed)-1):
            if(flowerbed[i-1] == 0 and flowerbed[i]==0 and flowerbed[i+1]==0):
                possibleflowers+=1
                flowerbed[i] =1
        return(possibleflowers>=n)