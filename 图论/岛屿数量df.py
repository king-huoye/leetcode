
directions=[[-1,0],[0,-1],[1,0],[0,1]]#确定方向
def dfs(arr,x,y,visited):
    for i,j in directions:
        next_x=x+i 
        next_y=y+j 
        if next_x<0 or next_x>=len(arr) or next_y<0 or next_y>=len(arr[0]):
            continue
        if arr[next_x][next_y]==1 and not visited[next_x][next_y]:
            visited[next_x][next_y]=True
            dfs(arr,next_x,next_y,visited)
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
                visited[i][j]=True #遍历过的就设为true
                dfs(grid,i,j,visited)
    print(count)
    
