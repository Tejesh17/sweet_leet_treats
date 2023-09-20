class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        leftS = 0
        for i in range(len(nums)):
            rightS = tot - leftS - nums[i]
            if(leftS == rightS):
                return i
            leftS += nums[i]
        return -1