position=[[-1,0],[0,-1],[0,1],[1,0]]

def dfs(graph,x,y,visited):
    global count
    for i,j in position:
        cur_x=x+i 
        cur_y=y+j 
        if cur_x<0 or cur_x>=len(graph) or cur_y<0 or cur_y>=len(graph[0]):
            continue
        if graph[cur_x][cur_y]==1 and not visited[cur_x][cur_y]:
            visited[cur_x][cur_y]=True 
            count+=1  记录当前连通区域的大小
            dfs(graph,cur_x,cur_y,visited)
n,m=map(int,input().split())
visited=[[False]*m for _ in range(n)]
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

result=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and not visited[i][j]:
            visited[i][j]=True 
            count=1 开始时当前连通区域至少包含1个节点
            dfs(graph,i,j,visited)
            result=max(result,count)
print(result)
