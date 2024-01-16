class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        rows = len(board)
        cols = len(board[0])
        def backtrack(word, board, i,j):
            nonlocal res
            if word == "":
                res = True
                return
            for x,y in ([[0,1], [1,0], [-1, 0], [0,-1]]):
                if(i+x in range(rows) and j+y in range(cols) and board[i+x][j+y] ==word[0]):
                    board[i+x][j+y] = "1"
                    backtrack(word[1:], board, i+x, j+y)
                    board[i+x][j+y] = word[0]
        for i in range(rows):
            for j in range(cols):
                if(board[i][j] == word[0]):
                    board[i][j] = "1"
                    backtrack(word[1:], board, i,j)
                    board[i][j] = word[0]
        return res