class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        def count(x,y):
            directions=[(-1,0),(0,-1),(0,1),(1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
            count=0
            for dx,dy in directions:
                newx,newy=x+dx,y+dy 
                if 0<=newx<m and 0<=newy<n and abs(board[newx][newy])==1:
                    count+=1
            return count
        for i in range(m):
            for j in range(n):
                live=count(i,j)
                if board[i][j]==1 and (live<2 or live>3):
                    board[i][j]=-1 #新的细胞死亡
                if board[i][j]==0 and live==3:
                    board[i][j]=2 #死细胞复活
        for i in range(m):
            for j in range(n):
                if board[i][j]>0:
                    board[i][j]=1
                else:
                    board[i][j]=0
