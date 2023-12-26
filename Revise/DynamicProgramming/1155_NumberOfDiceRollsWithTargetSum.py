class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        cache = {}
        def roll(n,target):
            if n==0:
                return 1 if target ==0 else 0
            if((n, target) in cache):
                return cache[(n,target)]
            res = 0
            for i in range(1, k+1):
                res = (res + roll(n-1, target-i)) % mod
            cache[(n,target)] = res
            return res
        return roll(n, target)