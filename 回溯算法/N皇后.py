class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int, cols: set, diag1: set, diag2: set, board: List[List[str]]):
            # 如果所有皇后都已放置，返回结果
            if row == n:
                result.append([''.join(r) for r in board])  # 将 board 列表转换为字符串列表
                return
            
            # 尝试在当前行的每一列放置一个皇后
            for col in range(n):
                # 检查列和对角线是否有冲突
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                # 放置皇后并标记该列和对角线
                board[row][col] = 'Q'  # 在当前行的指定列放置皇后
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # 递归处理下一行
                backtrack(row + 1, cols, diag1, diag2, board)
                
                # 回溯，移除皇后并取消标记
                board[row][col] = '.'  # 移除皇后
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        result = []
        # 初始化一个 n x n 的棋盘，全部为空（'.'）
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return result
