class Solution:
    def integerBreak(self, n: int) -> int:
        p = 0
        for i in range(2,n+1):
            res = [n//i] * i
            reminder = n%i
            for i in range(reminder):
                res[i]+=1
            localp = functools.reduce(operator.mul, res, 1)
            p = max(localp, p)
        return p