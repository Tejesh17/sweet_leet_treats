class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        l = len(nums)
        i = 0
        m=0
        while i< len(nums):
            if(seen.get(nums[i], 0) == 0):
                seen[nums[i]] = 1
                i+=1
            elif seen[nums[i]] <2 :
                seen[nums[i]] = 2
                i+=1
            else:
                nums.pop(i)
        while m < l:
            nums.append("_")
            m+=1
        return sum(seen.values())