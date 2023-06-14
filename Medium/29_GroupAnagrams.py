class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Hash = {}
        for i in range(len(strs)):
            l = sorted(strs[i])
            jsonword = str(json.dumps(l))
            if(jsonword in Hash):
                Hash[jsonword].append(i)
            else:
                Hash[jsonword] = [i]
        final= []
        for key in Hash:
            new = []
            for words in Hash[key]:
                new.append(strs[words])
            final.append(new)
        return(final)
