class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lettersHash={}
        words = s.split()
        if(len(words)!=len(pattern)):
            return False
        for i, l in enumerate(pattern):
            if(l not in lettersHash and words[i] not in lettersHash.values()):
                lettersHash[l] = words[i]
            elif(words[i] in lettersHash.values() and l not in lettersHash):
                return False
            elif(words[i]!= lettersHash[l]):
                return False 
        return True