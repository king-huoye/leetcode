import collections

area=0
postion=[[-1,0],[0,-1],[0,1],[1,0]]

def dfs(grid,x,y,visited,num):
    global area
    if visited[x][y]:
        return 
    visited[x][y]=True
    grid[x][y]=num #标记岛屿数字
    area+=1
    for i,j in postion:
        cur_x=x+i 
        cur_y=y+j 
        if 0<=cur_x<len(grid) and 0<=cur_y<len(grid[0]) and grid[cur_x][cur_y]==1:
            dfs(grid,cur_x,cur_y,visited,num)

def main():
    global area
    n,m=map(int,input().split())
    grid=[]
    visited=[[False]*m for _ in range(n)]
    for _ in range(n):
        grid.append(list(map(int,input().split())))
    record=collections.defaultdict(int)
    
    cnt=2 #为了避免和数字1冲突
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                area=0
                dfs(grid,i,j,visited,cnt)
                record[cnt]=area #记录面积
                cnt+=1 
    
    
    res=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==0:
                max_island=1 #水边陆地，1开始计算
                v=set()
                for x,y in postion:
                    new_x=x+i 
                    new_y=y+j 
                    if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]) and grid[new_x][new_y]!=0 and grid[new_x][new_y] not in v:#不能重复收集
                        max_island+=record[grid[new_x][new_y]]
                        v.add(grid[new_x][new_y])
                res=max(res,max_island)
    if res==0:
        return max(record.values()) #无水的情况
    return res 
if __name__ == '__main__':
    a=main()
    print(a)
                        
