class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1 ,len(s)):
            a = s.count("0", 0, i)
            b = s.count("1", i, len(s))
            res= max(res, a+b)
        return res