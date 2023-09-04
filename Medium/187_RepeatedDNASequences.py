class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()
        for i in range(len(s)-9):
            st = s[i: i+10]
            if(st in seen):
                res.add(st)
            seen.add(st)
        return list(res)