class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if(numRows == 1):
            return [[1]]
        final = [[1]]
        for i in range(2, numRows+1):
            x = [None] * i
            x[0] =1 
            x[-1]= 1
            for j in range(1, len(x)-1):
                x[j]= final[-1][j-1] + final[-1][j] 
            final.append(x)
        return final