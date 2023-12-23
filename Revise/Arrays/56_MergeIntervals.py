class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i=0
        print(intervals)
        res = []
        while i< len(intervals):
            low = intervals[i][0]
            high = intervals[i][1]
            while(i< len(intervals)-1 and intervals[i+1][0] <= high ):
                high = max(intervals[i+1][1], high)
                i+=1
            else:
                i+=1
            res.append([low, high])
        return res