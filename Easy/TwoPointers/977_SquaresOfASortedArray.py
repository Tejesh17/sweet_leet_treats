class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        res = [0 for _ in range(len(nums))]
        x = len(nums)-1
        while(l<=r):
            left = nums[l]**2
            right = nums[r]**2
            if(left >= right):
                res[x] = left
                l +=1
            else:
                res[x] = right 
                r-=1
            x-=1
        return res