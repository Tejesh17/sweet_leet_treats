class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = []
        for i in points:
            x.append(i[0])
        x.sort()
        low= 0
        for i in range(len(x)-1):
            low = max(x[i+1] - x[i] , low)
        return low 
