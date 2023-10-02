class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        i,j = 0, len(nums)-1
        while len(res) != len(nums):
            res.append(nums[i])
            i+=1
            if( i<= j):
                res.append(nums[j])
                j-=1
        return res