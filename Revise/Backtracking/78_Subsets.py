class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def generate(ar, i):
            nonlocal res
            while(i< len(nums)):
                ar.append(nums[i])
                res.append(ar.copy())
                generate(ar, i+1)
                i+=1
                ar.pop()
        generate([], 0)
        return res