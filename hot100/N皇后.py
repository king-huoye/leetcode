class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result=[]
        def backtracking(board,row,cols,dig1,dig2):
            if row==n:
                self.result.append([''.join(r) for r in board])
            for col in range(n):
                if col in cols or row-col in dig1 or row+col in dig2:
                    continue
                board[row][col]='Q'
                cols.add(col)
                dig1.add(row-col)
                dig2.add(row+col)
                backtracking(board,row+1,cols,dig1,dig2)
                board[row][col]='.'
                cols.remove(col)
                dig1.remove(row-col)
                dig2.remove(row+col)
        board=[['.']*n for _ in range(n)]
        backtracking(board,0,set(),set(),set())
        return self.result
