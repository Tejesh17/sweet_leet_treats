class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i=0
        s=0
        l=1
        nums.sort()
        for j in range(1, len(nums)):
            s+=nums[j-1]
            if((((j-i)*nums[j]) - s) >k):
                s-=nums[i]
                i+=1
            print(i,j)
            l = max(l, j-i+1)
        return l 