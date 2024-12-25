
from collections import defaultdict

class Union:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
    
    def find(self,u):
        if self.parent[u]==u:
            return u 
        else:
            return self.find(self.parent[u])
    def union(self,u,v):
        root_u=self.find(u)
        root_v=self.find(v)
        if root_v!=root_u:
            self.parent[root_v]=root_u
    def same(self,u,v):
        return self.find(u)==self.find(v)
    
    def judge(self,edges,edge):
        for i in range(len(edges)):
            if i==edge:
                continue
            s,t=edges[i]
            if self.same(s,t):
                return False
            else:
                self.union(s,t)
        return True 
    def remove(self,edges):
        for s,t in edges:
            if self.same(s,t):
                print(s,t)
                return 
            else:
                self.union(s,t)
if __name__ == '__main__':
    n=int(input())
    Un=Union(n)
    edges=[]
    in_degree=defaultdict(int)
    for i in range(n):
        s,t=map(int,input().split())
        in_degree[t]+=1 
        edges.append([s,t])
    vec=list()
    for i in range(n-1,-1,-1):
        if in_degree[edges[i][1]]==2:
            vec.append(i)
    if len(vec)>0:
        if Un.judge(edges,vec[0]):
            print(edges[vec[0]][0],edges[vec[0]][1])
        else:
            print(edges[vec[1]][0],edges[vec[1]][1])
    else:
        Un.remove(edges)
