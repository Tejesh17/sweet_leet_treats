class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0
        for num in nums:
            if(num-1 not in numsSet):
                length = 1
                while(num+1 in numsSet):
                    num +=1
                    length +=1
                res = max(res, length)
        return res
