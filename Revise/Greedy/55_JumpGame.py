class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, m = 0,0
        while(i < len(nums)):
            m = max(m, i+ nums[i])
            if(m>= len(nums)-1):
                return True
            if i >= m and nums[i] ==0:
                return False
            i+=1
        return False