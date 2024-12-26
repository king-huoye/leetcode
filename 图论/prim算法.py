
v,e=map(int,input().split())
graph=[[10001]*(v+1) for _ in range(v+1)]
for i in range(e):
    x,y,w=list(map(int,input().split()))
    graph[x][y]=w 
    graph[y][x]=w  #无向图要设置两次
visited=[False]*(v+1)
minDist=[10001]*(v+1)
 
for _ in range(1,v+1):这个循环用于遍历每一个节点，v 是节点总数，循环从 1 到 v，意味着所有节点都需要遍历一次。
    min_val=10002
    cur=-1
    for j in range(1,v+1):选择最小边,更新最小距离
        if visited[j]==False and minDist[j]<min_val:
            cur=j 
            min_val=minDist[j]
    visited[cur]=True
    for j in range(1,v+1):
        if visited[j]==False and minDist[j]>graph[cur][j]:
            minDist[j]=graph[cur][j]
ans=0
for i in range(2,v+1):
    ans+=minDist[i] i 从 2 开始，因为节点 1 已经是最小生成树的一部分
print(ans)
