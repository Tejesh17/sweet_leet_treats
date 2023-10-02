class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = {}
        i=res=0
        for j in range(len(s)):
            l[s[j]] = 1+ l.get(s[j],0)
            if( (j-i+1)- max(l.values()) > k ):
                l[s[i]] -= 1
                i+=1
            res = max(j-i+1, res)
        return res