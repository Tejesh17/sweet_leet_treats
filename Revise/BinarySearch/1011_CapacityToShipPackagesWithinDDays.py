class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checkCapacity(n):
            we= 0
            count = 0
            for w in weights:
                we+=w
                if(we > n):
                    count +=1
                    we = 0
                    we+=w
            return count < days

        l,h = max(weights), sum(weights)
        res = 0
        while(l<=h):
            mid = (l+h)//2
            if(checkCapacity(mid)):
                res = mid
                h= mid -1
            else:
                l = mid+1
        return res