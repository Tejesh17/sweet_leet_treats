# This solution is extremely inefficient hence dosnt pass the leetcode test
# but it works perfectly fine and I'm proud of it because I was able to 
# apply the principles of divide and conquer which I had learnt in class
# and come up with the algorithm on my own

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        row =[0]
        def spl (i):
            if len(i)==1:
                if (i[0]==0):
                    return [0,1]
                else:
                    return [1,0]
            x = spl(i[:len(i)//2])
            j= spl(i[len(i)//2:])
            return x+j
        for _ in range(n):
            row = spl(row)
        return row[k-1]