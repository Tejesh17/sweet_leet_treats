class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = {}
        default = len(wall)
        for w in wall:
            s = 0
            for b in w:
                s = s+b
                if(sum(wall[0])!= s):
                    gaps[s] = 1+ gaps.get(s,0)
        m = (max(list(gaps.values()), default =0))
        return default - m