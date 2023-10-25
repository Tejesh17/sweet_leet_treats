class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for i in range(len(nums)):
            if(nums[i] == 0 ):
                count+=1
            elif count > 0:
                res =res+ int((count * (count+1))/2)
                count=0
        if(count>0):
                res =res+  int((count * (count+1))/2)
        return res