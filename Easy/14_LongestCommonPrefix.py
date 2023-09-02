class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        counter= 0
        output=""
        shortest = min(strs, key=len)
        while counter < len(shortest):
            localCounter = 0
            for word in strs:
                if word[counter] == shortest[counter]:
                    localCounter +=1
            if(localCounter == len(strs)):
                output += shortest[counter]
            else:
                return output
            counter+=1
        return output