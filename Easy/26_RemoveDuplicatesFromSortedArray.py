class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = set()
        m=0
        l = len(nums)
        i=0
        while(i< len(nums)):
            if(nums[i] in k):
                nums.pop(i)
            else:
                k.add(nums[i])
                i+=1
        while m < l:
            nums.append("_")
            m+=1
        return len(k)