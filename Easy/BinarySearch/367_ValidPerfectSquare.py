class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,h = 0,num
        while(l<=h):
            mid = (l+h)//2
            if(mid**2 < num):
                l= mid+1
            elif(mid **2 > num):
                h = mid -1
            else:
                return True
        return False