class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0:0, 1:1, 2:2}
        def climb(n):
            if n in cache:
                return cache[n]
            x = climb(n-1)
            y = climb(n-2)
            cache[n] = x+y
            return cache[n]
        return climb(n)