class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction=[[-1,0],[0,1],[0,-1],[1,0]]
        if not grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        que=deque()
        fresh=0
        minute=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    que.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1
        while que and fresh>0:
            for i in range(len(que)):
                x,y=que.popleft()
                for j,k in direction:
                    new_x=x+j
                    new_y=y+k
                    if new_x<0 or new_x>=m or new_y<0 or new_y>=n:
                        continue
                    elif grid[new_x][new_y]==1:
                        fresh-=1
                        grid[new_x][new_y]=2 #腐蚀
                        que.append([new_x,new_y])
            minute+=1 #全部走完
        if fresh>0:
            return -1
        else:
            return minute
