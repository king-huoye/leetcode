from collections import deque
directions=[[-1,0],[0,-1],[1,0],[0,1]]#确定方向
def bfs(arr,x,y,visited):
    que=deque([])
    que.append([x,y])
    while que:
        cur_x,cur_y=que.popleft()#队列取出当前坐标
        for i,j in directions:
            next_x=cur_x+i 
            next_y=cur_y+j 
            if next_x<0 or next_x>=len(arr) or next_y<0 or next_y>=len(arr[0]):
                continue
            if arr[next_x][next_y]==1 and not visited[next_x][next_y]:
                visited[next_x][next_y]=True
                que.append([next_x,next_y])#加入队列的时候再把visited数组设置为True
if __name__ == '__main__':
    n,m=map(int,input().split())
    grid=[]
    for _ in range(n):
        grid.append(list(map(int,input().split())))#每一行的数据以list加入
    visited=[[False]*m for _ in range(n)]
    count=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and not visited[i][j]:
                count+=1 
                bfs(grid,i,j,visited)#这里不用标记，在上面队列哪里才需要
    print(count)
    
