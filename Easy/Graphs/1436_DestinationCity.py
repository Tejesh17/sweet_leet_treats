class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = set()
        dest = set()
        for i in paths:
            for j in range(len(i)):
                if(j==0):
                    source.add(i[j])
                else:
                    dest.add(i[j])

        return list(dest-source)[0]