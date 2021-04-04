class Solution(object):
    def findPeakElement(self, nums):
        highest = 0
        i=1
        temp=0
        if (len(nums)==2):
            if(nums[0]> nums[1]):
                return 0
            else:
                return 1
        if (nums[len(nums)-1]> nums[len(nums)-2]):
            temp = nums[len(nums)-1]
        while i< len(nums)-1:
                
            if ((nums[i]> nums[i+1])  and (nums[i]> nums[i-1])):
                    highest = i
            
            if(nums[highest]<temp):
                highest = len(nums)-1

            i+=1
        return highest