class Union:
    def __init__(self,n):
        self.parent=list(range(n+1))#初始化并查集
    def find(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.find(self.parent[u])
        return self.parent[u]
    def un(self,u,v):
        root_u=self.find(u)
        root_v=self.find(v)
        if root_v!=root_u:
            self.parent[root_v]=root_u # v的根节点指向u,这里指向没所谓只是效率的问题
    def Same(self,u,v):
        return self.find(u)==self.find(v)
def main():
    n,m=map(int,input().split())
    uf=Union(n)
    for _ in range(m):#要读取的是边的数目而不是结点的数目
        s,t=map(int,input().split())
        uf.un(s,t)
    source, destination = map(int, input().split())#最后一个输入的
    if uf.Same(source,destination):
        print(1)
    else:
        print(0)
    
if __name__ == '__main__':
    main()
