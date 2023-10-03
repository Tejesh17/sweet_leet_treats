class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        s = 0
        count = {}
        for i in range(len(nums)):
            if(nums[i] in count):
                s+= count[nums[i]]
            count[nums[i]] = count.get(nums[i],0)+1    
        return s