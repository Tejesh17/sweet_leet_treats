class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = False
        for i in range(len(nums)-1):
            if(nums[i] <= nums[i+1] ):
                continue
            if flag:
                return False
            if(i!=0 and nums[i+1]< nums[i-1]):
                nums[i+1] = nums[i]
            else:
                nums[i] = nums[i+1]
            flag = True
        return True