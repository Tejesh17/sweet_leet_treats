class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        seen = {}
        for i in range(len(s)):
            if(s[i] in seen):
                res = max(i-seen[s[i]]-1, res)
            else:
                seen[s[i]] = i
        return res