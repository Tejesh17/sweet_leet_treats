class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio = []
        res = 0
        m = {}
        for i in rectangles:
            d = i[0]/i[1]
            ratio.append(d)
            m[d] = m.get(d,0) +1
        for i in ratio:
            res+= m[i]-1
            m[i]-=1
        return res