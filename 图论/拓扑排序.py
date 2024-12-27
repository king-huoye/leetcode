from collections import defaultdict,deque

def tuopu(n,edges):
    in_degree=[0]*n
    ma=defaultdict(list)
    for s,t in edges:
        ma[s].append(t)
        in_degree[t]+=1
    queue=deque([i for i in range(n) if in_degree[i]==0])#把入度为0的先加入队列
    result=[]
    while queue:
        cur=queue.popleft()
        result.append(cur)#加入结果
        for file in ma[cur]:
            in_degree[file]-=1 
            if in_degree[file]==0:
                queue.append(file)#入度为0的加入
    if len(result)==n:
        print(" ".join(map(str,result)))
    else:
        print(-1)
        
    
if __name__ == '__main__':
    n,m=map(int,input().split())
    edges=[list(map(int,input().split())) for _ in range(m)]
    tuopu(n,edges)
