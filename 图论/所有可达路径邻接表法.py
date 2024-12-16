from  collections import defaultdict
result=[]
path=[]
def dfs(graph,x,n):
    if x==n:
        result.append(path[:])
    for i in graph[x]:#找到指向x的节点
        path.append(i)
        dfs(graph,i,n)
        path.pop()
if __name__ == '__main__':
    n,m=map(int,input().split())
    graph=defaultdict(list)#邻接表
    path.append(1)
    for _ in range(m):
        s,t=map(int,input().split())
        graph[s].append(t)
    dfs(graph,1,n)
    if not result:
        print(-1)
    else:
        for tmp in result:
            print(' '.join(map(str,tmp)))
