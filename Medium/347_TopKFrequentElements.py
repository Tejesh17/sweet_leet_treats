class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] =1+ d.get(num, 0)
        i=0
        res=[]
        while(i<k):
            n = max(d, key=d.get)
            res.append(n)
            del d[n]
            i+=1
        return res