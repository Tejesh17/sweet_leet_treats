class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = "".join([str(i) for i in digits])
        x = int(x)
        x+=1
        return([int(i) for i in str(x)])
        