class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #需要对所欲边界上的O进行DFS,标记为#
        direction=[[-1,0],[0,-1],[0,1],[1,0]]
        m=len(board)
        n=len(board[0])
        def dfs(x,y):
            if x<0 or x>=m or y<0 or y>=n or board[x][y]!='O':
                return
            board[x][y]='#' #临时标记为不会包围
            for dx,dy in direction:
                dfs(x+dx,y+dy)
        
        for i in range(m):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][n-1]=='O':
                dfs(i,n-1)
        for j in range(n):
            if board[0][j]=='O':
                dfs(0,j)
            if board[m-1][j]=='O':
                dfs(m-1,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='#':
                    board[i][j]='O'
