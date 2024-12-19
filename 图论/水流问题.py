
position=[[-1,0],[0,-1],[0,1],[1,0]]
first=set()
second=set()


def dfs(grid,x,y,visited,mode):
    if visited[x][y]==True:
        return #遍历过的就不管
    visited[x][y]=True #先标记
    mode.add((x,y))
    for i,j in position:
        cur_x=x+i 
        cur_y=y+j 
        if 0<=cur_x<len(grid) and 0<=cur_y<len(grid[0]) and grid[cur_x][cur_y]>=grid[x][y]:
            dfs(grid,cur_x,cur_y,visited,mode)
#要分别从两个边界去进行遍历，逆向去
def main():
    global first #把集合扔进去
    global second
    n,m=map(int,input().split())
    visited=[[False]*m for _ in range(n)]
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))
    for i in range(n):
        dfs(grid,i,0,visited,first)
    for j in range(m):
        dfs(grid,0,j,visited,first)
        
    visited=[[False]*m for _ in range(n)]
    for i in range(n):
        dfs(grid,i,m-1,visited,second)
    for j in range(m):
        dfs(grid,n-1,j,visited,second)
        
    result=first&second
    for x,y in result:
        print(f"{x} {y}")
if __name__ == '__main__':
    main()
