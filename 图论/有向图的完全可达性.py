import collections

def dfs(graph,n,visited):
    for nei in graph[n]:#搜索n节点连接过的点
        if not visited[nei]:
            visited[nei]=True
            dfs(graph,nei,visited)
#更好理解
def main():
    N,K=map(int,input().split())
    graph=collections.defaultdict(list)#建立邻接表形式的
    for _ in range(K):
        a,b=map(int,input().split())
        graph[a].append(b)#表示a到b节点是可达的
    visited=[False]*(N+1)
    visited[1]=True
    dfs(graph,1,visited)
    for i in range(1,N+1):
        if not visited[i]:
            print(-1)
            return 
    print(1)

if __name__ == '__main__':
    main()
    
