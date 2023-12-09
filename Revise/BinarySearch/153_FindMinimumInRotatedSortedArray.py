class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        res = nums[(l+h)//2]
        while(l <=h ):
            if(nums[h]>= nums[l] ):
                return min(nums[l],res)
            mid = (l+h)//2
            res = min(res, nums[mid])
            if(nums[mid]>=nums[l]):
                l = mid + 1
            else:
                h = mid -1
        return res