class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(dots, s, reminder):
            nonlocal res
            if (dots == 3):
                if(len(reminder)==1):
                    s+= reminder
                    if(s not in res):
                        res.append(s)
                elif(int(reminder) >=0 and int(reminder)<=255 and reminder[0] !="0"):
                    s+=reminder
                    if(s not in res):
                        res.append(s)
                return 
            for i in range(1,len(reminder)):
                if(int(reminder[:i]) >=1 and int(reminder[:i])<=255 and reminder[0] !="0"):
                    backtrack(dots+1, s+ reminder[:i]+".", reminder[i:])
                elif(reminder[0] == "0"):
                    backtrack(dots+1, s + "0.", reminder[1:])
        backtrack(0, "", s)
        return res