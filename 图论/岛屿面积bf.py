
position=[[-1,0],[0,-1],[0,1],[1,0]]
from collections import deque
def bfs(graph,x,y,visited):
    que=deque()
    que.append([x,y])
    global count
    while que:
        x_,y_=que.popleft()
        for i,j in position:
            cur_x=x_+i 
            cur_y=y_+j 
            if cur_x<0 or cur_x>=len(graph) or cur_y<0 or cur_y>=len(graph[0]):
                continue
            if graph[cur_x][cur_y]==1 and not visited[cur_x][cur_y]:
                visited[cur_x][cur_y]=True 
                count+=1 
                que.append([cur_x,cur_y])
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
visited=[[False]*m for _ in range(n)]
result=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and not visited[i][j]:
            visited[i][j]=True
            count=1 
            bfs(graph,i,j,visited)
            result=max(result,count)
print(result)
