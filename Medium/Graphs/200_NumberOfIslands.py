class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        def dfs(i,j):
            if(grid[i][j] == "1"):
                grid[i][j] = "x"
                if(i-1 >=0):
                    dfs(i-1, j)
                if(j-1 >=0):
                    dfs(i, j-1)
                if(i+1 < len(grid)):
                    dfs(i+1, j)
                if(j+1 <len(grid[0])):
                    dfs(i, j+1)
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] =="1"):
                    res+=1
                    dfs(i,j)
        return res