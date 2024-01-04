class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        res=0
        for i in nums:
            freq[i] = freq.get(i,0)+1
        for i in freq:
            if (freq[i] == 1):
                return -1
            res += freq[i] //3
            if(freq[i]%3):
                res+=1
        return res