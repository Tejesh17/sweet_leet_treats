class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = defaultdict(int)
        l=0
        i=0
        for j in range(len(s)):
            if(h[s[j]] >0):
                while(s[i] != s[j]):
                    h[s[i]] -=1
                    i+=1
                h[s[i]]-=1
                h[s[j]]+=1
                i+=1
            else:
                h[s[j]]+=1
            l = max(l,sum(h.values()))
        return l