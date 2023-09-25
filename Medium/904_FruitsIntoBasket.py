class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = defaultdict(int)
        i,j=0,0
        resu = 0
        r = 0
        while(j< len(fruits)):
            res[fruits[j]] +=1
            resu+=1
            r  = max(r,resu)
            if(len(res)> 2):
                res[fruits[i]]-=1
                resu-=1
                if(res[fruits[i]] == 0):
                    del res[fruits[i]]
                i+=1
            j+=1
        return (sum(res.values()))