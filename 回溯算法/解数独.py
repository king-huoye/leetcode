class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def isValid(row, col, val, board):
            # Check row
            for i in range(9):
                if board[row][i] == val:
                    return False
            # Check column
            for j in range(9):
                if board[j][col] == val:
                    return False
            # Check 3x3 sub-grid
            start_row, start_col = (row // 3) * 3, (col // 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == val:
                        return False
            return True
        
        def backtracking(board):
            # Try to fill each cell
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == '.':  # If the current cell is empty
                        # Try each number from 1 to 9
                        for num in range(1, 10):
                            char = str(num)
                            if isValid(i, j, char, board):  # If it's valid to put 'char' in board[i][j]
                                board[i][j] = char  # 填数字
                                if backtracking(board):  # Recursively attempt to solve the rest
                                    return True
                                board[i][j] = '.'  # 回退
                        return False  # 九个数都试完了
            return True  # 说明找到棋盘合适的位置
        
        backtracking(board)
