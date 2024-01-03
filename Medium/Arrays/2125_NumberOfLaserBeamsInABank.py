class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        num = []
        for row in bank:
            m = 0
            for l in row:
                if(l =="1"):
                    m+=1
            if m>0:
                num.append(m)
        res = 0
        for i in range(len(num)-1):
            res+= num[i]*num[i+1]
        return res