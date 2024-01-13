class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        res = 0
        for i in s_count:
            if(t_count.get(i,0) < s_count[i]):
                res +=s_count[i] - t_count[i]
        return res