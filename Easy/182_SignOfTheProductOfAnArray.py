class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = nums[0]
        if(nums[0]==0):
            return 0
        for i in range(1, len(nums)):
            if nums[i]==0:
                return 0 
            else:
                 prod *= nums[i]
        if(prod>0):
            return 1
        return -1