position=[[-1,0],[0,-1],[0,1],[1,0]]

def dfs(grid,x,y):
    grid[x][y]=2 #进入dfs把陆地的1改为2全部
    for i,j in position:
        cur_x=x+i 
        cur_y=y+j 
        if cur_x<0 or cur_x>=len(grid) or cur_y<0 or cur_y>=len(grid[0]):
            continue
        if grid[cur_x][cur_y]==2 or grid[cur_x][cur_y]==0:#不符合条件
            continue
        dfs(grid,cur_x,cur_y)
def main():
    n,m=map(int,input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int,input().split())))
    for i in range(n):
        if grid[i][0]==1:
            dfs(grid,i,0)#把边界进行遍历
        if grid[i][m-1]==1:
            dfs(grid,i,m-1)#先处理
    #后处理
    for j in range(m):
        if grid[0][j]==1:
            dfs(grid,0,j)
        if grid[n-1][j]==1:
            dfs(grid,n-1,j)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                grid[i][j]=0 
            if grid[i][j]==2:
                grid[i][j]=1 
    for row in grid:
        print(' '.join(map(str,row)))
if __name__ == '__main__':
    main()
        
