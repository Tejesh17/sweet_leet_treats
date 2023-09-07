class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        m, n = 1,1
        for i in range(len(nums)-1):
            if(nums[i]+1 == nums[i+1]):
                n +=1
                if(n>m):
                    m = n
            elif (nums[i] == nums[i+1]):
                continue
            else:
                n=1
        if(nums ==[]):
            return 0
        return m