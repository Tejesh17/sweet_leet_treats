class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a,b,countA,countB = 0,1,0,0
        if nums ==[]:
            return []
        for i in nums:
            if i == a:
                countA+=1
            elif i ==b:
                countB +=1
            elif countA==0:
                a = i
                countA+=1
            elif countB == 0:
                b=i
                countB+=1
            else:
                countA-=1
                countB -=1
        return [ x for x in (a,b) if nums.count(x)> len(nums)//3]