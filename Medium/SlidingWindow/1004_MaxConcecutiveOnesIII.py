class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=0
        res = 0
        x =0
        for j in range(len(nums)):
            if(nums[j] ==1 ):
                res = max(res, j-i+1)
                continue
            if(nums[j] != 1 and x <k):
                x+=1
            else:
                if(nums[j] ==0):
                    x+=1
                while(x>k):
                    if(nums[i] != 1):
                        x-=1
                    i+=1
            res = max(res, j-i+1)
        return res