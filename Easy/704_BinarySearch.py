class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0; r = len(nums)-1

        def binaryS(l,r):
            mid = floor((l+r)/2)
            if(l >= r):
                if(target == nums[l] ):
                    return mid
                else:
                    return -1
            elif(target == nums[mid]):
                return (mid)
            elif (target > nums[mid]):
                return binaryS(mid+1, r)
            elif(target< nums[mid]):
                return binaryS(l, mid-1)
        num = binaryS(0, r)
        return num