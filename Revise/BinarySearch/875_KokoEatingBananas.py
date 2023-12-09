class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkBananas(n):
            hours, i, eat = 0, 0, 0
            while(i< len(piles)):
                if(piles[i]%n == 0):
                    hours += piles[i]/n
                else:
                    hours += (piles[i]//n)+1
                i+=1
            return (hours<= h)
            
        l,hi,res = 1, max(piles), 1
        while(l<=hi):
            mid = (l+hi)//2
            if(checkBananas(mid)):
                hi = mid-1
                res = mid
            else:
                l = mid+1
        return res