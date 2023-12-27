class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r = []
        def add(target, ar,start):
            if(target ==0):
                ar.sort()
                if ar not in r:
                    r.append(ar.copy())
                return 0
            if(target < 0):
                return 0
            if(target>0):
                for i in range(start,len(candidates)):
                    ar.append(candidates[i])
                    add(target-candidates[i], ar,i)
                    ar.pop()
        candidates.sort()
        add(target, [],0)
        return r