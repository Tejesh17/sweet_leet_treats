class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        frequency = {}
        for i in nums:
            frequency[i] = frequency.get(i,0) +1
        res = []
        while frequency:
            temp = []
            for i in frequency:
                temp.append(i)
                frequency[i]-=1
            for i in nums:
                if i in frequency and frequency[i] ==0:
                    del frequency[i]
            res.append(temp)
        return res