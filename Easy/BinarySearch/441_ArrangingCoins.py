class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, h = 1, n
        res = 0  
        while(l<=h):
            mid = (l+h)//2
            val = (mid*(mid+1))/2
            if(n > val):
                l = mid+1
                res= max(mid, res)
            elif(n<val):
                h = mid-1
            else:
                return mid
        return res