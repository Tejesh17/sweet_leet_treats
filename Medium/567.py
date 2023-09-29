class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        i=0
        for j in range(len(s2)):
            if(j-i > len(s1)-1):
                if(s2[i] in count   ):
                    count[s2[i]]+=1
                i+=1
            if(s2[j] in count ):
                count[s2[j]] -=1
                if(all(value == 0 for value in count.values())):
                    return True
        return False