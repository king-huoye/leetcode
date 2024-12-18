
direction=[[-1,0],[0,1],[0,-1],[1,0]]
result=0 #全局变量的定义要注意
def dfs(graph,x,y,visited):
    global result
    result+=1 
    for i,j in direction:
        cur_x=x+i 
        cur_y=y+j 
        if cur_x<0 or cur_x>=len(graph) or cur_y<0 or cur_y>=len(graph[0]):
            continue
        if graph[cur_x][cur_y]==1 and not visited[cur_x][cur_y]:
            visited[cur_x][cur_y]=True 
            dfs(graph,cur_x,cur_y,visited)

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
visited=[[False]*m for _ in range(n)]
#处理边界
for i in range(n):
    if graph[i][0]==1 and not visited[i][0]:
        visited[i][0]=True 
        dfs(graph,i,0,visited)
    if graph[i][m-1]==1 and not visited[i][m-1]:
        visited[i][m-1]=True 
        dfs(graph,i,m-1,visited)

for j in range(m):
    if graph[0][j]==1 and not visited[0][j]:
        visited[0][j]=True
        dfs(graph,0,j,visited)
    if graph[n-1][j]==1 and not visited[n-1][j]:
        visited[n-1][j]=True
        dfs(graph,n-1,j,visited)

result=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and not visited[i][j]:
            visited[i][j]=True 
            dfs(graph,i,j,visited)
print(result)
