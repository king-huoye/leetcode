class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        direction=[[-1,0],[0,-1],[0,1],[1,0]]
        
        def dfs(grid,i,j,visited):
            for x,y in direction:
                next_x=x+i 
                next_y=y+j 
                if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
                    continue
                if grid[next_x][next_y]=='1' and not visited[next_x][next_y]:
                    visited[next_x][next_y]=True
                    dfs(grid,next_x,next_y,visited)
        m=len(grid)
        n=len(grid[0])
        visited=[[False]*n for _ in range(m)]
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not visited[i][j]:#发现陆地
                    count+=1
                    visited[i][j]=True
                    dfs(grid,i,j,visited)
        return count
