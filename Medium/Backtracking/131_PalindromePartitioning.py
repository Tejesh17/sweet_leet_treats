class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(s, ar):
            nonlocal res
            if s == "":
                if(len(ar)>0):
                    res.append(ar.copy())
                return 
            for i in range(1,len(s)+1):
                if(s[:i] == s[:i][::-1]):
                    ar.append(s[:i])
                    backtrack(s[i:], ar)
                    ar.pop()
        backtrack(s, [])
        return res