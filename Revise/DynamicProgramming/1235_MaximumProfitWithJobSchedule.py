class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        cache = {}
        def helper(i):
            if(i == len(startTime)):
                return 0 
            if(i in cache):
                return cache[i]

            res = helper(i+1)

            j = bisect.bisect(jobs, (jobs[i][1], -1,-1))

            cache[i] = res = max(res, jobs[i][2] + helper(j))
            return res
        return helper(0) 