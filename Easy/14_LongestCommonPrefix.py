class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        counter= 0
        output=""
        shortest = min(strs, key=len)
        while counter < len(shortest):
            for word in strs:
                if word[counter] != shortest[counter]:
                    return output
            output += shortest[counter]
            counter+=1
        return output