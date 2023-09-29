class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        t=0
        for i in range(len(nums)-1):
            if(nums[i+1]==  nums[i]):
                continue
            if(t==0):
                if(nums[i+1]> nums[i]):
                    t=1
                else:
                    t=2
            else:
                if(nums[i+1]< nums[i] and t ==1):
                    return False
                elif(nums[i+1]> nums[i] and t ==2):
                    return False
        return True