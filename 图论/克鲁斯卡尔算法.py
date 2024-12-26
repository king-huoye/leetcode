class Edge:
    def __init__(self, l, r, val):
        self.l = l
        self.r = r
        self.val = val

class UnionFind:
    def __init__(self, n):
        self.father = list(range(n))

    def find(self, u):
        if self.father[u] == u:
            return u
        else:
            # 路径压缩
            self.father[u] = self.find(self.father[u])
            return self.father[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.father[root_u] = root_v

def kruskal(v, edges):
    # Kruskal算法
    edges.sort(key=lambda edge: edge.val)  # 按照边的权值排序
    uf = UnionFind(v + 1)  # 初始化并查集（节点编号从1开始，所以大小为v+1）
    result_val = 0  # 最小生成树的总权值
    for edge in edges:
        if uf.find(edge.l) != uf.find(edge.r):  # 如果l和r不在同一个集合
            uf.union(edge.l, edge.r)  # 合并集合
            result_val += edge.val  # 加上边的权值
    return result_val

# 输入节点数和边数
v, e = map(int, input().split())
edges = []

# 输入每条边的信息
for _ in range(e):
    x, y, w = map(int, input().split())
    edges.append(Edge(x, y, w))

# 计算最小生成树的权值总和
result = kruskal(v, edges)
print(result)
