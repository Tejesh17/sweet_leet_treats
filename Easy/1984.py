class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if(len(nums)==1):
            return 0
        nums.sort()
        i=0
        low = nums[k-1] - nums[0]
        for j in range(0, len(nums)):
            if(j-i >k-1):
                i+=1
                low = min(low, nums[j]- nums[i])
        return low