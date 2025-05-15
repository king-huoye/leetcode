class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        fangge=[[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                c=board[i][j]
                if c!='.':
                    if c in rows[i] or c in cols[j] or c in fangge[i//3][j//3]:
                        return False
                    rows[i].add(c)
                    cols[j].add(c)
                    fangge[i//3][j//3].add(c)
        return True
