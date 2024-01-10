class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        def add(ar, i):
            nonlocal res
            while(i< len(nums)):
                ar.append(nums[i])
                if(ar.copy() not in res):
                    res.append(ar.copy())
                add(ar, i+1)
                i+=1
                ar.pop()
        add([], 0)
        return res