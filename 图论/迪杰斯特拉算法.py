
def djstral(n,m,edges,start,end):
    grid=[[float('inf')]*(n+1) for _ in range(n+1)]
    for x,y,w in edges:
        grid[x][y]=w 
    #构建邻接矩阵
    minDist=[float('inf')]*(n+1)
    visited=[False]*(n+1)
    minDist[start]=0 #初始距离为0
    for _ in range(1,n+1):
        minval=float('inf')
        cur=-1
        for i in range(1,n+1):
            if not visited[i] and minDist[i]<minval:
                minval=minDist[i]
                cur=i
        if cur==-1:
            break #找不到未访问过的节点,提前结束
        visited[cur]=True #标记节点已经访问了
        for i in range(1,n+1):
            if not visited[i] and grid[cur][i]!=float('inf') and minDist[cur]+grid[cur][i]<minDist[i]:
                minDist[i]=minDist[cur]+grid[cur][i]
    if minDist[end]==float('inf'):
        return -1 
    else:
        return minDist[end]
    


if __name__ == '__main__':
    n,m=map(int,input().split())
    edges=[]
    for _ in range(m):
        x,y,w=map(int,input().split())
        edges.append([x,y,w])
    start=1 
    end=n 
    result=djstral(n,m,edges,start,end)
    print(result)
    
