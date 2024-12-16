def dfs(graph,x,n,path,result):
    if x==n:#遍历的节点到终点收集结果
        result.append(path[:])
    for i in range(1,n+1):
        if graph[x][i]==1:
            path.append(i)
            dfs(graph,i,n,path,result)
            path.pop()
if __name__ == '__main__':
    n,m=map(int,input().split())#这种输入格式要注意,转为整数
    graph=[[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        s,t=map(int,input().split())
        graph[s][t]=1 #s到t是连通的表明
    result=[]
    dfs(graph,1,n,[1],result)
    if not result:
        print(-1)
    else:
        for tmp in result:
            print(' '.join(map(str,tmp)))
